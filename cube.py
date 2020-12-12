#!/usr/bin/env python
# coding: utf-8

# In[]:


class Cube :
    #6면체 색상 셋팅
    def __init__ (self):
        self.front = [["O" for _ in range(3)] for _ in range(3)]
        self.right = [["G" for _ in range(3)] for _ in range(3)]
        self.left = [["W" for _ in range(3)] for _ in range(3)]
        self.up = [["B" for _ in range(3)] for _ in range(3)]
        self.down = [["R" for _ in range(3)] for _ in range(3)]
        self.back = [["Y" for _ in range(3)] for _ in range(3)]
    
    #현재 큐브 상태 출력
    def printCube(self) :
        for row in self.up :
            for _ in range(3):
                print("    ",end="")
            for col in row :
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
