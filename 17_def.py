######################## def 함수 정의 ########################

def add(a,b):
    print(f'{a}와 {b}를 입력받았습니다')
    print(f'두 값을 더하면 {a+b} 입니다')

    return a+b
add(5,6)

add(99,1)

# return값이 없으면 None으로 나옴. 그래서 함수에선 꼭 return 값을 지정해주어야 함.
temp = add(123,456)

print(temp)