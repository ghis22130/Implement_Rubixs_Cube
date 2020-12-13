# 단계별 루빅스 큐브 구현하기

## 문제 개요

- 3단계 걸쳐 루빅스 큐브를 구현한다.
- 구현 언어는 python을 이용한다. 

***
## 1단계 : 단어 밀어내기 구현하기

### 문제 개요
1. 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
2. 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
3. 밀려나간 단어는 반대쪽으로 채워진다.

### 코드 설명
`push(msg)` 함수는 사용자의 입력을 단어, 밀어낼 수, 방향으로 분해하고 각 요구사항에 맞는 연산을 수행한다.

`word`는 apple, carrot 과 같은 입력문자열 맨 앞 단어를 저장한다.

`size`는 얼마나 이동시킬것인가에 대한 입력문자열 중간 정수형 숫자를 저장한다.

`direction`은 왼쪽과 오른쪽 중에 어느 방향으로 이동시킬것인가에 대한 입력문자열 맨 마지막 문자를 저장한다.

main에서 "Q" 혹은 "q" 입력시 "bye~"를 출력 후 while문을 탈출하고 실행 종료 시키도록 한다.
 
### 실행 코드
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
***
## 2단계 : 평면 큐브 구현하기
### 문제 개요
3 X 3의 2차원 배열이 아래처럼 있다.
```
R R W
G C W
G B B
```
사용자 입력을 받아서 아래의 동작을 하는 프로그램을 구현하시오
```
> U  가장 윗줄을 왼쪽으로 한 칸 밀기 RRW -> RWR
> U' 가장 윗줄을 오른쪽으로 한 칸 밀기 RRW -> WRR
> R  가장 오른쪽 줄을 위로 한 칸 밀기 WWB -> WBW
> R' 가장 오른쪽 줄을 아래로 한 칸 밀기 WWB -> BWW
> L  가장 왼쪽 줄을 아래로 한 칸 밀기 RGG -> GRG (L의 경우 R과 방향이 반대임을 주의한다.)
> L' 가장 왼쪽 줄을 위로 한 칸 밀기 RGG -> GGR
> B  가장 아랫줄을 오른쪽으로 한 칸 밀기 GBB -> BGB (B의 경우도 U와 방향이 반대임을 주의한다.)
> B' 가장 아랫줄을 왼쪽으로 한 칸 밀기 GBB -> BBG
> Q  Bye~를 출력하고 프로그램을 종료한다.
```

### 코드 설명
python에서는 `copy`라이브러리의 `deepcopy()`를 하지 않으면 2중 배열이 얕은 참조가 발생하여 큐브 변환에 어려움을 겪었습니다.

`Cube`클래스를 작성하였고 이 클래스는 생성시 초기 셋팅이 이루어지고 사용자의 입력을 받은 값에 따라 변환 할 수 있는 `enter*()` 메소드들을 가지고 있습니다.

프로그램 실행시 현재 큐브의 상태를 출력하며 사용자는 U,U',R,R',L,L',B,B',Q 을 입력 할 수 있습니다. 여러개를 한꺼번에 입력할 수 있으며 각 명령을 하나씩 수행하여 각 명령에 맞는 `Cube`클래스의 메소드를 호출 하고 수행중인 명령과 수행 후 변환 큐브를 출력합니다.

`enter`메소드들은 선언되면 큐브를 `temp` 변수에 깊은참조를 하고 % 연산자를 이용해 한칸씩 원하는 방향으로 이동시킵니다.

"Q" 혹은 "q" 가 입력되면 "bye~"를 출력하고 `isGoing`을 False로 변환 프로그램을 종료합니다.


### 실행 코드
```python
import copy

class Cube :
    myCube = []
    def __init__ (self):  # Cube가 생성되면 초기값 셋팅
        self.myCube = [["R","R","W"],["G","C","W"],["G","B","B"]]
    
    #각 명령들 입력시 수행할 메소드들
    def enterU (self):
        temp = copy.deepcopy(self.myCube[0])
        for idx in range(3) :
            self.myCube[0][idx]=temp[(idx+1)%3]
    def enterUr(self):
        temp = copy.deepcopy(self.myCube[0])
        for idx in range(3) :
            self.myCube[0][idx]=temp[(idx-1)%3]
    def enterR(self):
        temp = copy.deepcopy(self.myCube)
        for idx in range(3):
            self.myCube[idx][2]=temp[(idx+1)%3][2]
    def enterRr(self):
        temp = copy.deepcopy(self.myCube)
        for idx in range(3):
            self.myCube[idx][2]=temp[(idx-1)%3][2]
    def enterL(self):
        temp = copy.deepcopy(self.myCube)
        for idx in range(3):
            self.myCube[idx][0]=temp[(idx-1)%3][0]
    def enterLr(self):
        temp = copy.deepcopy(self.myCube)
        for idx in range(3):
            self.myCube[idx][0]=temp[(idx+1)%3][0]
    def enterB(self):
        temp = copy.deepcopy(self.myCube[2])
        for idx in range(3) :
            self.myCube[2][idx]=temp[(idx-1)%3]
    def enterBr(self):
        temp = copy.deepcopy(self.myCube[2])
        for idx in range(3) :
            self.myCube[2][idx]=temp[(idx+1)%3]
    def printCube(self):
        for row in range(3):
            for col in range(3):
                print (self.myCube[row][col], end = ' ')
            print()
            
cube = Cube() #큐브객체 생성
cube.printCube() #초기 큐브 출력
isGoing = True #프로그램 실행 여부 판단 변수

while(isGoing):
    msg = input("CUBE> ")    
    for idx, i in enumerate(msg) :
        if i =="'" : # ' 이면 아무런 동작 수행하지 않는다.
            continue
        if i == "Q" : # "Q" 입력시 실행 종료
            isGoing=False 
            print("bye~")
            break
        if idx != len(msg)-1 and  msg[idx+1] =="'" : #현재 위치가 입력 문자열에 맨 끝이 아니고 다음 문자에 ' 가 있는 경우
            if i == "U":
                cube.enterUr()
            elif i == "R":
                cube.enterRr()
            elif i == "L":
                cube.enterLr()
            elif i == "B":
                cube.enterBr()
            print(i+"'")
        else :  #'를 수행하지 않는 입력
            if i == "U":
                cube.enterU()
            elif i == "R":
                cube.enterR()
            elif i == "L":
                cube.enterL()
            elif i == "B":
                cube.enterB()
            print(i) #현재 수행한 명령을 출력
        cube.printCube() #명령 수행 후 변환된 큐브 출력
		```