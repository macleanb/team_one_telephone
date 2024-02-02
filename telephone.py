

whiskey_contacts = {
    "Andrew": "928-580-9077",
    "New Person": "123-456-7890",
    "Another Phone": "555-555-5555"
}


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
    return whiskey_contacts.keys


# print(delete_contact('natalie'))
print(get_list_of_contacts())
# print(whiskey_contacts)
