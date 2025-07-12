import json, requests, argparse

parser = argparse.ArgumentParser(prog='shodanHostLookup', description='This script returns the shodan API result for an IP, turn it to json and print it')

parser.add_argument('host', help='The IP address of the target')
parser.add_argument('-k', '--key', required=True, help='Shodan\'s API key')
parser.add_argument('-f', '--format', help='Format to display the datas text / json')

args = parser.parse_args()


# Get an API key from shodan and include it here
api_key = (args.key)

# Lookup an IP using shodan's REST API
response = requests.get(f'https://api.shodan.io/shodan/host/{args.host}?key={api_key}')


# The response text type is a string, so try to convert to dictionary
hinfd = json.loads(response.text)

# Format the output (indent, sort keys and don't convert Unicode) for printing JSON
host_info_json = json.dumps(hinfd, indent=4, sort_keys=True, ensure_ascii=False)
# print(host_info_json)

# Print the hostname from the dictionary
print("Hostname is:\t" + str(hinfd['hostnames']) + "\nIP address is:\t" + str(hinfd['ip_str']) + "\nPorts:\t" + str(hinfd['ports']) + "\nOperating system:\t" + str(hinfd['os']) + "\nLocation\t" + str(hinfd['country_code']) + "8asn:\t" + str(hinfd['asn']) + "\nTags:\t"+ str(hinfd['tags']) + "\nLast update :\t" + str(hinfd['last_update']))

if 'vulns' not in hinfd:
    print("No vulns found")
else:
    print("\nVulnerabilities\t" + str(hinfd['vulns']))

if (args.format) == 'text':
    print(response.text)
elif (args.format) == 'json':
    print(host_info_json)


