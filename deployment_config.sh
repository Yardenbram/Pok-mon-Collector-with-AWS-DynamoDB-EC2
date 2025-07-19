AWS_REGION="eu-central-1" # AWS region used across the app (must match app.py)
EC2_AMI_ID="ami-0xxxxxxxxxxxxxx" # AMI ID for Ubuntu or Amazon Linux in your region (get from EC2 console)
EC2_INSTANCE_TYPE="t2.micro" # Choose instance type based on your app’s needs (e.g., t2.micro or t3.micro)
EC2_KEY_PAIR_NAME="your-key-pair-name" # Replace with the name of your existing EC2 key pair
GITHUB_REPO_URL="https://github.com/your-username/pokemon-collector.git" # Link to your exact GitHub repository
DYNAMODB_TABLE_NAME="PokemonCollection" # Must match the table name used in app.py
DYNAMODB_PRIMARY_KEY="pokemon_name" # This should align with the primary key defined in app.py schema
