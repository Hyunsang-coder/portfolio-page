from flask import Flask, render_template, abort


app = Flask(__name__)

projects = [
    {
        "name": "Randum Runner app with C# and Unity",
        "thumb": "img/random_runner.png",
        "hero": "img/random_runner-hero.png",
        "categories" : ["C#", "Unity"],
        "slug": "random_runner",
        "prod": "https://sharemygame.com/@HyunsangCoder/randomrunner"
    },
    {
        "name": "Slack Bot with Python and Bolt API",
        "thumb": "img/slack_bot.png",
        "hero": "img/slack_bot-hero.png",
        "categories" : ["Python", "Slack/Bolt API"],
        "slug": "slack_bot",
        "prod": "https://slack.dev/bolt-python/concepts"
    },
    {   
        "name": "Simple Shooter with C++ and Unreal",
        "thumb": "img/simple_shooter.png",
        "hero": "img/simple_shooter-hero.png",
        "categories" : ["C++", "Unreal Engine"],
        "slug": "simple_shooter",
        "prod": "https://www.unrealengine.com"
    },
]

slug_to_project = {project["slug"]:project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html", projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html", projects=projects)

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=slug_to_project[slug])