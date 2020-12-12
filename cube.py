#!/usr/bin/env python
# coding: utf-8

# In[]:


import copy

class Cube :
    #6면체 색상 셋팅
    def __init__ (self):
        self.front = [["O" for _ in range(3)] for _ in range(3)]
        self.right = [["G" for _ in range(3)] for _ in range(3)]
        self.left = [["W" for _ in range(3)] for _ in range(3)]
        self.up = [["B" for _ in range(3)] for _ in range(3)]
        self.down = [["R" for _ in range(3)] for _ in range(3)]
        self.back = [["Y" for _ in range(3)] for _ in range(3)]
        self.myCube = [front,right,left,up,down,back]
    
    def setSideList(self,side1,side2,side3,side4):
        return side1+side2+side3+side4        
    
    def getLeftSide(self,face):
        return [i[2] for i in face]
    
    def getRightSide(self,face):
        return [i[0] for i in face]
            
    def sideRotation(self,ls,ds,rs,us):
        side_list = self.setSideList(ls,ds,rs,us)
        temp = copy.deepcopy(side_list)
        for idx, i in enumerate(side_list):
            side_list[idx] = temp[(idx+3)%len(side_list)]
        
        sl = [side_list[i * 3:(i + 1) * 3] for i in range((len(side_list) + 3 - 1) // 3 )] 

        return sl
        
    def faceRotation(self,face):
        N = len(face)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = face[r][c]
        return ret
                 
    def setSide(self,face,col,sl):
        if face == self.front :
            for i in range(3) :
                self.front[col][i] == sl[i]
        elif face == self.left :
            for i in range(3) :
                self.left[col][i] == sl[i]
        elif face == self.right :
            for i in range(3) :
                self.right[col][i] == sl[i]
        elif face == self.up :
            for i in range(3) :
                self.up[col][i] == sl[i]
        elif face == self.down :
            for i in range(3) :
                self.down[col][i] == sl[i]
        elif face == self.back :
            for i in range(3) :
                self.back[col][i] == sl[i]
            
        
    def enterF(self):
        ls = self.getLeftSide(self.left)
        rs = self.getRightSide(self.right)
        us = self.up[0]
        ds = self.down[0]

        sl = self.sideRotation(ls,rs,us,ds)
        
        print(sl)
        self.up[0] = sl[3]
        self.down[0] = sl[1]
        self.setSide(self.left,2,sl[0])
        self.setSide(self.right,0,sl[2])
        self.front = self.faceRotation(self.front)
        
    #현재 큐브 상태 출력
    def printCube(self) :
        for row in up :
            for _ in range(3):
                print("    ",end="")
            for col in row :
                print(col,end=" ")
            print()

    
        for i in range(3):
            print(left[i][0],left[i][1],left[i][2],end="   ")
            print(front[i][0],front[i][1],front[i][2],end ="   ")
            print(right[i][0],right[i][1],right[i][2],end = "   ")
            print(back[i][0],back[i][1],back[i][2])

        for row in down :
            for _ in range(3):
                print("   ",end=" ")
            for col in row :
                print(col,end=" ")
            print()

cube = Cube()
cube.printCube()

isGoing = True
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
            elif i == "F":
                cube.enterFr()
            elif i == "D":
                cube.enterDr()
                
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
            elif i == "F":
                cube.enterF()
            elif i == "D":
                cube.enterD()
            print(i) #현재 수행한 명령을 출력
    cube.printCube() #명령 수행 후 변환된 큐브 출력
