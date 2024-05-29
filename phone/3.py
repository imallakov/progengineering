def check_phone(phone):
    try:
        phone = "".join(phone.split())
        if phone.find("+7") != 0 and phone.find("8") != 0:
            raise Exception("неверный формат")
        if not all(phone.split("-")):
            raise Exception("неверный формат")
        else:
            phone = phone.replace("-", "")
        start_bt = phone.find("(")
        end_bt = phone.find(")")
        if start_bt > -1:
            if end_bt < start_bt or not phone[start_bt + 1:end_bt].isdigit() \
                    or not phone.count("(") == 1 or not phone.count(")") == 1:
                raise Exception("неверный формат")
        else:
            if end_bt > -1:
                raise Exception("неверный формат")
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        if phone.find("8") == 0:
            phone = "+7" + phone[1:]

        if not phone[1:].isdigit():
            raise Exception("неверный формат")
        if not len(phone[1:]) == 11:
            raise Exception("неверное количество цифр")

        return phone
    except Exception as error:
        return error


print(check_phone(input()))
