while True:
  print("\n menu")
  print("1. addition")
  print("2. subtraction")
  print("3.multiplication")
  print("4.division")
  print("5. exit")
  choice=int(input("enter your choice:"))

  if choice==5:
    print("exiting pogram,goodbye!")
    break
  elif choice in[1,2,3,4]:
    num1=float(input("enter frist number"))
    num2=float(input("enter second number"))
    if choice==1:
     print(f"the result is:{num1+num2}")
    elif choice==2:
      print(f"the result is:{num1-num2}")
    elif choice==3:
      print(f"the result is:{num1*num2}") 
    elif choice==4:
      if num2!=0:
       print(f"the result is:{num1/num2}")   
      else:
           print("divison by zero is not allowed.") 
  else:
     print("invalid choice chee thu please try again")           
