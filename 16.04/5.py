import sys


def main():
    file_name = ""
    sorting = False
    count = False
    num = False
    for arg in sys.argv[1:]:
        if arg == '--sort':
            sorting = True
        elif arg == '--num':
            num = True
        elif arg == '--count':
            count = True
        else:
            file_name = arg

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"ERROR")
        sys.exit(1)

    if sorting:
        lines = sorted(lines)

    if num:
        for i, line in enumerate(lines, 0):
            print(f"{i} {line}", end="")
            if not line[-1] == '\n':
                print()
    else:
        for line in lines:
            print(line, end="")

    if count:
        print(f"\nКоличество строк: {len(lines)}")


if __name__ == "__main__":
    main()
