x=input()
x_list=x.split()
N=int(x_list[0])
CB=int(x_list[1])
CP=int(x_list[2])

data=list()

for i in range(N):
    y=input()
    y_list=y.split()
    data.append(y_list)

TNB=0
TNP=0
for i in data:
    TNB=TNB+int(i[0])
    TNP=TNP+int(i[1])

if TNB%10==0:
    PB=TNB/10 
else:
    PB=int(TNB/10) + 1
    
if TNP%10==0:
    PP=TNP/10 
else:
    PP=int(TNP/10) + 1
    
cost=int((PB*CB)+(PP*CP))
print (cost)