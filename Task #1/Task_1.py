def my_new_decorator_is_task_1(func):
    def the_wrapper_around_the_original_function(a, b):
        result = func(a, b)
        return result * 2

    return the_wrapper_around_the_original_function


@my_new_decorator_is_task_1
def say_num(a, b):
    return a + b


print(say_num(2, 2))