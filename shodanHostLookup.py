import json, requests, argparse, os

parser = argparse.ArgumentParser(prog='shodanHostLookup', description='This script returns the shodan API result for an IP, turn it to json and print it')

parser.add_argument('host', help='The IP address of the target')
parser.add_argument('-k', '--key', required=True, help='Shodan\'s API key')
parser.add_argument('-f', '--format', help='Format to display the datas text / json')
parser.add_argument('-o', '--output', help='The path for the output file')

args = parser.parse_args()


# Variables
api_key = (args.key)

# Lookup an IP using shodan's REST API
response = requests.get(f'https://api.shodan.io/shodan/host/{args.host}?key={api_key}')


# The response text type is a string, so try to convert to dictionary
hinfd = json.loads(response.text)

# Format the output (indent, sort keys and don't convert Unicode) for printing JSON
host_info_json = json.dumps(hinfd, indent=4, sort_keys=True, ensure_ascii=False)
# print(host_info_json)

# Create the path and dir for the output

if args.output:
     
    output_file = os.path.join(args.output)
    with open(output_file, 'w') as f:
        f.write(host_info_json)
    print(f"Results saved to {output_file}")

# Print the hostname from the dictionary

# Safe printing with defaults for missing keys
hostname = hinfd.get('hostnames', 'N/A')
ip_str = hinfd.get('ip_str', 'N/A')
ports = hinfd.get('ports', 'N/A')
os = hinfd.get('os', 'N/A')
country_code = hinfd.get('country_code', 'N/A')
asn = hinfd.get('asn', 'N/A')
tags = hinfd.get('tags', 'N/A')
vulns = hinfd.get('vulns', 'N/A')
last_update = hinfd.get('last_update', 'N/A')

print(f"Hostname is:\t{hostname}\nIP Address is:\t{ip_str}\nPorts:\t{ports}\nOperating system:\t{os}\nLocation:\t{country_code}\nAsn:\t{asn}\nTags:\t{tags}\nKnown vulns\t{vulns}\nLast update:\t{last_update}")

if (args.format) == 'text':
    print(response.text)
elif (args.format) == 'json':
    print(host_info_json)


