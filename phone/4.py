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

        mts_codes = list(range(910, 920)) + list(range(980, 990))
        megafon_codes = range(920, 940)
        bilain_codes = list(range(902, 907)) + list(range(960, 970))

        phone_codes = [mts_codes, megafon_codes, bilain_codes]

        code = int(phone[2:5])
        code_found = False
        for phone_code in phone_codes:
            if code in phone_code:
                code_found = True

        if not code_found:
            raise Exception("не определяется оператор сотовой связи")

        return phone
    except Exception as error:
        return error


print(check_phone(input()))
