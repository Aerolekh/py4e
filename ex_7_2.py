# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
line_count = 0
total_number = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line_count += 1
    #total_lines = line_count + 1
    start = line.find(":")
    line_value = line[start + 2:]
    number = float(line_value)
    total_number += number

    #print(number)
average = total_number / line_count
print("Average spam confidence:", average)
