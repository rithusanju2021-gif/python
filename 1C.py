list=[]
y=int(input("Enter the range elements:"))
for i in range(1,y+1):
    u=int(input(f"Enter element:"))
    list.append(u)
n=len(list)
print("All posssible combinations:")
for i in (list):
    for j in(list):
        print(i,j)
