name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

person_who_sent = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    e_mail = line[1]
    person_who_sent[e_mail] = person_who_sent.get(e_mail, 0) + 1

most_sent_person = None
most_sent_count = None

for person, sent in person_who_sent.items():
    if most_sent_person is None or sent > most_sent_count:
        most_sent_person = person
        most_sent_count = sent

print(most_sent_person, most_sent_count)
