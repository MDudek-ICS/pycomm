import sys
import time
sys.path.append('../')

from pycomm.ab_comm.slc import Driver as SlcDriver
import logging


if __name__ == '__main__':
    logging.basicConfig(
        format="%(levelname)-10s %(message)s",
        level=logging.DEBUG
    )
    c = SlcDriver()
    if c.open('localhost'):
        print('connected')
        print(c.read_tag('F11:0'))
        print(c.read_tag('F11:1'))
        time.sleep(1)
        print(c.read_tag('F11:1'))
        print(c.read_tag('F11:0'))
