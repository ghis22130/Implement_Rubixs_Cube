#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def push(msg):
    word, size, direction = msg.split() #입력받은 문자열을 단어, 밀어낼 수, 방향으로 나누어 저장한다.
    answer = "" #반환할 단어
    
    for idx, i in enumerate (word):
        if direction == "R" or direction == "r":
            answer += word[(idx-int(size))%len(word)] #%연산자를 이용하여 오른쪽으로 밀어준다.
        elif direction == "L" or direction == "l" :
            answer += word[(idx+int(size))%len(word)]  #%연산자를 이용하여 왼쪽으로 밀어준다.
        
    return answer

while(True):
    message = input("> ")
    if message == "Q" or message == "q" : #Q 혹은 q 입력시 실행 종료
        print("bye~ ")
        break
    print(push(message))
