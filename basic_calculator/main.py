"""This is the entry point of the program."""


def basic_calculator(num1, num2, operation):
    if operation.lower() == 'add':
        return (num1 + num2)
    elif operation.lower() == 'subtract':
        return (num1 - num2)
    elif operation.lower() == 'multiply':
        return (num1 * num2)
    elif operation.lower() == 'divide':
        return float(num1 / num2)
    else:
        return 'Invalid operation'
