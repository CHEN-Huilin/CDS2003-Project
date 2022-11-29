"""
将首字母转换为数字并且添加到字典里
"""
def trans(dict0, num):
    """将字典的值转换为表格信息并添加"""
    name = dict0.keys()
    upperName = name.uppper()
    nameNum = []
    for i in upperName:
        nameNum.append(ord(i))
    dict0["Name Number"] = nameNum

    
    
