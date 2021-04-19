#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Create by DroidKali
import bitstring
from rflib import *

freq = input("\033[31m请输入频率：\033[0m")
start = b'\x80\x00\x00\x00\x00'
bins = input("\033[31m请输入二进制字符：\033[0m")
bytes = bitstring.BitArray(bin=bins).tobytes()
out = start + bytes

d = RfCat()
d.setFreq(int(freq))
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(2500)
d.setMaxPower()
#0=x88 1=xee f=x8e

print("\033[31m要发射的信号数据为：\033[0m")
print(out)
print("\033[32m开始发送。。。\033[0m")
d.RFxmit(out*15)
print("\033[31m发送完成。\033[0m")
