marks=85
if marks>=90:
    print("grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")

num=10
if(num>0):
    if(num%2==0):
        pass
    else:
        print("Positive odd number")
for i in range(1,6):
    for k in range(1,4):
        if(i==3):
            pass
        print(i,k)

j=1
while j<5:
    print(j)
    j+=1


def add(a,b):
    return a+b

print(add(90,60))