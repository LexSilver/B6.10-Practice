#B6.10. Workshop
#Assignment 6.10.1

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def rect_str(self):
        return 'Rectangle (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.width) + ', ' + str(self.height) + ')'

a = Rectangle(5, 10, 50, 100)

print(a.rect_str())
print(type(a.rect_str()))

# Assignment 6.10.2

class Rectangle:
    def __init__(self, width, leight):
        self.width = width
        self.leight = leight

    def rect_discribe(self):
        print('Ширина ', self.width)
        print('Высота ', self.leight)


rect1 = Rectangle(10, 5)
rect1.rect_discribe()

# Assignment 6.10.3

class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        if isinstance(self.balance, int) and self.balance >= 0:
            return self.balance

    def display_client(self):
        print(f'Клиент "{self.name}". Баланс: {self.balance} руб.')

client1 = Client('Петя Иванов', 50)

client1.display_client()

# Assignment 6.10.4

class Volunteer:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

class Guest(Volunteer):
    def __init__(self, name, city, status, hotel_nights=2):
        super().__init__(name, city, status)
        self.hotel_nights = hotel_nights

    def add_to_list(self, g_list):
        return g_list.append(f'{self.name}, г.{self.city}, статус "{self.status}"')

    def display_guest(self):
        print(f'{self.name}, г.{self.city}, статус "{self.status}"')

guests_list = []
guest1 = Guest('Иван Петров', 'Москва', 'Наставник')
guest2 = Guest('Андрей Кузнецов', 'Рязань', 'Лидер')
guest1.add_to_list(guests_list)
guest2.add_to_list(guests_list)
guest1.display_guest()
print(guests_list)