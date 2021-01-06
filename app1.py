''' 
*************************************************************************************************************************************
                                          Functionality NOTES 
"REQ_ID": format include digits. no length limit, when the last digit is the average of all the digits - rounded down.
        in case the REQ_ID, from some reason does include non-digit characters, the base format still applies, 
        the program will consider only the digits in the string for the calculation
"validate_req_count": each request need to have different "REQ_ID", the program will not accept more then (c =10) calls with the same 
        "REQ_ID" on the same date (validation list is stored in the program memory)
"check_miss_madatory_or_extra_prm":  checking that all Mandatory param exit in the message, otherwise response with> 
        "missing mandatory parameter:[PARAM_ID]" 
        checking that message doesn’t contain unknown parameters ,otherwise response with>
        "message contain unknown parameter: [PARAM_ID]"
"validate_defaults":  for the program to work well, all parameters need to be set with values, if message received without some parameters
        the program will set the defaults  values for these missing parameters, all required parameters are maintained
        in the "PARAM.csv" file
*************************************************************************************************************************************
'''
from flask import Flask, request, jsonify, make_response
import math
import json
import datetime as dt
import csv
now = dt.datetime.now()
cash_log = ['2021-01-06-B7777777','2021-01-06-B7777777','2021-01-06-B7777777']
# ---                   listingd the JMP modules [v_module]
with open ('JMP_Active_Modules.csv', mode = 'r') as moduls_list:
    modules_ = csv.reader(moduls_list)
    v_module = list(rows[0] for rows in modules_)
print(v_module)


# ---              importing all modules according to the list 
modules = []
modules_list = []
for x in range (len(v_module)):
    try:
        
        modules.append(__import__(v_module[x])) 
        print (f'Successfully imported {v_module[x]}')
        modules_list.append(v_module[x])
        module_name = v_module[x]
        #q= modules[x].getInputMetadata()
        #print(q) 
    except ImportError:
        error_msg = f'error importing {v_module[x]}'
        print(error_msg)
print(f'\n ********* modules: {modules}\n')


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
            #print(modules_list[int(x)])
            if req.get('JMP_MOD') == modules_list[int(x)]:
                module_param_dict = modules[x].getInputMetadata()
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
result  = Formula_Editor_Rigid_Flex_04_01_2021.score(req,{})
print(result)
'''
result = ''

    

#print(jmp.score(req,{}))
#print(jmp_RIGID_SHORT1.score(translate_keys(req_),{}))


#**********************EXEC PLAN*****************************
print('**********************EXEC PLAN*****************************')
try: 
#(all_valid_check())
#(check_miss_madatory_or_extra_prm())
#req_ = validate_defaults()
#req_2 = translate_keys(req_)
    result  = jmp_RIGID_SHORT1.score(req_2,{})
    print('\n--------------Result-------------')
    print(result)
except  AssertionError as error: 
    result = f'somrthing went wrong - {error}'
    print(result)

    pass
finally:
    pass 
        
#************************************************************

print('Starting .....')
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
            global req, req_2, req_3,result
            req = request.get_json()
            if all_valid_check():
                check2= check_miss_madatory_or_extra_prm()
                if check2 != 'False1' or check2 !='False2':
                    validate_defaults()
                    req_2 = translate_keys(req_)
                    result  = jmp_RIGID_SHORT1.score(req_2,{})
                    #response step----------------
                    if req.get("EXISTS_LASER_DRILL") == "YES"  :
                        
                            response = {
                                "REQ_ID" : req.get("REQ_ID"),
                                "EXISTS_LASER_DRILL" : req.get("EXISTS_LASER_DRILL"),
                                "JMP_Result" : result ,#jmp.score(req,{}),
                                "JMP_Formula" : "Score1_RIGID_SHORT1",
                                "FINISH_THICKNESS" : req_2.get("FINISH THICKNESS")
                            }
                            res= make_response(jsonify(response), 200)
                            return res  #"json test 1", 200
                    else:
                             response = {
                                "REQ_ID" : req.get("REQ_ID"),
                                "DESIGN_LAYERS" : req.get("DESIGN_LAYERS"),
                                "EXISTS_LASER_DRILL" : req.get("EXISTS_LASER_DRILL"),
                                    "JMP_Result" : 999,#jmp.score(req,{}),
                                "JMP_Formula" : "Score2_NO_LASE_DRILL"
                             }
                             res= make_response(jsonify(response), 200)
                             return res  #"json test 1", 200
                elif check2 == 'False1':
                    res = make_response(jsonify({"1.Message":f'missing mandatory parameter: {i}',}), 405)
                    return res  #'no json recieved', 400
                elif check2 == 'False2':
                    res = make_response(jsonify({"1.Message": f'message contain unknown parameter: {y}',}), 405)
                    return res  #'no json recieved', 400
                else : 
                    pass

            else:
                res = make_response(jsonify({"1.Message":"id_not_valid","2.Description" : "id format issue, or repetitive req.",}), 405)
                return res  #'no json recieved', 400
            
    else:
        res = make_response(jsonify({"1.Message":"No json recieved","2.Description" : "Message not in recognized json format",}), 400)
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


