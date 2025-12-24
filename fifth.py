x = 10
def show():
    global x
    x=100
    print("the value of x inside the fuction:", x)


show()
print("the value of x is:", x)