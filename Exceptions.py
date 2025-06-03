t = int(input())
for _ in range(t):
    firstValue, secondValue = input().split()
    try:
        result = int(firstValue) // int(secondValue)
        print(result)
    except ZeroDivisionError as err:
        print(f"Error Code: {err}")
    except ValueError as error:
        print(f"Error Code: {error}")
