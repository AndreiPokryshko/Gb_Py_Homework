import text
import view, model


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_saccessful)
            case 3:
                # view.print_contact(model.phone_book, text.error_msg)
                pb = model.get_pb()
                view.print_contact(pb, text.error_msg)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_msg)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                pb = model.get_pb()
                search_txt = view.input_search(text.search_text)
                if search_txt:
                    # res_search = model.search_text(search_txt, pb)
                    res_search = model.search(search_txt, pb)
                    # view.print_search(res_search)
                    view.print_search2(res_search)
                else:
                    view.print_message(text.cancel_msg)
            case 6:
                pb = model.get_pb()
                id_c = view.input_index(text.change_cont, pb, text.error_msg)
                contact = view.input_contact(text.new_contact, text.cancel_msg)
                model.change_contact(contact, id_c)

            case 7:
                pb = model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.error_msg)
                name = model.del_contact(index)
                view.print_message(name)

            case 8:
                break
