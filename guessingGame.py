#import random
#x=random.randint(1,100)
#print(x)
#from random import randint
#x=randint(1,100)
#print(x)
from random import *
x=randint(1,100)
print(x)
S='AB CD EF G HI'
c=choice(S)
print(c)
#y=sample(S,9)
y=sample(S,3)
print(y)
d=''.join(y)
print(d)



'''import string as st 

print(st.ascii_lowercase)
print(st.ascii_uppercase)
print(st.digits)
print(st.punctuation)'''


'''#wap computer will generate a random number
from random import randint
x=randint(1,100)
S=''
while(S!=0):
 S=int(input("enter the number"));
  if(S>x):
    if((S-x)>10):
      print("number is too high ")
    else:
       print("number is  high")
  elif(x>S):
      if((x-S)>10):
        print("number is too low")
      else:
        print("number is  low")
  
  else:
     print("input is right")'''


  
     
     
