from flask import Flask, render_template


app = Flask(__name__)

projects = [
    {
        "name": "Randum Runner app with C# and Unity",
        "thumb": "img/random_runner.png",
        "hero": "img/random_runner-hero.png",
        "categories" : ["C#", "Unity"],
        "slug": "A luck-based race game",
        "prod": "https://sharemygame.com/@HyunsangCoder/randomrunner"
    },
    {
        "name": "Slack Bot with Python and Bolt API",
        "thumb": "img/slack_bot.png",
        "hero": "img/slack_bot-hero.png",
        "categories" : ["Python", "Slack/Bolt API"],
        "slug": "A custom Slack bot to export data",
        "prod": "https://slack.dev/bolt-python/concepts"
    },
    {   
        "name": "Simple Shooter with C++ and Unreal",
        "thumb": "img/simple_shooter.png",
        "hero": "img/simple_shooter-hero.png",
        "categories" : ["C++", "Unreal Engine"],
        "slug": "A simple TPP shooter game",
        "prod": "https://www.unrealengine.com"
    },
]

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html", projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html", projects=projects)