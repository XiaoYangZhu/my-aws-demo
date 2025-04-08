# Nova Act Amazon Automation

This folder contains scripts for automating Amazon shopping tasks using Amazon's Nova Act SDK. Nova Act is an experimental SDK that enables browser automation with natural language commands.

## Overview

The scripts in this folder demonstrate how to use Nova Act to automate common tasks on Amazon.com, such as logging in, searching for products, and adding items to cart.

## Files

### logon-amazon-with-userdata.py

This script demonstrates how to use Nova Act with persistent user data to automate Amazon shopping tasks. It performs the following functions:

- Checks if a user data directory exists (for storing browser session data)
- Initializes Nova Act with the Amazon.com starting page
- Checks if the user is already logged in
- If logged in, it performs a search for a coffee maker, selects the second result, and adds it to cart
- If not logged in, it prompts the user to log in manually, then performs the same search and add-to-cart actions
- Records video of the automation process

#### Key Features:

- **Session Persistence**: Uses a user data directory to maintain login state between sessions
- **Login Detection**: Uses Nova Act's schema validation to determine login status
- **Interactive Mode**: Pauses for user input when manual intervention is needed
- **Video Recording**: Captures the automation process for review

### logon-amazon-first-time.py

A simpler script that sets up a user data directory for first-time login to Amazon.com.

### logon-mail.py

Demonstrates Nova Act automation with 126.com email service, showing how to:
- Enter credentials
- Navigate the inbox
- Read and reply to emails

### NovaAct.py

A basic example script showing how to use Nova Act to search for a coffee maker on Bing and interact with search results.

## Usage

```bash
# Run the Amazon automation with existing user data
python logon-amazon-with-userdata.py

# Set up a new user data directory with Amazon login
python logon-amazon-first-time.py

# Run the email automation example
python logon-mail.py
```

## Requirements

- Python 3.10 or above
- Nova Act SDK (`pip install nova-act`)
- Valid Nova Act API key (set as environment variable `NOVA_ACT_API_KEY`)
- Operating System: MacOS or Ubuntu

## Notes

- These scripts are examples and may need modification for your specific use case
- Nova Act is an experimental SDK and may have limitations
- Be cautious with automated login scripts and never hardcode sensitive credentials
