print("/\/\/\/\/\/CALCULATOR/\/\/\/\/")
a=int(input("Enter a digit      "))
b=int(input("Enter second digit     "))
op=input("Select an operation (/,*,+,-)     ")
if(op=="+"):
    result=a+b
elif(op=="-"):
    result=a-b
elif(op=="/"):
    result=a/b
elif(op=="*"):
    result=a*b
else:
    print("Invalid operation")

print("Result is: ", result)