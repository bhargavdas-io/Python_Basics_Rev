

# Comparision operator using if-else statements:


def big_num(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        print(num_1)
    elif num_2>=num_1 and num_2>=num_3:
        print(num_2)
    else:
        print(num_3)

big_num(4,12,9)

