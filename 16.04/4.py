import sys


def sum_arguments():
    if len(sys.argv) == 1:
        print("NO PARAMS")

    try:
        spisok: dict = {}
        sorting: bool = False

        for arg in sys.argv[1:]:
            if arg == '--sort':
                sorting = True
            else:
                key, value = arg.split('=')
                spisok[key] = value

        if sorting:
            sorted_spisok = dict(sorted(spisok.items(), key=lambda x: x[1]))
            spisok = sorted_spisok

        for key, value in spisok.items():
            print(key, "=", value)

    except Exception as error:
        print(error.__class__.__name__)


sum_arguments()
