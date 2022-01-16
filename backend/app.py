from urllib import response
from flask import Flask , request , jsonify , make_response
import CNNCategorisation as cnnCateg
import Recomovie as treeReco
import wget
import os
import shutil


basePosterURL = "https://image.tmdb.org/t/p/w370_and_h556_bestv2/"
imgFolderCacheName = "PosterCache"
app = Flask(__name__)


@app.route('/categorization',methods = ['GET'])
def get():
    posterId = request.args.get("posterId")
    poster_url = basePosterURL + posterId
    poster_filename = wget.download(poster_url, out=imgFolderCacheName)
    res = cnnCateg.evaluatePoster(model,poster_filename)
    response =  jsonify({
          'status': 'ok',
          'data': res
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


@app.route('/recomendation')
def getRecommendation():
    response = jsonify(Tree)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


if __name__ == "__main__":
    if os.path.exists(imgFolderCacheName) :
        shutil.rmtree(imgFolderCacheName)
    os.makedirs(imgFolderCacheName)
    
    print("\nCNN Model Importation\n")    
    model = cnnCateg.getModel()
    print("\nCNN Model Importation Done\n")    

    print("\nDecision Model Importation\n")    
    Tree = treeReco.getModel()
    print("\nDecision Model Importation Done\n")    

    app.run( debug=True, port=4996)
    # app.run(host="0.0.0.0", port=8080, debug=True)
