def rev_no(num):
    rev=0

    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10

    print(rev)
rev_no(6546464)

"""num=12345
rev=0

while (num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10

print(rev)"""