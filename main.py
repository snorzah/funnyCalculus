from calc import *
if __name__ == "__main__":
    f = lambda x: x**2
    print(integrate(f, 0, 2))
    print(integrate(f, 2, 0))