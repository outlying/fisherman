import logging

from finder.finder import ThresholdFinder
from fisherman import Fisherman
from gui_io.operator import Operator
from observer.observer import StandardObserver

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def run():

    operator = Operator.create()

    fisherman = Fisherman(
        operator=operator,
        finder=ThresholdFinder(),
        observer=StandardObserver(operator)
    )
    while True:
        fisherman.fish()

if __name__ == '__main__':
    run()