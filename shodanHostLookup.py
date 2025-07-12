import json, requests, argparse

parser = argparse.ArgumentParser(prog='shodanHostLookup', description='This script returns the shodan API result for an IP, turn it to json and print it')

parser.add_argument('host', help='The IP address of the target')
parser.add_argument('-k', '--key', required=True, help='Shodan\'s API key')

args = parser.parse_args()


# Get an API key from shodan and include it here
api_key = (args.key)

# Lookup an IP using shodan's REST API
response = requests.get(f'https://api.shodan.io/shodan/host/{args.host}?key={api_key}')
print(response.text)

# The response text type is a string, so try to convert to dictionary
host_info_dictionary = json.loads(response.text)

# Format the output (indent, sort keys and don't convert Unicode) for printing JSON
host_info_json = json.dumps(host_info_dictionary, indent=4, sort_keys=True, ensure_ascii=False)
print(host_info_json)

# Print the hostname from the dictionary
print("Hostname is " + str(host_info_dictionary['hostnames']))
