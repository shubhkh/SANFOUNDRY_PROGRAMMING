def palindrom(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if (temp==rev):
        print('Palindrom no')
    else:
        print('Not Palindrom')

palindrom(12546)
palindrom(12121)


"""num=12121
rev=0
temp=num

while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10

if (rev==temp):
    print('Plindrom no')
else:
    print('Not Palindrom')"""