import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):

    def time_diff():
        start_time = time.time()
        function()
        time_taken = time.time()
        name = function.__name__
        print(name + " " + str(time_taken - start_time))

    return time_diff


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()

slow_function()
