operator = ""
while operator !="xyz":
        operator=input("please enter any operator:")
        if operator =="+":
            num1=int(input("please enter any number:"))
            num2=int(input("please enter another number:"))
            print("{} + {}".format(num1,num2))
            print(num1+num2)
        elif operator =="-":
            num1=int(input("please enter any number:"))
            num2=int(input("please enter another number:"))
            print("{} - {}".format(num1,num2))
            print(num1-num2)
        elif operator =="*":
            num1=int(input("please enter any number:"))
            num2=int(input("please enter another number:"))
            print("{} * {}".format(num1,num2))
            print(num1*num2)
        elif operator =="/":
            num1=int(input("please enter any number:"))
            num2=int(input("please enter another number:"))
            print("{} / {}".format(num1,num2))
            print(num1/num2)
        else:
            print("You have not provided an accurate operator, please try again")