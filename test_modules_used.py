import inspect 
import importlib as implib


mod = implib.import_module( "app1" )
for i in inspect.getmembers(mod, inspect.ismodule ):
    print (i)
print('***********************')    
    
    
# import glob
# a = glob.glob("pkg/Formula_Editor_*.py")
# modules_list= [i.strip('pkg\\*.py') for i in a]
# del a
# for i in modules_list:
#     try:
#         __import__(f'pkg.{i}')
#         print (f'Successfully imported {i}')
#     except ImportError:
#         error_msg = f'error importing {i}'
#         print(error_msg)
