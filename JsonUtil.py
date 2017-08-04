# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 22:47:49 2017

@author: u6035034
"""

import json


def getSchema(jsonContent):
    keys= jsonContent.keys()
    keys.sort()
    return keys