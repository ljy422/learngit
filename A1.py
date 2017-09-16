print("Li Jingyu 15398663")

class Book():

    def __init__(self,author,title):
        self.title = title
        self.author = author
    def show(self):
        print('The title is',self.title)
        print('The author is',self.author)

class Library():

    def __init__(self,library_name):
        self.library_name = library_name
        self.list = []

    def add(self,title,author):
        self.list.append(Book(author,title))

    def print(self):
        print(self.library_name)
        for i in self.list:
           print('TITLE:',i.title,'AUTHOR:',i.author)



    def search(self,title_word = None, author_term = None):

        if title_word == None and author_term == None:
            print('At least one of title_word and author_term must be provided.')

        elif title_word == None:
            for i in self.list:
                if author_term in i.author:
                   i.show()
        elif author_term == None:
            for i in self.list:
                if title_word in i.title:
                    i.show()
        else:
            for i in self.list:
                if title_word in i.title and author_term in i.author:
                    i.show()


L1 = Library('Fiction')
L2 = Library('Science')
L1.add('Pride and Prejudice','Jane Austen')
L1.add('A Study in Scarlet','Arthur Conan Doyle')
L1.add('The Lost World','Arthur Conan Doyle')
L1.print()
L1.search(title_word='pre')
L2.add('Souvenirs Entomologiques','Jean-Henri Casimir Fabre')
L2.add('The Origin of Species','Charles Robert Darwin')
L2.add('Philosophiae Naturalis Principia Mathematica','Isaac Newton')
L2.print()
L2.search(title_word='es')