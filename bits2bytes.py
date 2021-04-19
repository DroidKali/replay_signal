#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Create by DroidKali
import bitstring

start = b'\x80\x00\x00\x00\x00'
bins = input("\033[31m请输入二进制字符：\033[0m")
bytes = bitstring.BitArray(bin=bins).tobytes()
print("\033[34m转换后的Hex数据为：\033[0m")
print(bytes)
print("\033[35m最终输出为: \033[0m")
print(start + bytes)
