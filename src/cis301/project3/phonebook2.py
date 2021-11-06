from cis301.objects.human import Human

class Person(Human):
    def __init__(self, name, email, phone, cell):
        super().__init__(name)
        self.email = email
        self.phone = phone
        self.cell = chr

    def __str__(self):
        return f'Name:{self.name}\t Email:{self.email}\t Phone:{self.phone}'
    def __eq__(self, other):
        if self.name == other.name and \
            self.email == other.email and \
            self.phone == other.phone and \
            self.cell == other.cell:
            return True
        else:
            return False
    def toCSV(self):
        return f'{self.name}, {self.email}, {self.phone}, {self.cell}\n'
    def toJSON(self):
        return '{"name":"'+self.name+'", "email:" , '+self.email+',' "phone":
        +self.phone+'"}'

class PhoneBook:

    def __init__(self, owner):
        self.owner = owner
        self.contacts = list()

    def add_contact(self, person):
        if(not isinstance(person, Person)):
            return
        self.contacts.append(person)

    def search_byname(self, name):
        for person in self.contacts:
            if person.name == name:
                return person
            return None

    def toJSON(self):
        contacts ="["
        for contact in self.contacts:
            contacts_json += contact.toJSON()+','
            contacts_json = contacts_json.rstrip(',')+']'
        phonebook_json = '{'
        phonebook_json += '"owner":'+self.owner+',"contacts":'+contacts_json
        phonebook_json += '}'
        return phonebook_json
