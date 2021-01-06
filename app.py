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
import Formula_Editor_RIGID_SHORT1  as jmp_RIGID_SHORT1
import json
import datetime as dt
import csv
now = dt.datetime.now()
cash_log = ['2020-12-22-INPUT777777','2020-12-22-INPUT777777','2020-12-22-INPUT777777']

################################  Setting Parameters Lists #################################### 
param_list = 'PARAM2.csv'
with open (param_list, mode = 'r') as prm_file:
    param_valid  = csv.reader(prm_file, quoting=csv.QUOTE_NONNUMERIC)
    prm_dict_mand = {rows[0]:rows[2] for rows in param_valid}
    prm_list_mand = [x for x,y in prm_dict_mand.items() if y =='M'] # mandator list
with open (param_list, mode = 'r') as prm_file:
    param_valid  = csv.reader(prm_file, quoting=csv.QUOTE_NONNUMERIC)
    prm_list = list(rows[0] for rows in param_valid) #full param list to match 
with open (param_list, mode = 'r') as prm_file:
    param_valid  = csv.reader(prm_file, quoting=csv.QUOTE_NONNUMERIC)
    prm_trnslt_list = {rows[0]:rows[1] for rows in param_valid}  #translate dict
with open (param_list, mode = 'r') as prm_file: # bring defaults list values
    param_valid  = csv.reader(prm_file, quoting=csv.QUOTE_NONNUMERIC)
    prm_defauld_list = {rows[0]:rows[3] for rows in param_valid}

##############################################################################################
global flow
flow = 1
result = ''

#  ---     Load JSON file for testing   ----
with open ("RIGID_SHORT1-json_input.json") as json_file:
    req = json.load(json_file)
    
#   is REQ_ID in int &  goes by the format     
def validate_req_int():
    num = 0
    req_id_temp =  req.get('REQ_ID') 
    req_id = [i for i in req_id_temp if i.isdigit()]
    for i in req_id:
       num = int(i) + num
    num = math.floor(num/len(req_id))
    if int(req_id[-1]) == num: #check last digit == average
        return True

#  check the number of the same REQ_ID
def validate_req_count(c):
   msg_id = (str(now.date()) +'-'+str(req.get('REQ_ID')))
   if msg_id in cash_log:
           if cash_log.count(msg_id) <= int(c):
               cash_log.append(msg_id)
               print(f'cash log : {cash_log}')
               return True
           return False
   else:
       cash_log.append(msg_id)
       return True

# joining 2 REQ_ID validation
def all_valid_check():
    if validate_req_count(8) and validate_req_int():
        global flow
        return True #'ID valid ... continue'
    else:
        flow = 0
        return False #'id_not_valid'

print (f'prm_list_mand: {prm_list_mand}')
# validate existence of mandatory! OR unknown! parameters 
def check_miss_madatory_or_extra_prm():
    for i in prm_list_mand:
        if i not in req:
            global flow
            flow = 0
            print(f'missing mandatory parameter: {i}')
            return 'error1'
        else: 
            for y in req.keys():
                if y not in prm_list:
                   flow = 0
                   print (f'message contain unknown parameter: {y}')
                   return 'error2'
                   break
                # else:
                #     pass#go to next check

# Getting json values into prm_defauld_list, replacing defaults if exist
def validate_defaults():
    for item_prm in prm_defauld_list:
        if req.get(item_prm):
            prm_defauld_list[item_prm] = req.get(item_prm)      
    # create "req" list from the updated prm_defauld_list & converting values !!! to INT/FLOAT !!!
    req_={}
    for items in prm_defauld_list:
        if items == 'DESIGN_LAYERS':
            req_[items] = float(prm_defauld_list.get(items))
        else:
            req_[items] = prm_defauld_list.get(items)
        if items == 'Assembly_Scrap':
            req_[items] = float(prm_defauld_list.get(items))
        else:
            req_[items] = prm_defauld_list.get(items)
        if items == 'FINISH_THICKNESS':
            req_[items] = float(prm_defauld_list.get(items))
        else:
            req_[items] = prm_defauld_list.get(items)
        if items == 'Laser__Holes_qty':
            req_[items] = float(prm_defauld_list.get(items))
        else:
            req_[items] = prm_defauld_list.get(items)
        if items == 'Lot_Size_PANEL':
            req_[items] = float(prm_defauld_list.get(items))
        else:
            req_[items] = prm_defauld_list.get(items)
        if items == 'Mechanical__Holes_qty':
            req_[items] = float(prm_defauld_list.get(items))
        else:
            req_[items] = prm_defauld_list.get(items)
        if items == 'X*Y_PANEL':
            req_[items] = float(prm_defauld_list.get(items))
        else:
            req_[items] = prm_defauld_list.get(items)
    return req_



# Translate Key fields > in case JMP file contain variables with backspaces (as "DESIGN LAYERS") 
def translate_keys(req_):
    req_2= {}
    for  x in req_.keys():
        for n in prm_trnslt_list.keys():
            if x == n:
                req_2[prm_trnslt_list.get(n)] = req_.get(n)
                #print (x, n )
    return req_2


# req_ = validate_defaults()
# print(f'\n validate_d e f a u l t s >> printing new req_: {req_}\n')

# del prm_defauld_list
# print('------@@@------')
# print(f' *** After tranlation: {translate_keys(req_)}')
########################################################################


#print(check_miss_madatory_or_extra_prm())     
    

#print(jmp.score(req,{}))
#print(jmp_RIGID_SHORT1.score(translate_keys(req_),{}))


#**********************EXEC PLAN*****************************
print('**********************EXEC PLAN*****************************')
try: 
    print(all_valid_check())
    while flow == 1:
        print(check_miss_madatory_or_extra_prm())
        while flow == 1:
            req_ = validate_defaults()
            while flow == 1:
                req_2 = translate_keys(req_)
                print(req_2)
                result  = jmp_RIGID_SHORT1.score(req_2,{})
                print('\n--------------Result-------------')
                print(result)
                flow = 0
except  AssertionError as error: 
    print(error)
    result ='somrthing went wrong - {error}'
    pass
finally:
    pass 
        
#************************************************************
'''
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


