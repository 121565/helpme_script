# Helpme Script
Very easy to use script for getting command help in the terminal
The function can be used in two ways:
1. Get guidance on a known command
helpme [COMMAND] [DESCRIPTION]
Here the user can prompt the LLM to help using a certain command.
E.g `helpme git Get all changes from master`
In this example a prompt is sent to goose to find out how `git` should be used to get all changes from master


2. Get terminal guidance for an unknown command
helpme - [DESCRIPTION]
Here a prompt is sent through goose to find any terminal command(s) that will satisfy the request




# To install:

This script is intended to be used in the terminal in tandem with goose
Please follow the goose CLI installation guide before using the script

https://block.github.io/goose/docs/quickstart/

After downloading goose and configuring the LLM model you want to use please add the "helpme" script to your .local/python/bin folder for ease of access
