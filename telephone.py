""" This modeul simulates a telephone """

# External Imports
import re
from rich.console import Console
from rich.style import Style
from rich import print

# Define constants
whiskey_contacts = {
    "Andrew": "928-580-9077",
    "New Person": "123-456-7890",
    "Another Phone": "555-555-5555"
}

def get_user_menu_choice():
    """ Gets a menu choice from the user """
    # Link to emoji codes: https://github.com/Textualize/rich/blob/master/rich/_emoji_codes.py
    regex = '[1-5]'
    console = Console()
    base_style = Style.parse("cyan")

    valid_input = False
    while not valid_input:
        print()
        console.print(
            ":mobile_phone:----  TELEPHONE APP ----:mobile_phone:",
            style = base_style + Style(underline=False)
            )
        print()
        print("[bold magenta]Options:[/bold magenta]")
        print('1.  Make a Call')
        print('2.  Manage Contacts')
        print('3.  Search the Internet')
        print('4.  Manage Tasks')
        print('5.  Quit')
        user_input = input('Please enter a menu option (1-5):  ')
        valid_input = bool(re.fullmatch(regex, user_input))

    return user_input


def get_user_contact_menu_choice():
    """ Gets a menu choice from the user """
    # Link to emoji codes: https://github.com/Textualize/rich/blob/master/rich/_emoji_codes.py
    regex = '[1-7]'
    console = Console()
    base_style = Style.parse("cyan")

    valid_input = False
    while not valid_input:
        print()
        console.print(
            ":mobile_phone:----  CONTACTS ----:mobile_phone:",
            style = base_style + Style(underline=False)
            )
        print()
        print("[bold magenta]Options:[/bold magenta]")
        print('1.  Add Contact')
        print('2.  Update Number')
        print('3.  Update Name')
        print('4.  Lookup Number')
        print('5.  Delete Contact')
        print('6   Display All Contacts')
        print('7.  Exit Contact Manager')
        user_input = input('Please enter a menu option (1-7):  ')
        valid_input = bool(re.fullmatch(regex, user_input))

    return user_input

def display_menu():
    """ This function simulates a telephone menu """
    user_selection = "<>"

    while user_selection != '5':
        user_selection = get_user_menu_choice()
        print(f'The user entered option {user_selection}')

        match user_selection:
            case "1":
                place_call()
            case "2":
                display_contacts_menu()
            case "3":
                #Team3.search_internet()
                pass
            case "4":
                #Team4.manage_tasks()
                pass
            case _:
                pass

    print('Thanks for using the telephone!  Goodbye!')


def display_contacts_menu():
    """ This function simulates a contacts menu """
    user_selection = -1

    print('here in display contacts menu')
    while int(user_selection) != 7:
        user_selection = get_user_contact_menu_choice()
        print(f'The user entered option {user_selection}')

        match user_selection:
            case "1":
                info = get_contact()
                add_contact(info[0], info[1])
                print(f'Added new contact: {info[0]}: {info[1]}')
            case "2":
                name = get_user_name()
                number = get_user_phone_number()
                result = update_number(name, number)
                if result is not None:
                    print(result) # prints any errors
                else:
                    print(f'Contact updated: {name}: {whiskey_contacts[name]}')
            case "3":
                current_name = get_user_name()
                new_name = get_user_name()
                result = update_name(current_name, new_name)

                if result is not None:
                    print(result) # prints any errors
                else:
                    print(f'Contact updated: {new_name}: {whiskey_contacts[new_name]}')
            case "4":
                name = get_user_name()
                result = get_number(name)
                print()
                print(result)
            case "5":
                name = get_user_name()
                result = delete_contact(name)

                if result is not None:
                    print(result) # prints any errors
                else:
                    print(f'Contact deleted: {name}')
            case "6":
                contacts = get_list_of_contacts()
                print()
                print('List of Contacts:')
                for contact in contacts:
                    print(contact)
            case _:
                pass


def get_user_name():
    """ Gets a user name"""
    regex = '[A-Za-z]{2,}'

    valid_input = False
    while not valid_input:
        user_input = input('Please enter a user name:  ')
        valid_input = bool(re.fullmatch(regex, user_input))
        if not valid_input:
            print('[bold red]Please enter only A-Z, at least two letters[/bold red]')

    return user_input


def get_user_phone_number():
    """ Gets a 10-digit phone number from the user"""
    regex = '[0-9]{10}'

    valid_input = False
    while not valid_input:
        user_input = input('Please enter a phone number:  ')
        valid_input = bool(re.fullmatch(regex, user_input))
        if not valid_input:
            print('[bold red]Please enter 10 digits[/bold red]')

    return user_input


def place_call():
    """ Simulates placing a call """
    number = get_user_phone_number()
    print(f'[bold pink]Calling {number}...[/bold pink]\n')


def get_contact():
    name = get_user_name()
    number = get_user_phone_number()
    return [name, number]

def add_contact(name, phone_number):
    whiskey_contacts[name] = phone_number


def update_number(name, number):
    if name in whiskey_contacts:
        whiskey_contacts[name] = number
    else:
        return "Contact Not Found"


def update_name(current_contact_name, updated_name):
    if current_contact_name in whiskey_contacts:
        whiskey_contacts[updated_name] = whiskey_contacts[current_contact_name]
        delete_contact(current_contact_name)
    else:
        return "Contact Not Found"

def get_number(name):
    if name in whiskey_contacts:
        return f"{name}'s phone number is {whiskey_contacts[name]}"
    else:
        return "Contact Not Found"

def delete_contact(name):
    if name in whiskey_contacts:
        del whiskey_contacts[name]
    else:
        return 'Contact not found'

def get_list_of_contacts():
    # print(whiskey_contacts)
    return whiskey_contacts.keys()


display_menu()
