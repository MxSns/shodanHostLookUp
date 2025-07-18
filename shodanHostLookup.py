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

ipinfo_dict = json.loads(response.text)

# Format the output
host_info_json = json.dumps(ipinfo_dict, indent=4, sort_keys=True, ensure_ascii=False)

# Create the path and dir for the output

if args.output:     
    output_file = os.path.join(args.output)
    with open(output_file, 'w') as f:
        f.write(host_info_json)
    print(f"Results saved to {output_file}")

# Print the hostname from the dictionary

print ("\nDetailed response:\n")
for key, value in ipinfo_dict.items():
    if isinstance(value, list) and key == 'data':
        print(f"{key}:")
        for item in value:
            print(f"\tPort: {item.get('port', 'N/A')}")
            print(f"\tBanner: {item.get('banner', 'N/A')}")
            print(f"\tVulns: {item.get('vulns', 'N/A')}")
    else:
        print(f"{key}:\t{value}")

if (args.format) == 'text':
    print(response.text)
elif (args.format) == 'json':
    print(host_info_json)


