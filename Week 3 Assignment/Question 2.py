#Given a list A of numbers (integers), you have to print those numbers which are not multiples of 5.

input_string=input()
list1=input_string.split()

for num in list1:
  if int(num)%5 != 0:
    print(num,end=" ")
