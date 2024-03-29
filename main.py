import os
import re
from typing import List, Set, Dict

FILE_NAME: str = 'phonebook.txt'

class Entry:
    '''
    Class to represent a Entry in txt file

    Attributes
    ----------
    surname: str
        Person surname
    name: str
        Person name
    fathersname: str
        Person fathersname
    organization: str
        Organization where person works
    office_phone: str
        Person\'s office phone
    personal_phone: str
        Person\'s own phone
    '''

    def __init__(self, surname: str, name: str, office_phone: str, 
                 personal_phone: str, organization: str, fathersname: str) -> None:
        '''Initializes Entry object\'s attributes'''
        
        self.surname: str = surname
        self.name: str = name
        self.office_phone: str = office_phone
        self.personal_phone: str = personal_phone
        self.fathersname: str = fathersname
        self.organization: str = organization
    
    def __str__(self) -> str:
        '''Returns entry object string representation'''
        
        return f'{self.surname} '  +\
            f'{self.name} {self.fathersname};\n'    +\
            f'Organization: {self.organization};\n' +\
            f'Office phone: {self.office_phone};\n' +\
            f'Personal phone: {self.personal_phone};\n' + 15 * '-'

    def __contains__(self, item: str) -> bool:
        '''Checks whether item in Entry object attributes'''
        
        return item in map(str.lower, self.__dict__.values())

    def edit(self, surname: str, name: str, office_phone: str, 
             personal_phone: str, organization: str, fathersname: str) -> str:
        '''Edits the information about the Entity object'''
        
        self.surname = surname if surname != "" else self.surname
        self.name = name if name != "" else self.name
        self.office_phone = office_phone if office_phone != "" else self.office_phone
        self.personal_phone = personal_phone if personal_phone != "" else self.personal_phone
        self.fathersname = fathersname if fathersname != "" else self.fathersname
        self.organization = organization if organization != "" else self.organization
    
    def get_information(self) -> str:
        '''Returns a formatted string to save it to a file'''
        
        return f'{self.surname}|{self.name}|{self.fathersname}|{self.organization}|{self.office_phone}|{self.personal_phone}\n'


def is_number_valid(number: str) -> bool:
    '''Checks whether phone number is valid'''

    pattern = re.compile("^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$")
    return re.match(pattern, number)


def print_info() -> None:
    '''Prints help board'''
    
    print('Phone book')
    print('Enter 1 to view the phonebook entries')
    print('Enter 2 to add entries into the phonebook')
    print('Enter 3 to edit the phonebook entries')
    print('Enter 4 to search entries into the phonebook')
    print('Enter 5 to print command again')
    print('Enter 6 to exit')


def load_data(file_name: str) -> List[Entry]:
    '''Loads data from the file'''

    phonebook: List[Entry] = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                entry:List[str] = line.strip().split('|')
                phonebook.append(
                    Entry(entry[0], entry[1], entry[4], entry[5], entry[3], entry[2])
                )
    return phonebook


