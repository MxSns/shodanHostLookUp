
  ██████  ██░ ██  ▒█████  ▓█████▄  ▄▄▄       ███▄    █     ██░ ██  ▒█████    ██████ ▄▄▄█████▓
▒██    ▒ ▓██░ ██▒▒██▒  ██▒▒██▀ ██▌▒████▄     ██ ▀█   █    ▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
░ ▓██▄   ▒██▀▀██░▒██░  ██▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒   ▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
  ▒   ██▒░▓█ ░██ ▒██   ██░░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒   ░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ 
▒██████▒▒░▓█▒░██▓░ ████▓▒░░▒████▓  ▓█   ▓██▒▒██░   ▓██░   ░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░  ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒     ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   
░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░  ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    
░  ░  ░   ░  ░░ ░░ ░ ░ ▒   ░ ░  ░   ░   ▒      ░   ░ ░     ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      
      ░   ░  ░  ░    ░ ░     ░          ░  ░         ░     ░  ░  ░    ░ ░        ░           
                           ░                                                                 
 ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
    ░  ░    ░ ░      ░ ░  ░  ░      ░              



# shodanHostLookup

A simple Python script to query the shodan API for detailed information about a given IP addresse.
It fetches host data using Shodan's REST API, converts the response to JSON, and provides options to display or save the results in various formats.
Useful for OSINT(open source intelligence) and penetration testing reconnaissance.

# Features

- Retrieves Shodan host information for a specified IP.
- Supports output in raw text or formatted JSON
- Optionally saves results to a file
- Iterates and prints key details like ports, banners, vulnerabilities, and more for easy readability
- Handles nested data (e.g., service banners under 'data')

# Requirements

- Python 3.x
- Required librairies : requests, json, argparse, os (these are standard or can be installed via
`pip install requests` if needed
- A valid Shodan API key (sign up at shodan.io for a free or paid account).

# Installation

- Clone or download the script to your local machine
- Ensure Python is installed and accessible
- Install requests if not aready present :

`pip install requests`

# Usage

Run the script from the command line, providing the required arguments

`python3 shodanHostLookup.py <host> -k <api_key> [-f <format>] [-o <output_path>]`

# Arguments

- host (required): The IP address to query (e.g., 8.8.8.8).
- -k, --key (required): Your Shodan API key.
- -f, --format (optional): Display format for the data. Options: text (raw API response) or json (pretty-printed JSON). If omitted, only the detailed iterated output is printed.
- -o, --output (optional): Path to save the JSON results as a file. The directory will be created if it doesn't exist.

# Output

## Detailed Response is always printed by default. Iterates over the JSON dictionary:

- Top-level fields (e.g., ip str, hostnames, ports, os, etc.) are shown as key: value.
- For the 'data' field (a list of services), it prints sub-details like Port, Banner, and Vulns for each item.
- Missing values in nested fields are shown as N/A.

## Format-Specific Output (if -f is used):

- text: Raw string from the API response.
- json: Pretty-printed JSON with indentation, sorted keys, and preserved Unicode.

- File Output (if -o is used): Saves the pretty JSON to the specified file and confirms with a message (e.g., "Results saved to results.json").


