from flask import Flask , request
from CNNCategorisation.py import categ 
app = Flask(__name__)

@app.route('/test')
def index():
    return "test"

if __name__ == "__main__":
    app.run(debug=True)
    model = categ.getModel()



@app.route('/categorization')
def getCategories():
    poster = request.args.get("movieId")
    categ.evaluatePoster(model,poster)
    


