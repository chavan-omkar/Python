
a = 5
b = 0

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter the number : "))
    print(k)
except ZeroDivisionError as e:
    print("Hey, You cannot divide by zero" , e)
except ValueError as f :
    print("Invalid input ", f)
except Exception as g:
    print("Something wnt wrong" , g)
finally:
    print("Resource closed")

# print("Bye")