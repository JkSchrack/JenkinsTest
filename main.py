from Person import Person

def addition(x, y):
    return (x + y)

if __name__ == "__main__":
    num1 = 5
    num2 = 6
    print("%d + %d = %d" % (num1, num2, addition(num1, num2)))

    me = Person("Justin", "Vancouver", 25)
    me.dob()