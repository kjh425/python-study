######################## for문과 dictionary ########################
user_data = {
    "name" : '준한',
    'age' : 30,
    'job' : '개발자'
}

print(f'{user_data}')

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

for data in user_data:
    # print(data)
    print(f'{data} : {user_data[data]}')

print('================================================')

for data in user_data.items():
    print(data)

# for문과 dictionary를 사용할때는 여러가지 방법들이 있다. 잘 선택해서 사용하도록 하자.