def save_data(file_name: str, phonebook: List[Entry]) -> None:
    '''Saves data into the file'''
    
    with open(file_name, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(entry.get_information())


def display_entries(phonebook: List[Entry], page_size: int = 5) -> None:
    '''Display Entity object in console'''
    
    total_entries: int = len(phonebook)
    num_pages: int = (total_entries + page_size - 1) // page_size
    isStop: bool = False
    for page in range(num_pages):
        if isStop:
            break
        print('')
        start: int = page * page_size
        end: int = min(start + page_size, total_entries)
        print(f'Page {page + 1}')
        print('-' * 15)

        for i in range(start, end):
            print(f'Entry number: {i + 1}')
            print(phonebook[i])

        print('')
        command: str = input('Press enter to continue...(s/S to stop)')
        isStop = command == 'S' or command == 's'
    

def add_entry(phonebook: List[Entry]) -> None:
    '''Adds the Entry object to the list of all Entry objects and save it locally'''
    
    surname: str = input('Input surname: ')
    name: str = input('Input name: ')
    fathersname: str = input('Input fathersname: ')
    organization: str = input('Input organization: ')
    office_phone: str = input('Input office phone: ')
    while not is_number_valid(office_phone):
        office_phone = input('Input office phone again: ')
    personal_phone: str = input('Input personal phone: ')
    while not is_number_valid(personal_phone):
        personal_phone = input('Input personal phone again: ')
    phonebook.append(Entry(surname, name, office_phone, 
                           personal_phone, organization, fathersname))


def print_is_correct(entry: Entry, surname: str, name: str, fathersname: str,
          organization: str, office_phone: str, personal_phone: str) -> None:
    '''Prints a message to the console to make sure that the user has entered everything correctly'''
    
    print('-' * 15)
    print(f'surname: {surname if surname != "" else entry.surname}')
    print(f'name: {name if name != "" else entry.name}')
    print(f'fathersname: {fathersname if fathersname != "" else entry.fathersname}')
    print(f'organization: {organization if organization != "" else entry.organization}')
    print(f'office phone: {office_phone if office_phone != "" else entry.office_phone}')
    print(f'personal phone: {personal_phone if personal_phone != "" else entry.personal_phone}')
    print('-' * 15)


def edit_entry(phonebook: List[Entry]) -> bool:
    '''
    Edits an Entry object by user\'s request.
    Returns True if there\'s such Entry else False
    '''
    
    print('Edit entries')
    display_entries(phonebook, len(phonebook))
    index: int = int(input('Enter the number of entry you\'d like to edit: ')) - 1
    if 0 <= index < len(phonebook):
        print('If you would like not to change field leave it empty')
        while True:
            surname: str = input('Input surname: ')
            name: str = input('Input name: ')
            fathersname: str = input('Input fathersname: ')
            organization: str = input('Input organization: ')
            office_phone: str = input('Input job phone: ')
            personal_phone: str = input('Input phone: ')

            print_is_correct(phonebook[index], surname, name, fathersname,
                  organization, office_phone, personal_phone)
            
            is_correct: str = input('Is all correct?(Y|д|N|н)')
            if is_correct in 'YyДд':
                phonebook[index].edit(surname, name, 
                                      office_phone, personal_phone,
                                        organization, fathersname)
                print('Entry was edited')
                return True
            print('Enter information again')
    else:
        print('You\'ve entered incorrected value')
        return False

def search_entries(phonebook: List[Entry]) -> None:
    '''Searches Entry objects filtered by user\'s requests'''
    
    filters: Dict[str, Set[str]] = {'surname': set(), 
                'name': set(), 
                'fathersname': set(),
                'organization': set(),
                'office_phone': set(),
                'personal_phone': set()}
    for key in filters:
        filter_by_key: Set[str] = set(map(str.casefold ,input(f'Enter keywords separated by space for filter {key}: ').split()))
        filters[key] = filter_by_key | filters[key] 
    results: List[Entry] = phonebook.copy()
    for key, value in filters.items():
        if value and len(value) != 0:
            results: List[Entry] = list(filter(lambda x: x.__dict__[key].casefold() in value, results))
    print('\nHere what was found:\n' + 15 * '-')
    for result in results:
        print(result)


def main() -> None:
    '''Main function. Start of the program.'''
    
    file_name = input('Input the name of the file you\'d like to use as phone book, or leave it empty to use standard(phonebook.txt)')
    if file_name == '':
        file_name = FILE_NAME
    if file_name[-4:] != '.txt':
        file_name += '.txt'
    phonebook: List[Entry] = load_data(file_name)
    print_info()
    while True:
        try:
            choice: int = int(input('Enter the command: '))
        except:
            print('Incorrect command. Try again.')
            continue
        match choice:
            case 1:
                try:
                    page_size = int(input(
                        'Input the size of the page, amount of entries you would like to see on 1 page: '))
                except:
                    print('Incorrect page size.')
                    continue
                display_entries(phonebook, page_size)
            case 2:
                add_entry(phonebook)
                save_data(file_name, phonebook)
                print('Entry was added')
            case 3:
                if edit_entry(phonebook):
                    save_data(file_name, phonebook)
            case 4:
                search_entries(phonebook)
            case 5:
                print_info()
            case 6:
                save_data(file_name, phonebook)
                print('Goodbye')
                break
            case _:
                print('No such command')


if __name__ == '__main__':
    main()