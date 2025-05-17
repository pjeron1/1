import time



def calculate(n):
    result = n*n*n*n*n*n/(5*n)
    yield result



def timer(function):
    def wrapper():
        start = time.time()
        result = function()
        end = time.time()
        print(f"Час використання {end - start:.4f} секунд")
        return result
    return wrapper()

@timer
def my_function():
    for f in calculate(n=124840):
        print(f)

def some_function():
    time.sleep(1)

    return

def test_time_function():
    some_function()

test_time_function()