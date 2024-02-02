""" This modeul simulates a telephone """

# External Imports
import re
from rich.console import Console
from rich.style import Style
from rich import print

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


def manage_contacts():
    """ This function simulates a contacts menu """
    user_selection = "<>"

    while int(user_selection) < 1 and user_selection > 6:
        user_selection = get_user_menu_choice()
        print(f'The user entered option {user_selection}')

        match user_selection:
            case "1":
                place_call()
            case "2":
                #Team2.manage_contacts()
                pass
            case "3":
                #Team3.search_internet()
                pass
            case "4":
                #Team4.manage_tasks()
                pass
            case _:
                pass



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
                manage_contacts()
                pass
            case "3":
                #Team3.search_internet()
                pass
            case "4":
                #Team4.manage_tasks()
                pass
            case _:
                pass

    print('Thanks for using the telephone!  Goodbye!')

display_menu()