D={"Aman":97,"Aditya":86,"Parth":74,"Shikhar":95}
x=str(input("Enter the name of student:"))
L=D.keys()
if x in L:
    print(x," got ",D[x]," marks")
else:
    print("Student not found")
