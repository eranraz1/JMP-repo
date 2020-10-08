from flask import Flask, request, jsonify, make_response
import Formula_Editor as jmp 
import Formula_Editor2 as jmp2 
import json


#*********************************************************

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if (request.method=='POST'):
        some_json = request.get_json()
        return jsonify ({'you sent': some_json}), 201
    else:
        return jsonify({"message":"Hi - that's not a valid path"})
    
@app.route("/about") 
def about():
    return "<h4 style = 'color: grey;' >TBD - JMP program details...</h4>"

@app.route('/jmp/', methods=['GET','POST'])
def json():
    if request.is_json: 
        req = request.get_json()
        print (type(req))
        print(req)
        #response step----------------
        print(jmp.score(req,{}))
        if req.get("EXISTS_LASER_DRILL") == "YES"  :    
                response = {
                    "PID" : req.get("PID"),
                    "DESIGN_LAYERS" : req.get("DESIGN_LAYERS"),
                    "EXISTS_LASER_DRILL" : req.get("EXISTS_LASER_DRILL"),
                    "JMP_Result" : jmp.score(req,{}),
                    "JMP_Formula" : "Score 1"
                }
                res= make_response(jsonify(response), 200)
                return res  #"json test 1", 200
        else:
                 response = {
                    "PID" : req.get("PID"),
                    "DESIGN_LAYERS" : req.get("DESIGN_LAYERS"),
                    "EXISTS_LASER_DRILL" : req.get("EXISTS_LASER_DRILL"),
                    "JMP_Result" : jmp2.score2(req,{}),
                    "JMP_Formula" : "Score 2"
                 }
                 res= make_response(jsonify(response), 200)
                 return res  #"json test 1", 200
    else:
        res = make_response(jsonify({"message":"no json recieved"}), 400)
        return res  #'no json recieved', 400


if __name__ == '__main__':  
    app.run(debug=True)
    

    #https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
    # C:\>cd/d C:\Users\eranra\Documents\PY\Scoring\Test_inv\
#******************************************************************