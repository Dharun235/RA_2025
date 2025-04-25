from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["textdb"]
collection = db["texts"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form.get("user_text")
        if user_text:
            collection.insert_one({"text": user_text})
        return redirect("/")
    
    all_texts = list(collection.find())
    return render_template("index.html", texts=all_texts)

if __name__ == "__main__":
    app.run(debug=True)
