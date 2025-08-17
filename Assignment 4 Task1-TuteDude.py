try:
    file1=open("Tutorial.txt","r")
    x=file1.readlines()
    for i in range(1,len(x)+1):
        print("Line",i,": ",x[i-1])
except FileNotFoundError:
    print("Error: The file was not found")
