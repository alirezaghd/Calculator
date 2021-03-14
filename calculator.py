import math
a = int(input("Enter the first number:"))

op = input("Enter the operator:")
if op == 'sqrt'  or op == 'sin' or op == 'cot' or op == 'tan' or op == 'fact':
   result = (a)
else:
    
    b = int(input("Enter the second number:"))


if op == "+":
    result = a + b 

elif op == "-":
    result = a - b 

elif op == "*":
    result = a * b 

elif op == "/":
    if b == 0 :
        result = "cannot"
    else:
        result = a / b 

elif op == "^" :
    result = a ** b

elif op == "Log":
    result = math.log(a,b)

elif op == "sqrt":
    result = math.sqrt(a)

elif op == "sin":
    c = (a / 180) * math.pi
    result = math.sin(c)

elif op == "tan":
    c = (a / 180) * math.pi
    result = math.tan(c)

elif op == "cot":
    c = (a / 180) * math.pi
    x = 1
    result = x / math.cos(c)

elif op == "fact":
    result = math.factorial(a)


else:
    print("Eror!")

print(result)
