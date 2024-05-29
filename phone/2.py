def check_phone(phone):
    try:
        phone = "".join(phone.split())
        if phone.find("+7") != 0 and phone.find("8") != 0:
            raise ValueError
        if not all(phone.split("-")):
            raise ValueError
        else:
            phone = phone.replace("-", "")
        start_bt = phone.find("(")
        end_bt = phone.find(")")
        if start_bt > -1:
            if end_bt < start_bt or not phone[start_bt + 1:end_bt].isdigit() \
                    or not phone.count("(") == 1 or not phone.count(")") == 1:
                raise ValueError
        else:
            if end_bt > -1:
                raise ValueError
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        if phone.find("8") == 0:
            phone = "+7" + phone[1:]

        if not phone[1:].isdigit() or not len(phone[1:]) == 11:
            raise TypeError
        return phone
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"


print(check_phone(input()))
