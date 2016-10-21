def print_result(func):
    def decorated_func(*args):
        print(func.__name__)
        x = func(*args)
        if type(x) == list:
            for el in x: print(el)
        elif type(x) == dict:
            for key in x: print('{} = {}'.format(key, x[key]))
        else:
            print(x)
        return x
    return decorated_func