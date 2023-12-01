# Task№1

This Python code defines a decorator named `my_new_decorator_is_task_1` which takes a function as an argument and returns a wrapper function. The wrapper function `the_wrapper_around_the_original_function` calls the original function with arguments `a` and `b`, then doubles the result before returning it.

The decorator is then applied to the `say_num` function using the `@` syntax, effectively modifying the behavior of `say_num`. When `say_num(2, 2)` is called, it will return the doubled result of the original function, `a + b`, which is `4`.
