def user_input_division(input_1: str, input_2: str):
    try:
        result = int(input_1)/int(input_2)
    except ZeroDivisionError:
        print("\nDon't division by zero")
    except ValueError:
        print("\nThis division is not available")
    else:
        return result


var_1, var_2 = [input('Enter number: ') for _ in range(2)]
if check := user_input_division(var_1, var_2):
    print("Rusult of division is", check)
else:
    print("\nThe program has stopped.")

