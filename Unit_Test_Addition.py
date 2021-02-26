# addition of two numbers with zero as default parameters

def addition(num1=0, num2=0):
    try:
        # this is for condition num1 and num2 has values (True)
        if num1 and num2:
            return int(num1) + int(num2)
        # when None is passed as parameter
        else:
            return "Enter numbers"

    except ValueError as err:
        return err
