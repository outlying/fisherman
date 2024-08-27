from finder.finder import StandardFinder, TemplateFinder
from fisherman import Fisherman
from gui_io.operator import Operator


def run():

    fisherman = Fisherman(
        operator=Operator.create(),
        finder=TemplateFinder()
    )
    fisherman.fish()

if __name__ == '__main__':
    run()