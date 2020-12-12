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
        self.finish = [self.front,self.right,self.left,self.up,self.down,self.back]
    
    # 회전해야할 옆면들을 하나의 배열로 묶어줍니다
    def setSideList(self,side1,side2,side3,side4):
        return side1+side2+side3+side4        
    
    #회전하고자 하는 면의 왼쪽 옆면을 반환
    def getLeftSide(self,face):
        return [i[2] for i in face]
    #회전하고자 하는 면의 오른쪽 옆면을 반환
    def getRightSide(self,face):
        return [i[0] for i in face]
    #회전하고자 하는 옆면의 정보를 하나의 리스트로 담아 회전시켜준다음 다시 분리해서 반환 (왼쪽 아래 오른쪽 위) 순서
    def sideRotate(self,ls,ds,rs,us):
        side_list = self.setSideList(ls,ds,rs,us)
        temp = copy.deepcopy(side_list)
        for idx, i in enumerate(side_list):
            side_list[idx] = temp[(idx+3)%len(side_list)]
        
        sl = [side_list[i * 3:(i + 1) * 3] for i in range((len(side_list) + 3 - 1) // 3 )] 
        return sl
    
    #회전하고자 하는 옆면의 정보를 하나의 리스트로 담아 회전시켜준다음 다시 분리해서 반환 (왼쪽 아래 오른쪽 위) 순서
    def sideReverseRotate(self,ls,ds,rs,us):
        side_list = self.setSideList(ls,ds,rs,us)
        temp = copy.deepcopy(side_list)
        for idx, i in enumerate(side_list):
            side_list[idx] = temp[(idx-3)%len(side_list)]
        
        sl = [side_list[i * 3:(i + 1) * 3] for i in range((len(side_list) + 3 - 1) // 3 )] 
        return sl
    
    #회전하고자 하는 면을 시계방향으로 90도 회전
    def faceRotate(self,face):
        N = len(face)
        ret = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = face[r][c]
        return ret
    
    #회전하고자 하는 면을 반시계방향으로 90도 회전
    def faceReverseRotate(self,face):
        ret = []
        for k in list(zip(*face)):
            ret.append(list(k))
        return ret
    
    #회전된 옆면을 적용
    def setSide(self,face,col,sl):
        if face == "front" :
            for i in range(3) :
                self.front[i][col] = sl[i]
        elif face == "left" :
            for i in range(3) :
                self.left[i][col] = sl[i]
        elif face == "right" :
            for i in range(3) :
                self.right[i][col] = sl[i]
        elif face == "up" :
            for i in range(3) :
                self.up[i][col] = sl[i]
        elif face == "down" :
            for i in range(3) :
                self.down[i][col] = sl[i]
        elif face == "back" :
            for i in range(3) :
                self.back[i][col] = sl[i]
            
    #F입력받았을때
    def enterF(self):
        ls = self.getLeftSide(self.left)
        rs = self.getRightSide(self.right)
        us = self.up[0]
        ds = self.down[0]

        sl = self.sideRotate(ls,ds,rs,us)
        self.up[0] = sl[3]
        self.down[0] = sl[1]
        self.setSide("left",2,sl[0])
        self.setSide("right",0,sl[2])
        self.front = self.faceRotate(self.front)
    
    #L입력받았을때
    def enterL(self):
        ls = self.getLeftSide(self.back)
        rs = self.getRightSide(self.front)
        us = self.getLeftSide(self.up)
        ds = self.getRightSide(self.down)

        sl = self.sideRotate(ls,ds,rs,us)
        
        self.setSide("up",2,sl[3])
        self.setSide("down",0,sl[1])
        self.setSide("back",2,sl[0])
        self.setSide("front",0,sl[2])
        self.left = self.faceRotate(self.left)
    
    #R입력받았을때
    def enterR(self):
        ls = self.getLeftSide(self.front)
        rs = self.getRightSide(self.back)
        us = self.getRightSide(self.up)
        ds = self.getLeftSide(self.down)

        sl = self.sideRotate(ls,ds,rs,us)
        self.setSide("up",0,sl[3])
        self.setSide("down",2,sl[1])
        self.setSide("back",0,sl[2])
        self.setSide("front",2,sl[0])
        self.right = self.faceRotate(self.right)
    
    #B입력받았을때
    def enterB(self):
        ls = self.getLeftSide(self.right)
        rs = self.getRightSide(self.left)
        us = self.up[2]
        ds = self.down[2]

        sl = self.sideRotate(ls,ds,rs,us)
        self.up[2] = sl[3]
        self.down[2] = sl[1]
        self.setSide("right",2,sl[0])
        self.setSide("left",0,sl[2])
        self.back = self.faceRotate(self.back)
        
    #U입력받았을때
    def enterU(self):
        ls = self.right[0]
        rs = self.left[0]
        us = self.front[0]
        ds = self.back[0]

        sl = self.sideRotate(ls,ds,rs,us)
        self.left[0] = sl[2]
        self.back[0] = sl[1]
        self.right[0] = sl[0]
        self.front[0] = sl[3]
        
        self.up = self.faceRotate(self.up)
          
    #D입력받았을때
    def enterD(self):
        ls = self.left[2]
        rs = self.right[2]
        us = self.front[2]
        ds = self.back[2]

        sl = self.sideRotate(ls,ds,rs,us)
        self.left[2] = sl[0]
        self.back[2] = sl[1]
        self.right[2] = sl[2]
        self.front[2] = sl[3]
        
        self.down = self.faceRotate(self.down)
        
    #F'입력받았을때
    def enterFr(self):
        ls = self.getLeftSide(self.left)
        rs = self.getRightSide(self.right)
        us = self.up[0]
        ds = self.down[0]

        sl = self.sideReverseRotate(ls,ds,rs,us)
        self.up[0] = sl[3]
        self.down[0] = sl[1]
        self.setSide("left",2,sl[0])
        self.setSide("right",0,sl[2])
        self.front = self.faceReverseRotate(self.front)
    
    #L'입력받았을때
    def enterLr(self):
        ls = self.getLeftSide(self.back)
        rs = self.getRightSide(self.front)
        us = self.getLeftSide(self.up)
        ds = self.getRightSide(self.down)

        sl = self.sideReverseRotate(ls,ds,rs,us)
        
        self.setSide("up",2,sl[3])
        self.setSide("down",0,sl[1])
        self.setSide("back",2,sl[0])
        self.setSide("front",0,sl[2])
        self.left = self.faceReverseRotate(self.left)
    
    #R'입력받았을때
    def enterRr(self):
        ls = self.getLeftSide(self.front)
        rs = self.getRightSide(self.back)
        us = self.getRightSide(self.up)
        ds = self.getLeftSide(self.down)

        sl = self.sideReverseRotate(ls,ds,rs,us)
        self.setSide("up",0,sl[3])
        self.setSide("down",2,sl[1])
        self.setSide("back",0,sl[2])
        self.setSide("front",2,sl[0])
        self.right = self.faceReverseRotate(self.right)
    
    #B'입력받았을때
    def enterBr(self):
        ls = self.getLeftSide(self.right)
        rs = self.getRightSide(self.left)
        us = self.up[2]
        ds = self.down[2]

        sl = self.sideReverseRotate(ls,ds,rs,us)
        self.up[2] = sl[3]
        self.down[2] = sl[1]
        self.setSide("right",2,sl[0])
        self.setSide("left",0,sl[2])
        self.back = self.faceReverseRotate(self.back)
        
    #U'입력받았을때
    def enterUr(self):
        ls = self.right[0]
        rs = self.left[0]
        us = self.front[0]
        ds = self.back[0]

        sl = self.sideReverseRotate(ls,ds,rs,us)
        self.left[0] = sl[2]
        self.back[0] = sl[1]
        self.right[0] = sl[0]
        self.front[0] = sl[3]
        
        self.up = self.faceReverseRotate(self.up)
          
    #D'입력받았을때
    def enterDr(self):
        ls = self.left[2]
        rs = self.right[2]
        us = self.front[2]
        ds = self.back[2]

        sl = self.sideReverseRotate(ls,ds,rs,us)
        self.left[2] = sl[0]
        self.back[2] = sl[1]
        self.right[2] = sl[2]
        self.front[2] = sl[3]
        
        self.down = self.faceReverseRotate(self.down)
        
    #현재 큐브 상태 출력
    def printCube(self) :
        for row in range(2,-1,-1) :
            for _ in range(3):
                print("    ",end="")
            for col in self.up[row] :
                print(col,end=" ")
            print()

    
        for i in range(3):
            print(self.left[i][0],self.left[i][1],self.left[i][2],end="   ")
            print(self.front[i][0],self.front[i][1],self.front[i][2],end ="   ")
            print(self.right[i][0],self.right[i][1],self.right[i][2],end = "   ")
            print(self.back[i][0],self.back[i][1],self.back[i][2])

        for row in self.down :
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
# %%
