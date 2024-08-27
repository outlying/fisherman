from finder.finder import ThresholdFinder
from fisherman import Fisherman
from gui_io.operator import Operator
from observer.observer import StandardObserver


def run():

    operator = Operator.create()

    fisherman = Fisherman(
        operator=operator,
        finder=ThresholdFinder(),
        observer=StandardObserver(operator)
    )
    fisherman.fish()

if __name__ == '__main__':
    run()