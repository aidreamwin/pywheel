# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")
from BinLog.log import Logger

# Logger('./test.log',logging.DEBUG,logging.DEBUG)
x = Logger()
x.debug("hello1")
x.debug("hello2")
x.debug("hello3")
x.debug("hello4")
x.debug("hello5")
x.debug("hello6")
