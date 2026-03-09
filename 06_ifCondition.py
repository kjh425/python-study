######################## 조건문 ########################
today = '월요일'

if today == '일요일':
    print('쉰다')
elif today == '월요일':
    print('출근이네..')
else :
    print('그럼 무슨요일이냐?')


today = 9
if today >= 5 :
    print('월급은 이미 들어왔따..')
elif today < 5 :
    print('월급 기대한다잉~')

pizza = True
burger = False

if pizza:
    # 피자가 true일때 실행
    print('야호 피자당~')
else: print('버거도 나쁘진 않지')

if not pizza:
    # 피자가 false일때 실행
    print('야호 피자당~')
else: print('버거도 나쁘진 않지')
