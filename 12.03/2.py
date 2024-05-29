class LeftParagraph:
    def __init__(self, num):
        self.size = num
        self.words: list[str] = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        temp = self.size
        for word in self.words:
            if not temp == self.size:
                print(' ', end='')
                temp -= 1
            if len(word) <= temp:
                print(word, end='')
                temp -= len(word)
            else:
                print()
                temp = self.size
                print(word, end='')
                temp -= len(word)


class RightParagraph:
    def __init__(self, num):
        self.size = num
        self.words: list[str] = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        temp = self.size
        tempstr: str = ""
        for word in self.words:
            if not temp == self.size:
                tempstr += " "
                temp -= 1
            if len(word) <= temp:
                tempstr += word
                temp -= len(word)
            else:
                print(' ' * (self.size - len(tempstr)), tempstr)
                temp = self.size
                tempstr = word
                temp -= len(word)
        print(' ' * (self.size - len(tempstr)), tempstr)


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()
