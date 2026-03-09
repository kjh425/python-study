######################## 리스트 ########################
food = []
print(type(food))

food = ['한식',"중식","양식"]
print(food)

food.append('일식')
print(food)
print(len(food))

food2 = ['기괴식']
food3 = food+food2
print(food3)

food3.insert(5,'냠냠')
print(food3)

food3.remove('기괴식')
print(food3)

print(food3.count('한식'))
print(food3.index('한식'))
print(food3.sort(reverse=False)) # 오름차순
print(food3)

