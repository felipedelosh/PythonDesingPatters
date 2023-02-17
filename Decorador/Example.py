def decorator_func(functionX):
    def func_interior(*args, **kwargs):
        print("Haciendo calculo...")

        c = functionX(*args, **kwargs)

        print("Fin del calculo...")
        return c

    return func_interior


class Example:
    def __init__(self) -> None:
        self.x = 10
        self.y = 20

    @decorator_func
    def sum(self):
        return self.x + self.y

    @decorator_func
    def dif(self):
        return self.x - self.y

    @decorator_func
    def powExternal(self, base, exp):
        return (base ** exp) - self.y 


    