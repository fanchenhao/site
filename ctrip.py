#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:16:59 2021

@author: ideal
"""

import requests
from bs4 import BeautifulSoup

url = "https://flights.ctrip.com/itinerary/oneway/TNA-BJS?date=2021-02-18"

headers = {'user-agent':\
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'\
               }


reqs = requests.get(url, headers = headers)

soup = BeautifulSoup(reqs.text, 'lxml')