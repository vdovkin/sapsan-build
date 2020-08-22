from flask import render_template, redirect, url_for, Blueprint

from core.main.forms import ContactForm

from apps import APPS

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("main/home.html", apps=APPS)


@main.route("/about")
def about():
    return render_template("main/about.html", title="Про сервіс")


@main.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("main.home"))
    return render_template("main/contact.html", title="Контакти", form=form)
