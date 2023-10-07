def pattern(str,len):
    for i in range(len):
        for j in range(len):
            if((j==0) or (j==len-1) or (i+j==len-1 and i>=len//2) or (i==j and i>=len//2)):
                print(str[i],end=" ")
            else:
                print(" ",end=" ")
        print()
str=input()
len=len(str)
pattern(str,len)
