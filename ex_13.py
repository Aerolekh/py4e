import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter URL: ")

uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment/count')

counts = tree.findall('.//count')
nums = list()
count = 0
for each in counts:
    nums.append(int(each.text))
    count += 1
print(f"Count: {count}")
print(f"Sum: {sum(nums)}")
