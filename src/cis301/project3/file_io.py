import csv
from dataclasses import fields

phonebook = {"0": {"name": "Mya", "phone": "111-222-3333"}, " 1": {"A"}}
phonebook_copy = {}


def store_phonebook():
    with open("phonebook.txt", 'w') as filename:
        filename.write("name, phone\r\n")
        for contact in phonebook.values():
            ent = f"{contact['name']},{contact['phone']}\n "
            filename.write(ent)


def load_phonebook():
    with open("phonebook.txt", 'r') as filename:
        contacts = filename.readlines()

    phonebook_copy = dict()
    index = 0
    for contact in contacts:
        # phonebook[index] = {"name: contact"}
        print(contact)

def csv_store():
    with open("phonebook.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow("name, phone")

        for contact in phonebook.values():
            ent = f"{contact['name']},{contact['phone']}\n "
            csvwriter.writerow(ent)

def csv_store():
    with open("phonebook.csv", 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(phonebook)

def csv_load():
    with open("phonebook.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        phonebook_copy = dict()
        indx = 0
        for row in csvreader:
            phonebook_copy[indx] = {"name": row[0], "phone": row[1]}
            indx+=1
        print("Phone Book Copy")
        print(phonebook_copy)

if __name__ == '__main__':
    store_phonebook()
    load_phonebook()
    csv_store()
    csv_load()

