def cwff():
    f=input("Enter the file name: ")
    file=open(f,'r')
    count=0
    for line in file:
        words=line.split()
        count=count+len(words)
    print("The number of words are ",count)

cwff()