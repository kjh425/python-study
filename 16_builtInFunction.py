######################## Built in func ########################

# 입력함수 input
name = input("이름을 입력하시오 : ")
print(name)

array = [1,2,3,4,5]
# 최대값 max
print(max(array))
# 최솟값 min
print(min(array))

ABCArray  = ['a','A','B','z','Z']
# 최대값 max(문자열도 가능)
print(max(ABCArray))
# 최솟값 min(문자열도 가능)
print(min(ABCArray))

numArray = [23,86,334,-12,521221]
# sorted = 오름차순
print(sorted(numArray))
# sorted(,reverse=True) = 내림차순
print(sorted(numArray,reverse=True))

# range로 list에 담기
temp = list(range(1,11))
print(temp)


