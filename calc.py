while True:
    def divide(a, b):
        result = a/b
        print(result)

    def multiply(a,b):
        result = a*b
        print(result)

    def add(a, b):
        result = a+b
        print(result)

    def subtract(a, b):
        result = a-b
        print(result)

    operation = input('What operation would you like to perform? (Divide, multiply, add, subtract) When you are done input "stop" ')

    if operation == 'stop':
        break

    a = int(input('First number '))
    b = int(input('Second number '))

    if operation == 'divide':
        divide(a, b)

    elif operation == 'multiply':
        multiply(a, b)

    elif operation == 'add':
        add(a, b)

    elif operation == 'subtract':
        subtract(a, b)
