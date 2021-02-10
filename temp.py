
#from pkg import  *
__import__('pkg.Formula_Editor_Rigid_Flex_Flip1')
__import__('pkg.Formula_Editor_Rigid_Flex_Flip4')

# ---              exec steps
json_mod_name =''
if not validate_req_int():
    msg = "wrong ID format"
    jmp_result = 999
    jmp_module = '999'
else: 
    if not validate_req_count(10):
            msg = f'more then {c} requests'
            jmp_result = 999
            jmp_module = '999'
    else:
        if validate_module_vs_json_and_param() not True:
            msg = validate_module_vs_json_and_param()
            jmp_result = 999
            jmp_module = '999'
        else:
            mod_ = req.get('JMP_MOD')
            selected_module = __import__(mod_)
            msg = 'calc executed'
            jmp_result = selected_module.score(req,{})
            jmp_module = selected_module
                     
    
    
    
response =             {
                           "REQ_ID" : req.get("REQ_ID"),
                           "message" : msg ,
                           "JMP_Result" : jmp_result,
                           "JMP_Module" : jmp_module
                       }
res= make_response(jsonify(response), 200)
return res
