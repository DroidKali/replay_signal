#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Create by DroidKali
import bitstring
import argparse
from rflib import *

parser = argparse.ArgumentParser(description='A python script to sent replay signal.')
parser.add_argument('-f', action="store", default="433920000", dest="baseFreq",help='Specify the target frequency to transmit on, default is 433920000.',type=int)
parser.add_argument('-b', action="store", dest="bitstring",help='Specify the bits from RTL_433 raw code.',type=str)
parser.add_argument('-r', action="store", dest="baudRate", default="2500", help='Specify the baudrate of the signal, default is 2500.',type=int)
results = parser.parse_args()
freq = results.baseFreq
start = b'\x80\x00\x00\x00\x00'
bits= results.bitstring
baudRate = results.baudRate
bs = ''
for s in bits:
    if s == '1':
        bs += '1110'
    else:
        bs += '1000'

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
d.RFxmit(out*15)
print("\033[31m发送完成。\033[0m")
