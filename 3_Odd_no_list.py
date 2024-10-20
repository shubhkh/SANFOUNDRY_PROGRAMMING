"""low=2
upp=100

for i in range(low,upp):
    if i%2!=0:
        print(i,'Odd no')"""


"""list1=[16,51,56,16,5,51]
for num in list1:
    if num%2!=0:
        print(num,'Odd no')"""

"""l1=[5,15,65,48,66]
only_odd=[num for num in l1 if num%2==1]
print(only_odd)"""

l1=[34,86,48,61,32,18]
odd_no = list(filter(lambda x: (x%2==1),l1))

print('odd no in the list:',odd_no)

