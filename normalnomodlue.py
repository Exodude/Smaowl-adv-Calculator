
n=int(input("Enter the total count of numbers you want: "))
val=0
a=float(input("Number:"))
for i in range(0,n-1):
         op=input("Operator:")
         b=float(input("Number:"))
         if(op=='+'):
                  val=a+b
                  a=val
         if(op=='-'):
                  val=a-b
                  a=val

         if(op=='*'):
                  val=a*b
                  a=val

         if(op=='/'):
                  val=a/b
                  a=val

print(val)

                  
                  


                  

         
