#方法1
X=input()
Y=input()
Z=input()
if X > Y > Z:
    print(X)
    print(Y)
    print(Z)
elif X > Z > Y:
    print(X)
    print(Z)
    print(Y)
elif Y > X > Z:
    print(Y)
    print(X)
    print(Z)
elif Y > Z > X:
    print(Y)
    print(Z)
    print(X)
elif Z > Y > X:
    print(Z)
    print(Y)
    print(X)
elif Z > X > Y:
    print(Z)
    print(X)
    print(Y)

#方法2
X=int(input())
y=int(input())
z=int(input())
list = [X,y,z]
list.sort(reverse=True)
print(list)
