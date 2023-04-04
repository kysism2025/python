class Address:
    def __init__(self, city, gu):
        self.city = city
        self.gu = gu
        
class Person(Address):
    def __init__(self, email, city, gu):
        super().__init__(city, gu)
        self.email = email

class Contact(Person):
    def __init__(self, name, email, city, gu):
        super().__init__(email, city, gu)
        self.name = name

    def __str__(self):
        return f"\n이름:{self.name}\
                \n이메일:{self.email}\
                \n도시:{self.city}\
                \n구:{self.gu}"

c = Contact("kim","kim@gmail.com","jongro","seoul")
print(c)