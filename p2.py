# Simple Calculator

def main():
    
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    
    op = int(input("What do you wanna do?? \n1.Add \n2.Sub \n3.Multiply \n4.Div \n "))
    if (op == 1):
        r = num1+num2
    elif(op==2):
        r = abs(num1 - num2)
    elif(op==3):
        r= num2*num1
    elif(op==4):
        r = num1 / num2
    else:
        print("Invalid input")
    
    print(r)
    
    
if __name__ == "__main__":
    main()