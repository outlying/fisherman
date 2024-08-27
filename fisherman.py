from PIL import Image

from finder.finder import Finder
from gui_io.operator import Operator


class Fisherman:

    def __init__(self, operator: Operator, finder: Finder):
        self.operator = operator
        self.finder = finder
        pass

    def fish(self):
        # see_before_throw = self.operator.see()
        # self.operator.throw()
        # self.operator.wait(2)
        # see_after_throw = self.operator.see()
        #
        # see_before_throw.save("tmp/0before.png")
        # see_after_throw.save("tmp/1after.png")

        see_before_throw = Image.open("tmp/0before.png")
        see_after_throw = Image.open("tmp/1after.png")

        self.finder.find_bobber(see_before_throw, see_after_throw)
        pass