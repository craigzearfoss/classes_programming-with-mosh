def fizz_buzz(input):
    if input % 3 == 0:
        if input % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print("3: ", fizz_buzz(3))
print("5: ", fizz_buzz(5))
print("15:", fizz_buzz(15))
print("7: ", fizz_buzz(7))
