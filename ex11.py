import re

line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
x = re.findall('\S+?@\S+', line)
y = re.findall("[a-z0-9]", line)
z = re.findall("[0-9]+", line)
print(z)
print(y)
print("X is:", x)

xz = 'From: Using the : character'
yz = re.findall('^F.+:', xz)
print(yz)

zz = re.findall("@(\S+)", line)
print(zz)

print("\nAssignment 1")

text = open('regex_sum_1041866.txt')
num_list = list()

for line in text:
    line = line.rstrip()
    numbers = re.findall("[0-9]+", line)

    if len(numbers) < 1:
        continue

    for number in numbers:
        num_list.append(int(number))

print(sum(num_list))
