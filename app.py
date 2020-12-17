import flask, json
app= flask.Flask(__name__)

cafc_opinions = json.load(open('./data/cafc_opinions.json'))
cafc_hearings = json.load(open('./data/cafc_hearings.json'))

@app.route('/')
def index():
  return flask.render_template('index.html', 
    cafc_opinions=cafc_opinions,
    cafc_hearings=cafc_hearings)

if __name__ == "__main__":
    app.run()