#mhn Roisin Anglim 08-04-18 
#Identify smallest number divided by 1-20 without and remainder 
# Python Program to find the L.C.M. of two input number


 # Set variables
n =  2520
c = True
b = 0

while c: 
  # Range set as 11 - 20 as we already know LCM for 1-10 is 2520
  for x in range(11,21): 
  # Set a as the remainder from n  modulus X
    a = n % x
    b = b + a 
  # If b does not equal zero increase n by 20
  if b != 0 :
      b = 0 
      n = n + 20 
    # print every 1 x million so that we can keep track of the code
      if n % 1000000 == 0: 
         print(n) 
  # after the for loop if the remainder is zero print N
  else : 
      c = False 
print(n)
