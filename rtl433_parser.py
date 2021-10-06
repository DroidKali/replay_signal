#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Create by DroidKali
import bitstring
import argparse
from rflib import *
banner='''
\033[31m ____           _ _         _   _            _             \033[0m
\033[32m|  _ \ __ _  __| (_) ___   | | | | __ _  ___| | _____ _ __ \033[0m
\033[33m| |_) / _` |/ _` | |/ _ \  | |_| |/ _` |/ __| |/ / _ \ '__|\033[0m
\033[34m|  _ < (_| | (_| | | (_) | |  _  | (_| | (__|   <  __/ |   \033[0m
\033[35m|_| \_\__,_|\__,_|_|\___/  |_| |_|\__,_|\___|_|\_\___|_|   \033[0m
'''
print(banner)
print("\033[32mauthor: \033[31m记忆里的纯真\033[0m")
print("\033[34mversion: \033[35m1.0\n\033[0m")

parser = argparse.ArgumentParser(description='\033[34mA python script to sent replay signal.\033[33m')
parser.add_argument('-f', action="store", default="433920000", dest="baseFreq",help='Specify the target frequency to transmit on, default is 433920000.',type=float)
parser.add_argument('-b', action="store", dest="bitstring",help='Specify the bits from RTL_433 raw code.',type=str)
parser.add_argument('-r', action="store", dest="baudRate", default="2500", help='Specify the baudrate of the signal, default is 2500.',type=int)
parser.add_argument('-x', action="store", dest="multiply", default="15", help='Specify the multiply of the signal, default is 15.',type=int)

results = parser.parse_args()
freq = results.baseFreq
bits= results.bitstring
baudRate = results.baudRate
multiply = results.multiply
bs = ''
for s in bits:
    if s == '1':
        bs += '1110'
    else:
        bs += '1000'

start = b'\x80\x00\x00\x00\x00'
bytes = bitstring.BitArray(bin=bs).tobytes()
out = start + bytes

d = RfCat()
d.setFreq(freq)
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(baudRate)
d.setMaxPower()
#0=x88 1=xee f=x8e

print("\033[31m要发射的信号数据为：\033[0m")
print(out)
print("\033[32m开始发送。。。\033[0m")
d.RFxmit(out*multiply)
print("\033[31m发送完成。\033[0m")
