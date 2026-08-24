s1 = int(input("enter a number: "))
operator = input("enter operator(+, _,*,/): ")
s2 = float(input("enter second number: "))

if operator =="+":
    print("ans:", s1+ s2)
    
elif operator =="-":
    print("ans:", s1-s2)
    
elif operator == "*":
    print("ans:",s1 * s2)
    
elif operator == "/":
    if s2 != 0:
        print(int("ans:", s1 / s2))
    else:
        print("cannot be divided  by zero")
        
else:
    print("invalid operator")                   
    