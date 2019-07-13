def func_by_work2():
    return 3

def func_by_work():
    return 2

def func_work():
    return 1 + func_by_work() - func_by_work2()

if __name__ == '__main__':
    print (func_work())
    pass
