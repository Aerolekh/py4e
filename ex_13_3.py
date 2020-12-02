import json,ssl
import urllib.request,urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#Stroring the given parameters
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
# sample_address = "South Federal University"
address = input("Enter location: ")
address_wanted = address

#Setting the GET parameters on the URL
parameters = {"address": address_wanted, "key":api_key}
formatted_url = urllib.parse.urlencode(parameters)

#Generating the complete URL. Printing it in order to check if it's correct.
url = serviceurl.strip() + formatted_url.strip()
print("Retrieving", url)

data_read = urllib.request.urlopen(url, context=ctx).read()
data = data_read.decode()
print('Retrieved', len(data), 'characters')

j_data = json.loads(data)
place_id = j_data["results"][0]["place_id"]
print("Place id ", place_id)
