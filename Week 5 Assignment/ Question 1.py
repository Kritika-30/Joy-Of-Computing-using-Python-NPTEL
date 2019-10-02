'''Arun is working in an office which is N blocks away from his house. He wants to minimize the time it takes him to go from his house to the office.
He can either take the office cab or he can walk to the office.
Arun's velocity is V1 m/s when he is walking. The cab moves with velocity V2 m/s but whenever he calls for the cab, it always starts from the office, covers N blocks, collects Arun and goes back to the office.
The cab crosses a total distance of N meters when going from office to Arun's house and vice versa, whereas Arun covers a distance of (2–√∗N) while walking.
Help Arun to find whether he should walk or take a cab to minimize the time.

Input Format:
A single line containing three integer numbers N, V1, and V2 separated by a space.

Output Format:
Print 'Walk' or 'Cab' accordingly'''

#!/usr/bin/python3
import math                                    //importing math library

input_string=input()                           //taking the input and converying it integer
list1=input_string.split()
for i in range(0,len(list1)):
  list1[i]=int(list1[i])
  
n=list1[0]
v1=list1[1]
v2=list1[2]

d1=(math.sqrt(2))*n                             // calculating time
d2=n*2
t1=d1/v1
t2=d2/v2

if t2>=t1:
  print('Walk')
else:
  print('Cab')
