def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("your second number cannot be zero!")
    except ValueError:
        print("enter integer numbers only!")
    except Exception as e:
        print(f"Error: {e}")
    else:
        return result
    finally:
        print("Ran succesfully!")


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("Result:", divide(num1, num2))