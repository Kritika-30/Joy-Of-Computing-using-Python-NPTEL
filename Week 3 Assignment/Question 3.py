#You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit
#(i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.

count0=0
count1=0
number=input()
for i in str(number):
    if int(i) == 0:
        count0=count0+1
    else:
        count1=count1+1


if (count1==1 and count0>=0) or (count0==1 and count1>=0) :
    print("YES")
else:
    print("NO")
