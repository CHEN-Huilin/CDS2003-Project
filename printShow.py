# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 23:06:59 2022
@author: shengqigui
"""
"""用于将所有信息按照表格的形式整齐的打印出来"""

import sys 
from prettytable import PrettyTable
reload(sys)
sys.setdefaulencoding('utf-8')

table = PrettyTable(["Name", "Phone number", "Address"])

def addDic(dict0, num):
    """将字典的值转换为表格信息并添加"""
    name = None
    for i in dict0:
        name = i
    inDict = dict0[name]
    phoneNum = inDict["Phone"]
    address = inDict["Address"]
    table.add_row([num, name, phoneNum, address])

def editTable(head):
    """遍历LinkedList+添加"""
    temp = head
    while temp != None:
        addDic(temp.next)
        temp = temp.next

def showSortedFrormat():
    """打印表格"""
    print(table)


