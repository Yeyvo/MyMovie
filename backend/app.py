from flask import Flask , request , jsonify , make_response
from CNNCategorisation import *
import wget
import os
import shutil



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



# tree Structure
# tree = {
#     question = "kdzhidzhdndz?"
#     TrueChild = {
#         question = ":zfnkskfnq?"
#         TrueChild = {...}
#         FalseChild = {...}
#     }
#     FalseChild = {
#         question = "oqjfeojqfjfq?"
#         TrueChild = {...}
#         FalseChild = {...}
#     }
# }

@app.route('/recomendation')
def getRecommendation():
    # posterId = request.args.get("RecomendationId")
    # posterId = request.args.get("LastAwnser")
    # poster_url = basePosterURL + posterId
    # poster_filename = wget.download(poster_url, out=imgFolderCacheName)
    # res = evaluatePoster(model,poster_filename)
    # # print('\n#####' + res)

    response =  jsonify({
        'question': "alpha1?",
        'TrueChild': {
            'question': ":alpha2?",
            'TrueChild': {},
            'FalseChild': {},
        },
        'FalseChild': {
            'question': "alpha3?",
            'TrueChild': {},
            'FalseChild': {},
        }
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


if __name__ == "__main__":
    if os.path.exists(imgFolderCacheName) :
        shutil.rmtree(imgFolderCacheName)
    os.makedirs(imgFolderCacheName)
        
    model = getModel()
    app.run( debug=True, port=4996)
    # app.run(host="0.0.0.0", port=8080, debug=True)
