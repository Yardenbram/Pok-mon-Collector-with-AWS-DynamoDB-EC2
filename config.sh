AWS_REGION="eu-central-1" # Define your AWS region (must align with other config files)
DYNAMODB_TABLE_NAME="PokemonCollection" # Set the table name exactly as used in your setup
IAM_ROLE_NAME="PokemonAppEC2Role" # This must match the role name from deploy.sh
SECURITY_GROUP_NAME="PokemonAppSG" # Should be identical to the security group name defined in deploy.sh
LAUNCH_TEMPLATE_NAME="PokemonAppLaunchTemplate" # Ensure this name matches the one created in deploy.sh

# You might need to manually set the INSTANCE_ID below if the cleanup script fails to retrieve it automatically.
# Example: INSTANCE_ID="i-0xxxxxxxxxxxxxxxxxxxx"
