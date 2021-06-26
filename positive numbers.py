l,l1,n,i=[],[],0,0
while True:
    try:
        print('Enter n value: ')
        n=(int(input()))
        break
    except:
        print('Please enter an integer')
print('Enter the elements of the list:')
while i<n:
    try:
        l.append(int(input()))
    except:
        i-=1
        print('Please enter an integer')
    i+=1
print('The entered list is:',l)
for i in l:
    if i>0:
        l1.append(i)
print('All the positive elements in the list:',l1)
