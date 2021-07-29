#random.py

import random

for i in range(1, 11): #최대 10번 시행횟수

    a = random.randrange(0,9)

    while True:
        b = random.randrange(0,9)
        if b != a:
            break #0과 9사이의 값이면서 a와 곂치면 안됌
    
    while True:
        c = random.randrange(0,9)
        if c != a and c!= b:
            break
    
    while True:
        d = random.randrange(0,9)
        if d != a and d != b and d != c:
            break
    
    print(a,b,c,d)

    
# 정답 값 랜덤 선택 과정

    
    while True:
        x = int(input("첫번째 값을 입력하세요"))
        if x >= 0 and x <= 9:
            break #x는 0에서 9사이 한자리 정수
    
    while True:
        y = int(input("두번째 값을 입력하세요"))
        if y >= 0 and y <= 9 and x != y:
            break
    
    while True:
        z = int(input("세번째 값을 입력하세요"))
        if z >= 0 and z <= 9 and z != x and z!=y:
            break
    
    while True:
        w = int(input("네번재 값을 입력하세요"))
        if w >= 0 and w <= 9 and w != y and w!=x and w!=z:
            break

#사용자 값, 알맞은 값 입력때까지 반복

    print (x,y,z,w)

    strike = 0
    ball = 0

    if a==x:
        strike +=1 # 정답과 사용자 입력값, 자릿수가 같으면 스트라이크
    elif a==y or a==z or a==w:
        ball+=1 # 그외 상황은 전부 볼

    if b==y:
        strike+=1
    elif b==x or b==z or b==w:
        ball+=1


    if c==z:
        strike+=1
    elif c==x or c==y or c==w:
        ball+=1

    if d==w:
        strike+=1
    elif d==x or d==y or d==z:
        ball+=1

    if strike == 4:
        print(strike,"스트라이크! ","정답입니다")
        break
    else:
        print(i,"번째 도전입니다.", strike, "스트라이크",ball,"볼입니다. 다시 도전하세요\n")
        
#스트라이크와 볼 카운트 및 출력
        
print("게임 끝")
#게임 

