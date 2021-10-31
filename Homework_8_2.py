
def type_logger(func):
    def wrapper(*args):
        print(func.__name__+"(" + ",".join([str(i)+": "+ str(type(i)) for i in args])+")")
        func(*args)
    return wrapper

@type_logger
def calc_cube(a,b,c):
   return str(a)+str(b)+str(c)

a = calc_cube(5,"ads",[123])