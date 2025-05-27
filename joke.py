from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/joke")
def joke():
    joke = None
    api_url = "https://icanhazdadjoke.com/"
    mood=["Happy", "Sad", "Stressed", "Bored"]
    error = None
    dad_joke=""
    dad_jokes =[]
    if request.method == "POST":
        headers={"Accept":"application/json"}
        response = requests.get(api_url,headers=headers)
        if response.status_code == 200:
            data = response.json()
            dad_jokes = list(data["message"].keys())
            dad_jokes.sort()
            dad_joke = request.form.get("joke")
    
    return render_template("joke.html", mood=mood, dad_joke=dad_joke, dad_jokes=dad_jokes)

@app.route("/search", methods=["GET", "POST"])
def search_joke():
        joke=None
        term=None
        error=None
        jokes=""
        if request.method == "POST":
                term = request.form.get("search")
                api_url = f"https://icanhazdadjoke.com/search?term={term}"
                headers = {"Accept": "application/json"}
                response = requests.get(api_url, headers=headers)
                if response.status_code == 200:
                        jokes = response.json().get("results")
                else:
                     error="Couldnt get your joke, either try again with a different term or try again later "
        return render_template("search.html",jokes=jokes,error=error,joke=joke)
if __name__ == "__main__":
    app.run(debug=True)