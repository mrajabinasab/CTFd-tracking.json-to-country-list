import os
import json
import pycountry
from geoip import geolite2

#Reading CTFd tracking file
input_file = open('tracking.json', 'r')
tracking = input_file.readlines()
#Reformatting tracking file for easy usage
reformat = '[' + tracking[0].split('[')[1].lstrip().split(']')[0] + ']'
ready = open('ready.json', 'w')
ready.write(reformat)
ready.close()
#Reading reformatted json file
jsonfile = open('ready.json')
json_array = json.load(jsonfile)
jsonfile.close()
os.remove('ready.json')
ip_list = []
country_list = []
#Gathering ip list
for item in json_array:
    if item['ip'] not in ip_list:
        ip_list.append(item['ip'])
#Converting ip list to country name list
for ip in ip_list:
    lookup = geolite2.lookup(ip)
    if lookup is not None:
        if lookup.country is not None:
            country = pycountry.countries.get(alpha_2 = lookup.country)
            if country.name not in country_list:
                country_list.append(country.name)
#Sorting country names
country_list = sorted(country_list)
#Saving the results to country_list.txt
file = open('country_list.txt', 'w')  
for country in country_list:
    file.write(country + '\n')
file.close()
