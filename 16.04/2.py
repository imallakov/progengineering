import sys


def sum_arguments():
    if len(sys.argv) == 1:
        print("NO PARAMS")
        return ""

    try:
        num = 1
        sum = 0
        for arg in sys.argv[1:]:
            sum += num * int(arg)
            num *= -1
        return sum
    except Exception as error:
        return error.__class__.__name__


result = sum_arguments()
print(result)
