''' 
*************************************************************************************************************************************
                                          Functionality NOTES - Ver 2.0.0
"REQ_ID": format include digits. no length limit, when the last digit is the average of all the digits - rounded down.
        in case the REQ_ID, from some reason does include non-digit characters, the base format still applies, 
        the program will consider only the digits in the string for the calculation
"validate_req_count": each request need to have different "REQ_ID", the program will not accept more then (c =10) calls with the same 
        "REQ_ID" on the same date (validation list is stored in the program memory)
*************************************************************************************************************************************
'''

from flask import Flask, request, jsonify, make_response
import math, glob, csv
import json
import datetime as dt
# ---              importing JMP modules from 'pkg' folder & set :'modules_list'
a = glob.glob("pkg/Formula_Editor_*.py")
modules_list = [i.strip('pkg\\*.py') for i in a]
del a
for i in modules_list:
    try:
        __import__(f'pkg.{i}')
        print (f'Successfully imported {i}')
    except ImportError:
        error_msg = f'error importing {i}'
        print(error_msg)
print('\n')
print (modules_list[0])
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
def validate_module_vs_json_and_param():
    global json_mod_name
    json_mod_name = req.get('JMP_MOD') 
    if json_mod_name in modules_list:
        for x in range(len(modules_list)):
            if req.get('JMP_MOD') == modules_list[int(x)]:
                module_param_dict = __import__(modules_list[int(x)]).getInputMetadata()
                for key_module in module_param_dict.keys():
                    if key_module in req.keys():
                        continue
                    else:
                        result = f'"missing_param" : "{key_module}" '
                        return result
                return True            
    else:
        result = f'"Module not listed" : "{json_mod_name}"'
        return result


def json():
    if True:#request.is_json:
        #req = request.get_json()
        # ---              exec steps

        if not validate_req_int():
            msg = "wrong ID format"
            jmp_result = 999
            jmp_module = '999'
        else: 
            if not validate_req_count(10):
                    msg = f'too many similar requests'
                    jmp_result = 999
                    jmp_module = '999'
            else:
                if not validate_module_vs_json_and_param() :
                    msg = validate_module_vs_json_and_param()
                    jmp_result = 999
                    jmp_module = '999'
                else:
                    mod_ = req.get('JMP_MOD')
                    selected_module = __import__(mod_)
                    msg = 'calc executed'
                    jmp_result = selected_module.score(req,{})
                    jmp_module = selected_module
          
       # print (f'!!!module:{jmp_module} , score: {jmp_result}, msg: {msg}, REQ_ID:{req.get("REQ_ID")}')                   
                            
        response = {
            "REQ_ID" : req.get("REQ_ID"),
            "JMP_Result" : jmp_result,
            "JMP_Module" : jmp_module,
            "Message" : msg
            }
        res = response
        # res= make_response(jsonify(response), 200) # todo : if result = 999, post code 405
        return res  # return response as JSON
            
    else:
        res = 'somthong else'#make_response(jsonify({"1.Message":"No json recieved","2.Description": "Message not in recognized json format",}), 400)
        return res  #'no js
print('@@@@@@@@@@@@@@@@@@@@@@@@\n')
print(json())


#************************************************************
'''
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
def json():
    if request.is_json:
        req = request.get_json()
        # ---              exec steps
        print(' ---              exec steps            --- ')
        json_mod_name =''
        if not validate_req_int():
            msg = "wrong ID format"
            jmp_result = 999
            jmp_module = '999'
        else: 
            if not validate_req_count(10):
                    msg = f'too many similar requests'
                    jmp_result = 999
                    jmp_module = '999'
            else:
                if not validate_module_vs_json_and_param() :
                    msg = validate_module_vs_json_and_param()
                    jmp_result = 999
                    jmp_module = '999'
                else:
                    mod_ = req.get('JMP_MOD')
                    selected_module = __import__(mod_)
                    msg = 'calc executed'
                    jmp_result = selected_module.score(req,{})
                    jmp_module = selected_module
          
        print (f'!!!module:{jmp_module} , score: {jmp_result}, msg: {msg}, REQ_ID:{req.get("REQ_ID")}')                   
                            
        response = {
            "REQ_ID" : req.get("REQ_ID"),
            "JMP_Result" : jmp_result,
            "JMP_Module" : jmp_module,
            "Message" : msg
            }
        res= make_response(jsonify(response), 200) # todo : if result = 999, post code 405
        return res  # return response as JSON
            
    else:
        res = make_response(jsonify({"1.Message":"No json recieved","2.Description"
                                     : "Message not in recognized json format",}), 400)
        return res  #'no json recieved', 400


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


