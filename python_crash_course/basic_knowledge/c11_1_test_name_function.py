#!/usr/bin/env python
# coding=UTF-8
'''
@Description: S
@Author: StaURL
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-05-09 17:50:22
@LastEditTime: 2019-05-09 17:55:28
'''
import unittest 
from name_function import get_formatted_name 
class NamesTestCase(unittest.TestCase):
     """测试name_function.py""" 
    def test_first_last_name(self): 
        """能够正确地处理像Janis Joplin这样的姓名吗？""" 
        formatted_name = get_formatted_name('janis', 'joplin') 
        self.assertEqual(formatted_name, 'Janis Joplin') 
    unittest.main() 
