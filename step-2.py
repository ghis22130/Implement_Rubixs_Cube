#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

