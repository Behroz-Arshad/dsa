import time

def decorator_function(other_function):
    def wrapper(*args, **kwargs):
        print("wraper")
        return other_function(*args, **kwargs)
    return wrapper

# Classbased

class Decorator:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Class base wrapper")
        return self.original_function(*args,**kwargs)



@decorator_function
def display():
    print("display")

@decorator_function
def hello():
    print("hello")

@decorator_function
def display_info(age,name):
    print(f"hello {name} with age {age}")


@Decorator
def display_class_base_decorator():
    print("display")

@Decorator
def hello_class_base_decorator():
    print("hello")

@Decorator
def display_info_class_base_decorator(age,name):
    print(f"hello {name} with age {age}")


# calculate time
def my_timer(original_function):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"time = {t2}")
        return result
    return wrapper



@my_timer
def display_with_time():
    time.sleep(1)
    print("display")


display()
print("------------")
hello()
print("------------")
display_info(30,"Behroz")

print("--------0--------")
display_class_base_decorator()
print("------------")
hello_class_base_decorator()
print("------------")
display_info_class_base_decorator(30,"Behroz")

display_with_time()