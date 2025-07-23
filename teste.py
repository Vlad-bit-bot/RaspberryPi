from Generator import Generator
from Connection import Connection
from commands import *
import time

mega = Generator()
meg = Connection(17,27,22, "ArduinoGoBRRRRR")

mega.addTokens([POWERON_STEPPERS,0x0B])

mega.signalStockpile(meg)
mega.dumpStockpile()

time.sleep(2)

mega.addTokens([0x14])
mega.signalStockpile(meg)
