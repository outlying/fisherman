from gui_io.operator import Operator


class Fisherman:

    def __init__(self, operator: Operator):
        self.operator = operator
        pass

    def fish(self):
        see_before_throw = self.operator.see()
        self.operator.throw()
        self.operator.wait(2)
        see_after_throw = self.operator.see()

        see_before_throw.save("0before.png")
        see_after_throw.save("1after.png")
        pass