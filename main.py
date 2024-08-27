from finder.finder import ThresholdFinder, TemplateFinder
from fisherman import Fisherman
from gui_io.operator import Operator


def run():

    fisherman = Fisherman(
        operator=Operator.create(),
        finder=ThresholdFinder()
    )
    fisherman.fish()

if __name__ == '__main__':
    run()