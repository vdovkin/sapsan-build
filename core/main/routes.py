from flask import render_template, Blueprint
from apps import APPS

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("main/home.html", apps=APPS)


@main.route("/about")
def about():
    return render_template("main/about.html", title="Про сервіс")


@main.route("/contact")
def contact():
    return render_template("main/contact.html", title="Контакти")
