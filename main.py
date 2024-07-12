import warnings
warnings.filterwarnings("ignore")
import os
from flask import Flask,request,jsonify
from uploadpdf import vector
from askquestion import ask_question
from checkdoc import checkdoc
from generatequestions import genques
from generateimage import genimage
from PIL import Image
import requests
app = Flask(__name__)

@app.route('/question', methods=["POST"])
def question():
    uuid = request.json['uuid']
    query = request.json['query']
    answer=ask_question(str(uuid),str(query))
    print(answer)
    #return jsonify(answer)
    return jsonify({"result" :answer})


@app.route('/uploadpdf', methods=["POST"])
def uploadpdf():
    pdf = request.json['pdf']
    uuid = request.json['uuid']
    persist_directory=vector(str(uuid),str(pdf))
    print(persist_directory)
    #return jsonify(persist_directory)
    return jsonify({"result" :persist_directory})


@app.route('/checkdoc', methods=["POST"])
def checkpdf():
    uuid = request.json['uuid']
    if checkdoc(str(uuid)):
         return jsonify({"status": True,}), 200
         return "Success", 201
        #return jsonify({"exists" :uuid})
    else:
         return jsonify({"status": False,}), 200
    
@app.route('/generatequestions', methods=["POST"])
def generatequestion():
    uuid = request.json['uuid']
    count = request.json['count']
    questionaire=genques(str(uuid),str(count))
    print(questionaire)
    #return jsonify(answer)
    return jsonify({"result" :questionaire})

@app.route('/genimg', methods=["POST"])
def prompt():
    img = request.json['img']
    img = "360 degree view of " + str(img)
    imgurl=genimage(img)
    print(img)
    #return jsonify(answer)
    response = requests.get(imgurl) 
    # using the Image module from PIL library to view the image 
    return jsonify({"image url" :imgurl})





if __name__ == '__main__':
	app.run()

