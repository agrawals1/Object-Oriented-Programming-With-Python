try:
    f = open("demofile2.txt", "a")
except:
    f = open("demofile2.txt", "x")
f.write("some random content")
f.close()

try:
    f = open("demofile2.txt", "r")
    print(f.read())
except:
    print("file dows not exist")  

try:
    f = open("demofile1.txt", "r")
    print(f.read())
except:
    print("file does not exist")    

