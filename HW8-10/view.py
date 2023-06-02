import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contact(pb: list[dict[str, str]], error_msg: str):
    if pb:
        print('\n' + '=' * 66)
        for i, contact in enumerate(pb, 1):
            if contact:
                print(f'{i:>3}.{contact.get("name"):<20}| {contact.get("phone"):<20}| {contact.get("comment"):<20}')
            else:
                print_message(error_msg)
        print('=' * 66 + '\n')
    else:
        print_message(error_msg)


def input_contact(message: str, cancel_msg: str) -> dict:
    contact = {}
    print(message)
    for key, val in text.input_contact.items():
        data = input(val)
        if data:
            contact[key] = data
        else:
            contact[key] = "no"
            print_message(cancel_msg)
    return contact


def input_index(message: str, pb: list, error: str):
    print_contact(pb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(pb) + 1:
            return int(index)


def del_contact(name: str):
    return f'Контакт {name} успешно удален!'


def input_search(message: str):
    return input(message)



def print_search(cont: dict):
    print(f'''Найден контакт: 
{cont.get("name")} | {cont.get("phone")} | {cont.get("comment")}''')


def print_search2(cont: list):
    print("Найдены совпадения:")
    for n, i in enumerate(cont, 1):
        print(f'{n}) {i}')
