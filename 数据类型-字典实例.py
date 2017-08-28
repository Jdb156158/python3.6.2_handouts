#!/usr/bin/python3
 
dict = {}
dict['one'] = "1 - Helen讲师"
dict[2]     = "2 - Jason助教"
 
tinydict = {'name': 'Jason','code':1, 'site': 'http://www.z2hacademy.cn/index/'}
 
 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
