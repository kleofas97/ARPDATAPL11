import time

# Dekoratory - wrappery wokół funkcji.
# najlpeszy przyklad - bez integracji w funkcje możemy zmierzyc czas jej wywolania
# otaczajac ją wrapperem

def timer(func):
    def wrap_function(*args, **kwargs):
        start_time = time.time()
        print('Rozpoczeto mierzenie czasu - funkcja dopiero sie zacznie')
        result = func(*args, **kwargs)
        print('Zakonczylem funkcje')
        end_time = time.time()
        print(f'Function {func.__name__} executed in {end_time - start_time}')
        return result

    return wrap_function


@timer
def my_long_function(n):
    variable = 0
    print("jestem w funkcji")
    for i in range(100000 * n):
        variable += variable + i
    return None


my_long_function(2)
