from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/joke", methods=["GET", "POST"])
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
            joke = response.json().get("joke")
    
    return render_template("joke.html", mood=mood, joke=joke, )


API_URL = "https://icanhazdadjoke.com/search"


headers = {
    'Accept': 'application/json'
}
@app.route('/search', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']
        response = requests.get(API_URL, headers=headers, params={'term': search_term})
        data = response.json()
        jokes = data.get('results', [])
        
        return render_template('search.html', jokes=jokes, search_term=search_term)
    
    return render_template('search.html', jokes=[], search_term='')

if __name__ == '__main__':
    app.run(debug=True)