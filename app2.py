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
jmp_ver = '2.2.1'
# ---              importing JMP modules from 'pkg' folder & set :'modules_list'
a = glob.glob("pkg/JMP_*.py")
modules_list = [i.strip('pkg/*.py') for i in a]
del a
for i in modules_list:
    try:
        __import__(f'pkg.{i}')
        print (f'Successfully imported {i}')
    except ImportError:
        error_msg = f'error importing {i}'
        print(error_msg)
print('\n')
#print (modules_list[1])
print('\n')
now = dt.datetime.now()
cash_log = ['2021-01-06-B7777777','2021-01-06-B7777777','2021-01-06-B7777777']

# # ---                   listingd the JMP modules [v_module]
# with open ('JMP_Active_Modules.csv', mode = 'r') as moduls_list:
#     modules_ = csv.reader(moduls_list)
#     v_module = list(rows[0] for rows in modules_)
# print(v_module)


# ---              loading JSON request 
with open (f'JSON\json_input_example.json') as json_file:
    req = json.load (json_file)
print('\n--------- print req file-values ----------\n')
print(req)


# ---              check REQ_ID   goes by the format - check last digit == average     
def validate_req_int():
    num = 0
    req_id_temp =  req.get('REQ_ID') 
    req_id = [i for i in req_id_temp if i.isdigit()]
    for i in req_id:
       num = int(i) + num
    num = math.floor(num/len(req_id))
    if int(req_id[-1]) == num: #check last digit == average
        return True
    return False
#print(validate_req_int()) #> True


# ---              check # of the same REQ_ID for date 
def validate_req_count(c):
   msg_id = (str(now.date()) +'-'+str(req.get('REQ_ID')))
   if msg_id in cash_log:
           if cash_log.count(msg_id) <= int(c):
               cash_log.append(msg_id)
               print(f'cash log : {cash_log}')
               return True
           return False #> will exit with error
   else:
       cash_log.append(msg_id)
       return True


# ---              checking  module  exist vs (JSON), if so - checking all param exist
json_mod_name =''
def validate_module_vs_json_and_param(req):
    global json_mod_name
    json_mod_name = req.get('JMP_MOD') 
    if json_mod_name in modules_list:
        for x in range(len(modules_list)):
            if req.get('JMP_MOD') == modules_list[int(x)]:
                module_param_dict = __import__(modules_list[int(x)]).getInputMetadata()
                for key_module in module_param_dict.keys():
                    if key_module in req.keys():
                        result = True
                    else:
                        result = f'"missing_param" : "{key_module} requiered for module {json_mod_name}" '
                        return result            
    else:
        result = f'"Module not listed" : "{json_mod_name}"'
    return result


def json(req):
    if True:#request.is_json:
        if validate_module_vs_json_and_param(req) == True:
            mod_ = req.get('JMP_MOD')
            selected_module = __import__(mod_)
            msg = 'calc executed'
            jmp_result = selected_module.score(req,{})
            jmp_module = selected_module
        else:
            msg = validate_module_vs_json_and_param()
            jmp_result = 999999
            jmp_module = '999999'
                           
                            
        response = {
            "REQ_ID" : req.get("REQ_ID"),
            "JMP_Result" : jmp_result,
            "JMP_Module" : jmp_module,
            "Message" : msg
            }
        res = response
    
    else:
        res = 'somthong else'#make_response(jsonify({"1.Message":"No json recieved","2.Description": "Message not in recognized json format",}), 400)
    return res  #'no js
print('\n--------- print jmp function ----------\n')
#print (validate_module_vs_json_and_param())
print(json(req))


#************************************************************
'''                        END OF TEST > STARTING FLASK  APP 
print('Starting Flask.....')
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if (request.method=='POST'):
        some_json = request.get_json()
        return jsonify ({'you sent': some_json}), 201
    else:
        return jsonify({"message":"Hi - that's not a valid path"})

@app.route('/jmp/', methods=['GET','POST'])
def json_ws():
    if request.is_json:
        req_ws = request.get_json()
        # ---              exec steps
        if validate_module_vs_json_and_param(req_ws) == True:
                    mod_ = req_ws.get('JMP_MOD')
                    selected_module = __import__(mod_)
                    msg = 'calc executed'
                    jmp_result = selected_module.score(req_ws,{})
                    jmp_module = selected_module
        elif validate_module_vs_json_and_param(req_ws) != True:
            msg = validate_module_vs_json_and_param(req_ws)
            jmp_result = 999999
            jmp_module = '999999'
        
        response = {
                   "REQ_ID" : req_ws.get("REQ_ID"),
                   "JMP_Result" : jmp_result,
                   "JMP_Module" : str(jmp_module),
                   "Message" : msg
                   }
        res = make_response(jsonify(response), 200) # response
    else:
        res = make_response(jsonify({"1. Message":"No json recieved","2. Description": "Message not in recognized json format",}), 400)
    return res  # return response as JSON  


@app.route('/jmp/module', methods=['GET','POST'])
def get_module():
    resp = make_response(jsonify({"App Ver": f"{jmp_ver}","Module list":f"{modules_list}"}), 200)
    return resp  # return response as JSON          
################################################################

if __name__ == '__main__':  
    app.run(debug=True)
'''
    # curl -H "Content-Type: Application/json" - X POST -d '{"name":"Eran", "address": "Raz"}' http://127.0.0.1:5000/a
    # D:\PY>python flask_script.py mkjkw
    #https://www.youtube.com/watch?v=VzBtoA_8qm4
    #https://www.youtube.com/watch?v=YFBRVJPhDGY  ### config UBUNTU for Flask 
    #https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
    # C:\>cd/d C:\Users\eranra\Documents\PY\Scoring\Test_inv\
#******************************************************************


