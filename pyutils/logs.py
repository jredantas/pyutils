#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:01:36 2017

@author: 09959295800
"""
import logging
from pyutils.misc import create_dir_if_not_exists
import time

def setup_logger(logger_name, log_file, log_path, level=logging.INFO):
    create_dir_if_not_exists(log_path)
    individual_log = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    individual_log.setLevel(level)
    individual_log.addHandler(fileHandler)
    return logging.getLogger(logger_name)
    
def setup_main_log(log_path,  level=logging.INFO):
    create_dir_if_not_exists(log_path)
    logging.basicConfig(level=logging.getLevelName(level))
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    fileHandler = logging.FileHandler("{0}/{1}.log".format(log_path, time.strftime("%Y%m%d%H%M%S")))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    
def close_logs():
        logging.shutdown()

def log_all(logger,level,message):
    level = logging.getLevelName(level)
    for i in logger.keys():
        logger[i].log(level,message) 
