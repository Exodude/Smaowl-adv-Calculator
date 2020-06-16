import scientificalmodule as sm


ans=input("sin,tan,%,power,root,logarhtim").strip()
while (ans!='sin' and ans!='tan' and ans!='%' and ans!='power' and ans!='root' and ans!='logarhtim' ):
    print("Give a valid answer!")
    ans=input("sin,tan,%,power,root,logarhtim").strip()
else:
                 
         if (ans=='sin'):
                  x=int(input("What's the degree:"))
                  val=sm.sinx(x)
                  state="The radians is"
                  
        elif (ans=='tan'):
                  x=int(input("What's the degree:"))
                  val=sm.tanx(x)
                  state="The tangent is"
        
         elif (ans=='%'):
                  num=int(input("what is the base number:"))
                  p=int(input("by what persentage:"))
                  val=sm.perc(p,num)
                  state="The value is"
                      
         elif (ans=='power'):
                  num=int(input("What number:"))
                  ex=int(input("What number do you want to power it:"))
                  val=sm.squaring
                  state="The value is"

         elif (ans=='root'):
                  num=int(input("What number:"))
                  ex=int(input("What number do you want to root it:"))
                  val=sm.squarerooting
                  state="The value is"
                  
         elif (ans=='logarhitim'):
                  b=int(input("what is the number for the natural logarhytim:"))
                  ex=int(input("What is the base:")
                  val=sm.logarhtim(b,ex)
                  state="The logarhytim is"
         
                  
         print(state,val)
