'''
Created on Jun 7, 2017

@author: 09959295800

Some miscellaneous utility functions.  
'''

import logging
import os 
import math

def create_dir_if_not_exists(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

        
def setup_logger(logger_name, log_file, log_path, level=logging.INFO):
    create_dir_if_not_exists(log_path)
    log = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    fileHandler = logging.FileHandler(log_path+log_file, mode='w')
    fileHandler.setFormatter(formatter)
    log.setLevel(level)
    log.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    log.addHandler(consoleHandler)
    return logging.getLogger(logger_name)

def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def length(v):
    return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
    if length(v1) * length(v2) == 0:
        return 0
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


