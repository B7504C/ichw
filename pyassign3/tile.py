'''tile.py:pave blocks
__author__ = 'Bai Yuchen'
__pkuid__  = '1800011798'
__email__  = '1800011798@pku.edu.cn'
'''
import copy
import turtle
q_h=int(input('墙横向有几个格'))
q_s=int(input('墙竖向有几个格'))
z_h=int(input('砖横向有几个格'))
z_s=int(input('砖竖向有几个格'))
wall= [0]*q_s
alist= [0]*q_h
for t in range(q_s):
    wall[t] = copy.deepcopy(alist)
every_result = []
all_methods = []


def check_h(lie,hang,wall):
    '''检查横着放砖是否可行'''
    if lie+z_h>q_h or hang+z_s>q_s:
        return False
    for t in range(z_s):
        for s in range(lie,lie+z_h):
            if wall[hang+t][s]!=0:
                return False
    return True


def check_s(lie,hang,wall):
    '''检查竖着放砖是否可行'''
    if lie+z_s>q_h or hang+z_h>q_s:
        return False
    for t in range(z_h):
        for s in range(lie,lie+z_s):
            if wall[hang+t][s]!=0:
                return False
    return True


def paving(wall,every_result,all_methods):
    '''铺长方形砖'''
    if wall==[[1]*q_h]*q_s:
        all_methods.append(every_result.copy())
        return 
    w=[]
    for i in range(q_s):
        for j in range(q_h):
            w.append(wall[i][j])
    for t in range(len(w)):
        if w[t]==0:
            lie=t%q_h
            hang=t//q_h
            break
    if check_h(lie,hang,wall):
        block=()
        for i in range(z_s):
            for j in range(z_h):
                wall[hang+i][lie+j]=1
                block=block+(lie+j+(hang+i)*q_h,)
        every_result.append(block)
        paving(wall,every_result,all_methods)
        for i in range(z_s):
            for j in range(z_h):
                wall[hang+i][lie+j]=0
        every_result.remove(block)
    if check_s(lie,hang,wall):
        block=()
        for i in range(z_h):
            for j in range(z_s):
                wall[hang+i][lie+j]=1
                block=block+(lie+j+(hang+i)*q_h,)
        every_result.append(block)
        paving(wall,every_result,all_methods)
        for i in range(z_h):
            for j in range(z_s):
                wall[hang+i][lie+j]=0
        every_result.remove(block)
    return


def paving2(wall, every_result, all_methods):
    '''铺正方形砖'''
    if wall==[[1]*q_h]*q_s:
        all_methods.append(every_result.copy())
        return 
    w=[]
    for i in range(q_s):
        for j in range(q_h):
            w.append(wall[i][j])
    for t in range(len(w)):
        if w[t]==0:
            lie=t%q_h
            hang=t//q_h
            break
    if check_h(lie,hang,wall):
        block=()
        for i in range(z_s):
            for j in range(z_h):
                wall[hang+i][lie+j]=1
                block=block+(lie+j+(hang+i)*q_h,)
        every_result.append(block)
        paving2(wall,every_result,all_methods)
        for i in range(z_s):
            for j in range(z_h):
                wall[hang+i][lie+j]=0
        every_result.remove(block)
    return


def draw(all_methods):
    '''画图'''
    t=turtle.Turtle()
    print('共有%d种铺法'%(len(all_methods)))
    number=int(input('从1到%d种中选择一种铺法'%(len(all_methods))))
    method=all_methods[number-1]
    for i in range(q_s+1):
        t.pu()
        t.goto(0,-i*25)
        t.pd()
        t.goto(q_h*25,-i*25)
    for i in range(q_h+1):
        t.pu()
        t.goto(i*25,0)
        t.pd()
        t.goto(i*25,-q_s*25)
    t.color('blue')
    t.pensize(6)
    for block in method:
        start=block[0]
        if start+z_h-1==block[z_h-1]:
            t.pu()
            t.goto((start%q_h)*25,-(start//q_h)*25)
            t.pd()
            t.goto(((start%q_h)+z_h)*25,-(start//q_h)*25)
            t.goto(((start%q_h)+z_h)*25,(-(start//q_h)-z_s)*25)
            t.goto((start%q_h)*25,(-(start//q_h)-z_s)*25)
            t.goto((start%q_h)*25,-(start//q_h)*25)
        else:
            t.pu()
            t.goto((start%q_h)*25,-(start//q_h)*25)
            t.pd()
            t.goto(((start%q_h)+z_s)*25,-(start//q_h)*25)
            t.goto(((start%q_h)+z_s)*25,(-(start//q_h)-z_h)*25)
            t.goto((start%q_h)*25,(-(start//q_h)-z_h)*25)
            t.goto((start%q_h)*25,-(start//q_h)*25) 

def main():
    if z_h==z_s:
        paving2(wall,every_result,all_methods)
        for method in all_methods:
            print(method)
        draw(all_methods)
    else:
        paving(wall,every_result,all_methods)
        for method in all_methods:
            print(method)
        draw(all_methods)

if __name__ == '__main__':
    main()

