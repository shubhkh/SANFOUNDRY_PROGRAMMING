"""def palindrom_str(s1):
    s2=""
    for i in s1:
        s2=i+s2
    if(s1==s2):
        print('Yes, String is palindrom')
    else:
        print('No, String is not palindrom')

palindrom_str("RADAR")"""

str='RADAR'
str=str.casefold()

if(str==str[::-1]):
    print('Palindrom str')
else:
    print('Not Palindrom str')


"""s1="RADAR"
s2=""

for i in s1:
    s2=i+s2
if (s1==s2):
    print('Yes, String is palindrom')
else:
    print('No, String is not palindrom')"""