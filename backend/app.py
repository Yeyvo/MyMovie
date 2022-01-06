from flask import Flask , request

app = Flask(__name__)

@app.route('/test')
def index():
    return "test"

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/categorization')
def getCategories():
    request.args.get("movieId")


