def main():
    expression=input("Expression: ").split(" ")
    x=float(expression[0])
    operator=str((expression[1]))
    y=float((expression[2]))
    answer = operation(x, operator, y)
    if answer == -1:
        print("Whatever you did was very dumb")
    else:
        print(answer)
    
def operation(x, operator, y):    
    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "*":
        return x*y
    elif operator == "/":
        if y==0:
           return -1
        else:
            return x/y        
    else:
        return -1
        
if __name__=="__main__":
    main()