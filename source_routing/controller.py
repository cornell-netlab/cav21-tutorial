from petr4 import App
from topo import *
from petr4.runtime import *
from tornado.ioloop import *
from struct import pack
import binascii
from collections import defaultdict
from packet_utils import *


class SourceRouting(App):
    
    def switch_up(self,switch,ports):
        print(f"{switch} is up!")
        return
        
    def __init__(self, port=9000):
        super().__init__(port)

app = SourceRouting()
app.start()
