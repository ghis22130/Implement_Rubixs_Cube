# 단계별 루빅스 큐브 구현하기

## 🚀 문제 개요

- 3단계 걸쳐 루빅스 큐브를 구현한다.
- 구현 언어는 python을 이용한다. 

***
## 1단계 : 단어 밀어내기 구현하기
1. 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
2. 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
3. 밀려나간 단어는 반대쪽으로 채워진다.

### 코드 설명
```push(msg)``` 함수는 사용자의 입력을 단어, 밀어낼 수, 방향으로 분해하고 각 요구사항에 맞는 연산을 수행한다.

```word```는 apple, carrot 과 같은 입력문자열 맨 앞 단어를 저장한다.

```size```는 얼마나 이동시킬것인가에 대한 입력문자열 중간 정수형 숫자를 저장한다.

```direction```은 왼쪽과 오른쪽 중에 어느 방향으로 이동시킬것인가에 대한 입력문자열 맨 마지막 문자를 저장한다.

main에서 "Q" 혹은 "q" 입력시 "bye~"를 출력 후 while문을 탈출하고 실행 종료 시키도록 한다.
 
## 실행 코드
```python
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
```