from libs import *
import time


def test():
    mega = Generator()

    meg = Connection(17,27,22, "ArduinoGoBRRRRR")
    mega.addTokens([POWERON_STEPPERS,0x0B])

    mega.deliverStockpile(meg)
    mega.dumpStockpile()

    time.sleep(2)

    mega.addTokens([0x14])
    mega.deliverStockpile(meg)

test()
