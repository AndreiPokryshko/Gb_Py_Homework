phone_book: list[dict[str, str]] = []

path = 'phone.txt'


def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        print(data)
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})


def save_pb():
    global phone_book, path
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book


def add_contact(contact: dict[str, str]):
    global phone_book
    if contact:
        phone_book.append(contact)
    return contact.get('name')


def del_contact(index: int):
    return phone_book.pop(index - 1).get('name')  # возвращает имя


def change_contact(new_dict: dict, index: int):
    global phone_book
    cont_id = index - 1
    old_cont = {}
    old_cont = phone_book[cont_id]
    for key in new_dict.keys():
        if new_dict.get(key) == 'no':
            new_dict[key] = old_cont.get(key)
    phone_book[cont_id] = new_dict


def search_text(text: str, pb):
    global phone_book
    for contact in phone_book:
        id_ = phone_book.index(contact)
        for val in contact.values():
            if text.lower() in val.lower():
                return phone_book[id_]


def search(text: str, pb) -> list[dict[str, str]]:
    global phone_book
    list_ = []
    for contact in phone_book:
        id_ = phone_book.index(contact)
        for val in contact.values():
            if text.lower() in val.lower():
                list_.append(phone_book[id_])
    return list_
