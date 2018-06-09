#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging.handlers
import logging,os
 
class Logger:
  def __init__(self, path = './test.log',clevel = logging.DEBUG,Flevel = logging.DEBUG):
    self.logger = logging.getLogger(path)
    self.logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')
    
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    sh.setLevel(clevel)
    
    fh = logging.handlers.RotatingFileHandler(path, maxBytes=10*1024, backupCount=50)
    fh.encoding="utf-8"
    fh.setFormatter(fmt)
    fh.setLevel(Flevel)
    self.logger.addHandler(sh)
    self.logger.addHandler(fh)
 
  def debug(self,message):
    self.logger.debug(message)
   
  def info(self,message):
    self.logger.info(message)
   
  def war(self,message):
    self.logger.warn(message)
   
  def error(self,message):
    self.logger.error(message)
   
  def cri(self,message):
    self.logger.critical(message)
 
def test():
  log_test = Logger('./test.log',logging.DEBUG,logging.DEBUG)
  log_test.debug('test log')

if __name__ =='__main__':
  test()