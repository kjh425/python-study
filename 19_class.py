######################## 클래스 class ########################

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def hello(self):
        print(f'Hello~~ my name is {self.name} and my age is {self.age}')

user_1 = User('주나니',30)
user_2 = User('나니나니','미상')

user_1.hello()
print('============')
user_2.hello()

