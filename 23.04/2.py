def is_palindrome(data):
    return data == data[::-1]


def main():
    data = input("Enter the word: ")
    if is_palindrome(data):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
