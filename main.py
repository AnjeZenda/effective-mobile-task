import os
from typing import List

FILE_NAME = 'phonebook.txt'

class Entry:
    def __init__(self, surname, name, office_phone, 
                 personal_phone, organization, fathersname):
        self.surname = surname
        self.name = name
        self.office_phone = office_phone
        self.personal_phone = personal_phone
        self.fathersname = fathersname
        self.organization = organization
    
    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.fathersname};\nOrganization: {self.organization};\nOffice phone: {self.office_phone};\nPersonal phone: {self.personal_phone};'

    def __contains__(self, item):
        return item in map(str.lower, self.__dict__.values())

    def edit(self, surname, name, office_phone, 
             personal_phone, organization, fathersname):
        self.surname = surname
        self.name = name
        self.office_phone = office_phone
        self.personal_phone = personal_phone
        self.fathersname = fathersname
        self.organization = organization
    
    def get_information(self):
        return f'{self.surname}|{self.name}|{self.fathersname}|{self.organization}|{self.office_phone}|{self.personal_phone}\n'

def print_info():
    print('Phone book')
    print('Enter 1 to view the phonebook entries')
    print('Enter 2 to add entries into the phonebook')
    print('Enter 3 to edit the phonebook entries')
    print('Enter 4 to search enrties into the phonebook')
    print('Enter 5 to print command again')
    print('Enter 6 to exit')


def load_data() -> List[Entry]:
    phonebook = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            for line in file:
                entry = line.strip().split('|')
                phonebook.append(
                    Entry(entry[0], entry[1], entry[4], entry[5], entry[3], entry[2])
                )
    return phonebook


def save_data(phonebook: List[Entry]):
    with open(FILE_NAME, 'w') as file:
        for entry in phonebook:
            file.write(entry.get_information())

def display_entries(phonebook: List[Entry], page_size = 5):
    total_entries = len(phonebook)
    num_pages = (total_entries + page_size - 1) // page_size

    for page in range(num_pages):
        print('')
        start = page * page_size
        end = min(start + page_size, total_entries)
        print(f'Page {page + 1}')
        print('-'*15)
        for i in range(start, end):
            print(phonebook[i])
            print('-'*15)
        print('')
        input('Press enter to continue...')
    



def add_entry(phonebook: List[Entry]):
    surname = input('Input surname: ')
    name = input('Input name: ')
    fathersname = input('Input fathername: ')
    organization = input('Input organization: ')
    office_phone = input('Input job phone: ')
    personal_phone = input('Input phone: ')
    phonebook.append(Entry(surname, name, office_phone, 
                           personal_phone, organization, fathersname))
    save_data(phonebook)
    print('Entry was added')
    

def edit_entry(phonebook: List[Entry]):
    print('Edit entries')
    display_entries(phonebook, len(phonebook))
    index = int(input("Enter the number of entry you\'d like to edit: ")) - 1
    if 0 <= index < len(phonebook):
        while True:
            surname = input('Input surname: ')
            name = input('Input name: ')
            fathername = input('Input fathername: ')
            organization = input('Input organization: ')
            job_phone = input('Input job phone: ')
            phone = input('Input phone: ')
            print(f'{surname} {name} {fathername} {organization} {job_phone} {phone}')
            is_correct = input('Is all correct?(Y|N)')
            if is_correct in 'YyДд':
                phonebook[index]['surname'] = surname
                phonebook[index]['name'] = name
                phonebook[index]['fathername'] = fathername
                phonebook[index]['organization'] = organization
                phonebook[index]['phone'] = phone
                phonebook[index]['job phone'] = job_phone
                print('Entry was edited')
                return
            print('Enter information again')

def search_entry(phonebook: List[Entry]):
    keyword = input('Enter the key word for searching: ').lower()
    results = []
    for entry in phonebook:
        if keyword in entry:
            results.append(entry)
    if results:
        print('Result of searching:')
        for result in results:
            print(result)
    else:
        print('Nothing was found')

def main():
    phonebook = load_data()
    print_info()
    while True:
        try:
            choice = int(input('Enter the command: '))
        except:
            print('Incorrect command. Try again.')
            continue
        match choice:
            case 1:
                display_entries(phonebook)
            case 2:
                add_entry(phonebook)
            case 3:
                edit_entry(phonebook)
            case 4:
                search_entry(phonebook)
            case 5:
                print_info()
            case 6:
                save_data(phonebook)
                print('Goodbye')
                break
    
        

if __name__ == '__main__':
    main()