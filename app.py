from flask import Flask, render_template

app = Flask(__name__)


# defining class for "jinja_data_structures.html" file to access GalileanMoons class values

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


# rendering plan text

@app.route("/")
@app.route("/hello/")
def hello_world():
    return "Hello World!"

# rendering embedded HTML string


@app.route("/fancy/")
def first_app():
    return """
    <h1>Intro to Flask Framework</h1>
    <p>I am learning flask from udemy platform. This is best course to get skills.</p>
"""

# rendering first_page.html file


@app.route("/first/")
def first_page():
    return render_template("first_page.html")

# rendering second_page.html file


@app.route("/second/")
def second_page():
    return render_template("second_page.html")

# rendering jinja_intro.html file


@app.route("/jinja2/")
def jinja_page():
    return render_template("jinja_intro.html", name="Prashant", template_name="Jinja2")

# rendering jinja_expressions.html file


@app.route("/expressions/")
def jinja_expression():

    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition and substraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation
    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name

    }

    return render_template("jinja_expressions.html", **kwargs)


# rendering jinja_data_structures.html file

@app.route("/data_structures/")
def data_structures():

    movies = ["Leon the Professional",
              "The Usual Suspects", "A Beautiful Mind"]

    car = {"brand": "Tesla", "model": "Roadster", "year": "2020"}

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {"movies": movies, "car": car, "moons": moons}

    return render_template("jinja_data_structures.html", **kwargs)


# here rendering jinja_conditionals.html file with the conditions like " with company " and " without company"

@app.route("/conditionals/")
def jinja_conditionals():

    company = "Apple"  # pass company name from jinja_conditionals.html file

    return render_template("jinja_conditionals.html", company=company)


# here rendering jinja_for_loops.html file

@app.route("/for_loops/")
def jinja_for_loops():

    # Here is list
    planets = ["Mercury",
               "Venus",
               "Earth",
               "Mars",
               "Jupiter",
               "Saturn",
               "Uranus",
               "Neptune"
               ]

    # Here is Dictionary
    players = {"ms_dhoni": "Ranchi",
               "rohit_sharma": "Mumbai",
               "virender_sehwag": "Delhi"
               }

    kwargs = {"planets": planets, "players": players}

    return render_template("jinja_for_loops.html", **kwargs)


# rendering loops and conditional template "jinja_loops_conditional.html" file.

@app.route("/loops_conditionals/")
def loops_conditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows"
    }
    
    return render_template("jinja_loops_conditional.html", user_os= user_os)