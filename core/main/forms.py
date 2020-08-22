from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    title = StringField("Тема", validators=[DataRequired()])
    content = TextAreaField("Повідомлення", validators=[DataRequired()])
    submit = SubmitField("Відправити")
