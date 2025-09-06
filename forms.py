from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NameForm(FlaskForm):
name = StringField(
"Your name",
validators=[DataRequired(message="Digite um nome."), Length(max=50)],
render_kw={"placeholder": "Type your name"}
)
submit = SubmitField("Send")
