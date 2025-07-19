import requests
import boto3
import random
import json  # Helps print JSON in a readable way

# DynamoDB settings
DYNAMODB_TABLE_NAME = "PokemonCollection"  # Replace with your DynamoDB table name
REGION_NAME = "your-aws-region"  # For example: "eu-central-1" or "us-east-1"

# Create a DynamoDB resource object (uses IAM role credentials of the EC2 or environment)
dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

def get_random_pokemon_name():
    """Fetch a random Pokémon name from the PokeAPI."""
    try:
        response = requests.get(f"{POKEAPI_BASE_URL}pokemon?limit=10000")  # Get a big list of Pokémon
        response.raise_for_status()  # Stop the code if the request fails
        data = response.json()
        pokemon_list = data['results']
        random_pokemon = random.choice(pokemon_list)
        return random_pokemon['name']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokémon list: {e}")
        return None

def get_pokemon_details(pokemon_name):
    """Fetch detailed info of a specific Pokémon from the PokeAPI."""
    try:
        response = requests.get(f"{POKEAPI_BASE_URL}pokemon/{pokemon_name}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokémon details for '{pokemon_name}': {e}")
        return None

def save_pokemon_to_db(pokemon_data):
    """Save Pokémon details to DynamoDB."""
    try:
        # Define the item to save according to your table's structure
        item = {
            'pokemon_name': pokemon_data['name'],
            'id': pokemon_data['id'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'types': [t['type']['name'] for t in pokemon_data['types']],
            'abilities': [a['ability']['name'] for a in pokemon_data['abilities']],
            'base_experience': pokemon_data.get('base_experience'),  # Use get in case the key is missing
            'sprite_front_default': pokemon_data['sprites']['front_default'] if 'front_default' in pokemon_data['sprites'] else None
        }
        table.put_item(Item=item)
        print(f"Pokémon '{pokemon_data['name']}' was saved successfully to DynamoDB.")
    except Exception as e:
        print(f"Error saving Pokémon to the database: {e}")

def get_pokemon_from_db(pokemon_name):
    """Retrieve Pokémon details from DynamoDB."""
    try:
        response = table.get_item(Key={'pokemon_name': pokemon_name})
        return response.get('Item')
    except Exception as e:
        print(f"Error retrieving Pokémon from the database: {e}")
        return None

def display_pokemon_details(pokemon_details):
    """Print Pokémon details in a nice format."""
    if not pokemon_details:
        print("No Pokémon details found.")
        return

    print("\n--- Pokémon Details ---")
    print(f"Name: {pokemon_details.get('pokemon_name', 'N/A').capitalize()}")
    print(f"ID: {pokemon_details.get('id', 'N/A')}")
    print(f"Height: {pokemon_details.get('height', 'N/A')}")
    print(f"Weight: {pokemon_details.get('weight', 'N/A')}")
    print(f"Types: {', '.join([t.capitalize() for t in pokemon_details.get('types', ['N/A'])])}")
    print(f"Abilities: {', '.join([a.capitalize() for a in pokemon_details.get('abilities', ['N/A'])])}")
    print(f"Base Experience: {pokemon_details.get('base_experience', 'N/A')}")
    if pokemon_details.get('sprite_front_default'):
        print(f"Image URL: {pokemon_details['sprite_front_default']}")
    print("------------------------\n")

def main():
    while True:
        choice = input("Would you like to fetch a random Pokémon? (yes/no): ").lower()

        if choice == 'yes':
            pokemon_name = get_random_pokemon_name()
            if not pokemon_name:
                continue

            print(f"Selected Pokémon: {pokemon_name.capitalize()}")

            # Check if the Pokémon already exists in the DB
            db_pokemon = get_pokemon_from_db(pokemon_name)

            if db_pokemon:
                print(f"Pokémon '{pokemon_name.capitalize()}' already exists in the database.")
                display_pokemon_details(db_pokemon)
            else:
                print(f"Pokémon '{pokemon_name.capitalize()}' is not in the database. Fetching details and saving...")
                api_pokemon_details = get_pokemon_details(pokemon_name)
                if api_pokemon_details:
                    save_pokemon_to_db(api_pokemon_details)
                    display_pokemon_details(api_pokemon_details)
        elif choice == 'no':
            print("Goodbye! Hope you enjoyed your Pokémon collection!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()
