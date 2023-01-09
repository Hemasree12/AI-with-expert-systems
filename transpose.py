a=[[5,8],
   [6,4],
   [9,6]]
print("given matrix : ")
for y in a:
    print(y)

x=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        x[j][i]=a[i][j]

print("transpose of matrix :")
for k in x:
    print(k)
