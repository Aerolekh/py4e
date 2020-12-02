import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)

count = 0
nums = list()
for item in info["comments"]:
    nums.append(int(item["count"]))
    count += 1

print(f"Count: {count}")
print(f"Sum: {sum(nums)}")



