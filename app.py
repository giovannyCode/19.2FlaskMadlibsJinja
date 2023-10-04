from flask import Flask, request, render_template
'''from flask_debugtoolbar import DebugToolbarExtension'''
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] ="oh-so-secret"
'''debug = DebugToolbarExtension(app)'''

@app.route("/home")
def home_page():
  return render_template("homepage.html")

@app.route("/story",methods=["POST"])
def story_page():

  place = request.form["place"]
  noun= request.form["noun"]
  verb= request.form["verb"]
  adjective= request.form["adjective"]
  plural_noun = request.form["plural_noun"]
  dictionary={"place":place,"noun":noun,"verb":verb,"adjective":adjective,"plural_noun":plural_noun}
  story = Story(["place", "noun", "verb", "adjective", "plural_noun"],
      """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
  
  outPutStory = story.generate(dictionary)
  return render_template("story.html",outPutStory =outPutStory)
