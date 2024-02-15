x = int(input("Enter a number of repetitions: "))

def repeat_call(func):
    def wrapper():
        for _ in range(x):
            func()
    return wrapper

@repeat_call
def hello():
    print("Hello")

hello()