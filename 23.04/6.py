import string


def strip_punctuation_ru(data):
    # Remove punctuation from the string
    data = data.translate(str.maketrans('', '', string.punctuation))
    # Remove multiple spaces
    data = ' '.join(data.split())
    # Return the result
    return data


def main():
    sentence = input('Input the sentence:')
    print(strip_punctuation_ru(sentence))


main()
