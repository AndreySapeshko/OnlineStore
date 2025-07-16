class ReportByCreateObject:
    """ Класс миксин при создании объектов его наследников выводится строка по
    шаблону: ИмяКласса(значение аргумента1, значение аргумента2, ... значение аргументаN) """

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        args = ''
        for arg in self.__dict__.values():
            if len(args) == 0:
                args = arg
            else:
                args += ', ' + str(arg)
        message = f'{self.__class__.__name__}({args})'
        return message
