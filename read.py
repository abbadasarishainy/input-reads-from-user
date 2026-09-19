n=int(input("enter the total elements:"))
d={}
for i in range(n):
    k=input(f"enter key{i+1}:")
    v=int(input( f"enter val{i+1}:"))
    d[k]=v
print(d)
