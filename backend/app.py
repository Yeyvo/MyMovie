from flask import Flask , request , jsonify , make_response
from CNNCategorisation import *
import wget
import os


basePosterURL = "https://image.tmdb.org/t/p/w370_and_h556_bestv2/"
imgFolderCacheName = "PosterCache"
app = Flask(__name__)

# @app.route('/')
# def hello_world(): 
#     return 'Hello, World'

@app.route('/categorization',methods = ['GET'])
def get():
    posterId = request.args.get("posterId")
    poster_url = basePosterURL + posterId
    poster_filename = wget.download(poster_url, out=imgFolderCacheName)
    res = evaluatePoster(model,poster_filename)
    # print('\n#####' + res)
    response =  jsonify({
          'status': 'ok',
          'data': res
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

    # return make_response(jsonify({
    #       'status': 'ok',
    #       'data': jsonify(res)
    #     }) , 200)




if __name__ == "__main__":
    if not os.path.exists(imgFolderCacheName):
        os.makedirs(imgFolderCacheName)

    app.run( debug=True, port=4996)
    app.run(host="0.0.0.0", port=8080, debug=True)
    model = getModel()
