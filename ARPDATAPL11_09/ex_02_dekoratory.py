import time




def my_long_function(n):
    variable = 0
    print("jestem w funkcji")
    for i in range(100000 * n):
        variable += variable + i


my_long_function(2)