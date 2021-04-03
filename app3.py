''' 
*************************************************************************************************************************************
                                          Functionality NOTES - Ver 2.2.0
"validate_req_count": each request need to have different "REQ_ID", the program will not accept more then (c =10) calls with the same 
        "REQ_ID" on the same date (validation list is stored in the program memory)
*************************************************************************************************************************************
'''

from flask import Flask, request, jsonify, make_response
import math, glob, csv
import json
import datetime as dt
from icecream import ic
import os
jmp_ver = '2.2.0'
# ---              importing JMP modules from 'pkg' folder & set :'modules_list'
arr = os.listdir("/JMP.v2.2/pkg/")
modules_list = []
for i in arr:
    if i.startswith('JMP'):
        mod = str(i[:-3])
    print(mod)
    modules_list.append(str(i[:-3]))
print(modules_list)
__import__('C:\Temp\JMP_TEMP')
'''
for i in modules_list:
    try:
        __import__(f'pkg.{i}')
        print (f'Successfully imported {i}')
    except ImportError:
        error_msg = f'error importing {i}'
        print(error_msg)
print('\n')
print (modules_list)
print('\n')
now = dt.datetime.now()
cash_log = ['2021-01-06-B7777777','2021-01-06-B7777777','2021-01-06-B7777777']
'''