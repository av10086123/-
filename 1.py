#成绩提取分类——————————————————————————————————————————————————————————————
a=int(input("add student number:"))
c=0
d=0
chengji=[] #设空
while (a):
    b = int(input("add course:"))
    chengji.append(b)    #逐一加入
    a-=1
    if a==0:
        break
chengji.sort()        #排序，可要可不要
e=len(chengji)        #确定循环次数
for k in range (0,e):
    m=chengji.__getitem__(k)
    if m>=50:
        c+=1
    else:
        d+=1

print("up 50 course %d below 50 course %d"%(c,d))
