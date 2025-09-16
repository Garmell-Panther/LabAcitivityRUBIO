def gcd(x, y):
    # Recursive gcd
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

# Main program
while True:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
    if x > 0 and y > 0:
        break
    else:
        print("Invalid input! Please enter positive integers only.")

print(f"The LCM of {x} and {y} is = {lcm(x, y)}")

