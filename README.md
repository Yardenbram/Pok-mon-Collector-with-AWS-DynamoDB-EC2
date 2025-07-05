Overview
This project demonstrates a lightweight Python application that integrates with the public PokeAPI to fetch, manage, and store Pokémon data using AWS services. It includes a fully automated infrastructure setup leveraging Bash scripts to deploy the necessary AWS components and ensures the application is installed and launched on an EC2 instance seamlessly.

Project Objectives
Retrieve random Pokémon data from PokeAPI.

Store Pokémon records in a DynamoDB table.

Check if a Pokémon already exists in the database before saving.

Display stored Pokémon data to the user.

Automate infrastructure deployment using AWS CLI and Bash.

Automatically install and run the app on the EC2 server post-deployment.

Architecture Summary
The system consists of the following cloud and API components:

Amazon EC2 – A Linux virtual machine that runs the Python application.

AWS DynamoDB – A fully managed NoSQL database used to persist Pokémon data.

IAM Role – Grants the EC2 instance secure permissions to access DynamoDB.

Security Group – Controls inbound (SSH) and outbound (internet) traffic for the EC2 instance.

PokeAPI – A public REST API providing real-time Pokémon metadata.

