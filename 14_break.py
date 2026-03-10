######################## break문과 continue ########################
count = 1

while True:
    print(f'{count} 바퀴째')
    count += 1
    if count == 19:
        print(f'좀 쉬쟈... 힘드렁..')
        continue
    if count == 21:
        break
print(f'달리기 끝~~')

for i in range(0,10):
    if i == 3:
        break
    print(i)

for i in range(0,10):
    if i == 3:
        continue
    print(i)
