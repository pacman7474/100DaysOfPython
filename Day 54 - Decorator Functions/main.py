# import time
#
# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970
#
#
# # Write your code below 👇
#
# def speed_calc_decorator(func):
#     time_now = time.time()
#     func()
#     new_time = time.time()
#     print(f"{func.__name__} run speed: {new_time - time_now}s")
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i

# TODO: Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result
    return wrapper


# TODO: Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)