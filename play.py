#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:47:25 2021

@author: ideal
"""

from tts import tts_main


context = input("please input some words:").encoding("utf-8")


tts_main(context)

