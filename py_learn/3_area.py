a = float(input("please input a:"))
b = float(input("please input b:"))
c = float(input("please input c:"))

s = float((a+b+c)/2)

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
lenth = a + b + c
print("the area of '{0}','{1}','{2}' is '{3}'".format(a,b,c,area))
print("the lenth of '{0}','{1}','{2}' is '{3}'".format(a,b,c,lenth))