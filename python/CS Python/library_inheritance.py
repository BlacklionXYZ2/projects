class item:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe(self):
        print(f'{self.title} - {self.year}')

class book(item):
    def __init__(self, author, title, year):
        super().__init__(title, year)
        self.author = author

    def describe(self):
        print(f'{self.title} - {self.author} - {self.year}')

class dvd(item):
    def __init__(self, duration, title, year):
        super().__init__(title, year)
        self.duration = duration

    def describe(self):
        print(f'{self.title} - {self.year} - {self.duration}')

