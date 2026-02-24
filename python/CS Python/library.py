import time
i = -1
class book:
    def __init__(self, title, author, borrowed, borrowed_by):
        global i
        i += 1
        x = i
        if len(str(i)) < 2:
            x = f'0{i}'

        print(time.time())

        self.__title = title
        self.__author = author
        self.__borrowed = borrowed
        self.__borrowed_by = borrowed_by
        self.__date_borrowed = time.time()
        self.__code = list(library.hash([author, title], is_book = False))

        temp = 'a'
        for s in self.__code:
            temp += str(s)
        temp = temp[1:] + x
        self.__code = temp
    
    def borrowed(self):
        self.__borrowed = True

    def returned(self):
        self.__borrowed = False

    def get_attributes(self):
        return {'title': self.__title, 'author': self.__author, 'borrowed': self.__borrowed, 'borrowed_by': self.__borrowed_by, 'code': self.__code}
    
    def set_attribute(self, attr, value):
        eval(f'self.__{attr} = {value}')

    def time_since_borrowed(self):
        print(time.time(), self.__date_borrowed) # fix time, all values are different for some reason and everything happens within about 1/20 of a secod so the values are basically useless
        return time.time() - self.__date_borrowed

class library:
    def __init__(self):
        self.__books_organised = [[[] for _ in range(50)] for _ in range(50)]
        self.__available_books = 'a'

    def hash(data, is_book = True):
        value1 = 0
        value2 = 0
        if is_book:
            value1 = sum(ord(char) for char in data.get_attributes()['author']) % 50
            value2 = sum(ord(char) for char in data.get_attributes()['title']) % 50
        else:
            value1 = sum(ord(char) for char in data[0]) % 50
            value2 = sum(ord(char) for char in data[1]) % 50
        return value1, value2

    def update_available(self):
        last_author = None
        self.__available_books = 'a'
        for x in self.__books_organised:
            for y in x:
                try:
                    if last_author != y[0].get_attributes()['author']:
                        self.__available_books += '\n'
                        self.__available_books += f'{y[0].get_attributes()['author']}\n'
                    last_author = y[0].get_attributes()['author']
                    self.__available_books += f'     {y[0].get_attributes()['title']} - {y[0].get_attributes()['code']}{f' - borrowed by {y[0].get_attributes()['borrowed_by']}' if y[0].get_attributes()['borrowed'] else ''}\n'
                except IndexError:
                    pass
        self.__available_books = self.__available_books[1:]

    def list_available(self):
        print(self.__available_books)

    def is_available(self, book):
        idx1, idx2 = library.hash(book)
        for x in self.__books_organised[idx1][idx2]:
            if x.get_attributes()['borrowed']:
                pass
            else:
                print(f'Available: {book.get_attributes()['code']}')

    def add_book(self, book):
        if type(book) == list:
            for x in book:
                idx1, idx2 = library.hash(x)
                self.__books_organised[idx1][idx2].append(x)
        else:
            idx1, idx2 = library.hash(book)
            self.__books_organised[idx1][idx2].append(book)
        self.update_available()

    def remove_book(self, data):
        idx1, idx2 = library.hash([data[0], data[1]], is_book = False)
        for x in self.__books_organised[idx1][idx2]:
            if x.get_attributes()['code'] == data[2]:
                self.__books_organised.remove(x)
        self.update_available()

    def borrowed_time(self, book):
        if type(book) == list:
            idx1, idx2 = library.hash([book[0], book[1]], is_book = False)
            for x in self.__books_organised[idx1][idx2]:
                if x.get_attribute()['code'] == book[2]:
                    return x.time_since_borrowed()
        else:
            idx1, idx2 = library.hash(book)
            for x in self.__books_organised[idx1][idx2]:
                if x.get_attribute()['code'] == book.getattribute()['code']:
                    return x.time_since_borrowed()

books = [book('The Hunt', 'Gareth Coker', False, None), 
         book('Discovery Of Gravity', 'Isaac Newton', True, 'Harry Foxon')
         ]
library1 = library()
library1.add_book(books)
library1.add_book(book('Fairytale Wonderland', 'Gareth Coker', False, None))
#library1.remove_book([books[0].title, books[0].author, books[0].code])
library1.list_available()
print(library1.borrowed_time(['Discovery Of Gravity', 'Isaac Newton', '483901']))