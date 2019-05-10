#!/usr/bin/env python
# coding=UTF-8
'''
@Description: S
@Author: StaURL
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-05-09 17:28:25
@LastEditTime: 2019-05-10 16:18:36
'''
from c11_1_name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
