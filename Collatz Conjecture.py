# vgv Roisin Anglim 11-02-18 

#Collatz : If even number divide by 2, if uneven multiply by 3 + 1



# Requests user to enter an interger

i = int(input("input integer ")) 

print(i) 

#Do the following when i is not equal to one

while i != 1: 

#When i even number

     if i %2 ==0: 

         i= i/2

         print(int(i))   

#When i uneven number      

     elif i %2 ==1:

         i= i*3+1

         print(int(i))
