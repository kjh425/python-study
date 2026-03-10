######################## 라이브러리 모듈 ########################
import time

print(1)
# 2초 지연
time.sleep(2)
print(2)

for i in range(1,11):
    # 1초씩 카운트세면서 10까지
    print(i)
    time.sleep(1)

import random
# 랜덤함수
x = random.random()
# 범위지정 랜덤함수
y = random.randint(1,10)
print(x)
print(y)

x = [1,2,3,4,5]
# 배열 내 랜덤 선택
y = random.choice(x)
# 배열 내 2개 랜덤선택
z = random.sample(x,2)
# 배열 내 요소 랜덤배열
random.shuffle(x)

print(x)
print(y)
print(z)

import datetime
# 오늘 날짜 출력
today = datetime.date.today()

print(today)

