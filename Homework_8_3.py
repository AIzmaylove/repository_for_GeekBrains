def val_checker(l_func):
    def decorator(func):
        def wrapper(x):
            if l_func(x):
                func(x)
            else:
                raise ValueError("wrong val "+str(x))
        return wrapper
    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
a = calc_cube(-5)