######################## 딕셔너리 ########################
# 딕셔너리는 중괄호로 시작하며, 말 그대로 사전처럼 생긴 자료형임
user = {'name' : '김준한','job' : '개발자' , 'age' : 30}

print(user)
print(user['name'])
print(user['job'])
print(user['age'])

user['age'] = 20

print('20대로 돌아가고 싶다. 돌아가지니?')
print(str(user['age'])+ '대로 돌아갔다!')

del user['name']
print(user)

keys_list = user.keys()
print(keys_list)
print(type(keys_list))

# 오류 - 리스트 형식처럼 보이지만? 리스트는 아님. 그래서 형변환을 통해 바꿔주어야함.
# print(keys_list[0])

keys_list = list(keys_list)
print(type(keys_list))
print(keys_list[0])

items_list = user.items()

print(type(items_list))
items_list = list(items_list)
print(type(items_list))
print(items_list[0])
print(items_list[1])
