# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 17:20:20 2016

@author: u6035034
"""

import logging

logger =logging.getLogger()


def init_logger():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    logger.addHandler(ch)