'''f=open("Matrix.txt",'w')
n1=int(input("Enter number of rows "))
n2=int(input("Enter number of columns "))
for i in range(n1):
    a=list(map(int,input("Enter "+str(n2)+" entries for "+str(i+1)+" row ").split()))
    for j in a:
        f.write(str(j)+' ')
    f.write('\n')
f.close()'''
f=open("Matrix.txt")
l=f.readlines()
l2=[]
for i in l:
    l1=i.split()
    l3=[]
    for j in l1:
        l3.append(int(j))
    l2.append(l3)
for i in l2:
    print(i)
def reduce(l,e):
    b=l[0]
    for i in range(1,len(l)):
        c=l[i]
        d=c[e]/b[e]
        for j in range(len(c)):
            c[j]=c[j]-d*b[j]
        l[i]=c
    return(l)
def replace(i,l):
    for j in range(1,len(l)):
        c=l[j][i]
        if c!=0:
            l[0],l[j]=l[j],l[0]
            break
    return l
l3=[(1,1)]
if l2[0][0]==0:
    for i in range(len(l2[0])):
        if l2[0][i]==0:
            l2=replace(i,l2)
            if l2[0][i]!=0:
                break
        elif l2[0][i]!=0:
            break
print('')
for i in l2:
    print(i)
l2=reduce(l2,0)
print('')
for i in l2:
    print(i)
l1=l2.copy()
f=2
while len(l1)!=1:
    del l1[0]
    e=0
    for i in range(1,len(l1[0])):
        if l1[0][i]==0:
            l1=replace(i,l1)
            if l1[0][i]!=0:
                e=i
                l3.append((f,e+1))
                break
        elif l1[0][i]!=0:
            e=i
            l3.append((f,e+1))
            break
    else:
        continue
    f+=1
    l1=reduce(l1,e)
    for i in range(len(l1)):
        l2[len(l2)-len(l1)+i]=l1[i]
    print('')
    for i in l2:
        print(i)
print('')
def reduce_back(l,e):
    b=l[-1]
    for i in range(len(l)-2,-1,-1):
        c=l[i]
        d=c[e]/b[e]
        for j in range(len(c)):
            c[j]=c[j]-d*b[j]
        l[i]=c
    return(l)
def scale(a):
    for j in range(len(a)):
        if a[j]!=0:
            b=a[j]
            break
    for i in range(len(a)):
        if a[i]==0:
            pass
        else:
            a[i]=a[i]/b
    return a
l1=l2.copy()
while set(l1[-1])=={0}:
    del l1[-1]
l1[-1]=scale(l1[-1])
for i in range(len(l1)):
        l2[i]=l1[i]
print('')
for i in l2:
        print(i)
l1=reduce_back(l1,l3[-1][-1]-1)
for i in range(len(l1)):
        l2[i]=l1[i]
print('')
for i in l2:
        print(i)
f=-1
while len(l1)!=1:
    del l1[-1]
    f-=1
    l1[-1]=scale(l1[-1])
    l1=reduce_back(l1,l3[f][-1]-1)
    for i in range(len(l1)):
            l2[i]=l1[i]
    print('')
    for i in l2:
            print(i)
l4=[]
for i in l3:
    l4.append(i[1])
print("pivot positions are",l3)
l5=[]
for j in range(1,len(l2[0])+1):
    if j not in l4:
        l5.append(j)
if len(l3)==len(l2[0]):
    print("Only solution is: ",[0]*len(l2[0]))
else:
    while set(l2[-1])=={0}:
        del l2[-1]
    for i in range(1,len(l2[0])+1):
        l=[]
        if i not in l4:
            c=0
            while len(l)!=len(l2[0]):
                if l2[c][i-1]!=0:
                    l.append(-l2[c][i-1])
                elif l2[c][i-1]==0:
                        l.insert(l3[c][1]-1,0)
                if c+1>=len(l2):
                    break
                c+=1
            if len(l)<len(l2[0]):
                #c=0
                for j in l5:
                    if i!=j:
                        l.insert(j-1,0)
            l.insert(i-1,1)
            print('x'+str(i)+'*',end='')
            print(l,end='')
            print('+',end='')
    print([0]*len(l2[0]))

        

    
