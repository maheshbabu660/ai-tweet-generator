from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result=None

    if request.method=="POST":

        brand = request.form["brand_name"]
        industry = request.form["industry"]
        objective = request.form["objective"]
        products = request.form["products"]

        tweets = [
f"Discover the taste of {brand}! Try our {products} today ☕",
f"{brand} is redefining {industry}. Don’t miss out!",
f"Experience the magic of {brand}. Visit us today!",
f"{products} lovers, this one’s for you! #{brand}",
f"Step into style with {brand}! Explore our {products}.",
f"{brand} brings the best in {industry}. Try it today!",
f"Upgrade your lifestyle with {products} from {brand}.",
f"Trendy. Affordable. Stylish. That’s {brand}! #Fashion",
f"Your perfect pick from {brand} awaits! {products}",
f"Love {products}? You’ll love them even more at {brand}! 💥"
]
        voice_summary=[
        f"{brand} focuses on quality and customer experience.",
        f"Engaging and friendly communication style.",
        f"Highlights innovation in {industry}."
        ]

        result={
        "tweets":tweets,
        "voice_summary":voice_summary
        }

    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
    

if __name__ == "__main__":
    app.run(debug=True)
