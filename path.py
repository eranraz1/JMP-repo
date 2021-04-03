import os
import glob
# a = glob.glob("pkg/JMP_*.py")
# modules_list = [i.strip('pkg\\*.py') for i in a]
# print((modules_list))

# arr = os.listdir("/JMP.v2.2/JSON/")
# print(arr)

arr = os.listdir("/JMP.v2.2/pkg/")
for i in arr:
    if i.startswith('JMP'):
        mod = str(i[:-3])
        print(mod)
        try:
            
            __import__(f'pkg\\{mod}')
            print (f'Successfully imported {mod}')
        except ImportError:
            print(f'error importing {mod}')

# for i in modules_list:
#     try:
#         __import__(f'pkg.{i}')
#         print (f'Successfully imported {i}')
#     except ImportError:
#         error_msg = f'error importing {i}'
#         print(error_msg)
# print('\n')
