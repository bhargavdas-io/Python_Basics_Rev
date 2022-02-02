# Just a practise of exponential function in pyhton using for loop

def raise_num(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
        return result


print(raise_num(2, 5))
