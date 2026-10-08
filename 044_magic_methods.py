# Magic methods = Dunder methods ( __init__ , __str__ , __eq__ , __gt__ )
#                   they are automatically called by python's built-in operations
#                   they allow developer to define or customise the behaviour of objects

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
# __init__ is called automatically behind the scenes when we create an object of the class.

    # we can print an string representation of the object when we print directly
    def __str__(self):
        return f"'{self.title}' by {self.author} of pages - {self.pages}"
    # this method helps to print the object in a readable format instead of the default memory address

    # for checking if two objects are equal
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # when we use < or > for comparing we get error in __eq__, so here is a way
    def __lt__(self, other): #(lt - less than)
        return self.pages < other.pages

    def __gt__(self, other): #(gt - greater than)
        return self.pages > other.pages

    # when we try to add pages of two books we get error, so we can define a method for that
    def __add__(self, other):
        return self.pages + other.pages

    # when we search for a keyword in the object we get error, so
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # if we want to get value of a key, it gives error, so we can define a method for that
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f" Key '{key}' not found in the object"
        
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter", "J.K Rowling", 223)
book3 = Book("The Lion", "C.S. lewis", 172)
book4 = Book("The Lion", "C.S. lewis", 172)

print(book3 == book4) # True
print(book2 < book1) # True
print(book1 > book2) # True
print(book3 + book4) # 395
print("Hobbit" in book1) # True
print(book3["title"]) # The Lion