import flask, json
import contentful
import os
from dotenv import load_dotenv

load_dotenv()

app= flask.Flask(__name__)

# cafc_opinions = json.load(open('./data/cafc_opinions.json'))
cafc_patent_cases = json.load(open('./data/cafc_patent_cases.json'))
cafc_hearings = json.load(open('./data/cafc_hearings.json'))
alice_cases = json.load(open('./data/alice_cases.json'))

client = contentful.Client(
  os.getenv("CONTENTFUL_SPACE_ID"),  # This is the space ID. A space is like a project folder in Contentful terms
  os.getenv("CONTENTFUL_DELIVERY_API")  # This is the access token for this space. Normally you get both ID and the token in the Contentful web app
)

blog_posts = client.entries({'content_type': 'blog'}) # query for a content-type by its ID (not name)

@app.route('/')
def index():
  return flask.render_template('index.html', 
    cafc_opinions=cafc_patent_cases[:10],
    cafc_hearings=cafc_hearings[:10])

@app.route('/alice')
def alice():
  return flask.render_template('alice.html', 
    alice_cases=alice_cases)

@app.route('/blog')
def blog():
  return flask.render_template('blog.html', 
    blog_posts=blog_posts)

if __name__ == "__main__":
    app.run()