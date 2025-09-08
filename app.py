from flask import Flask, render_template, redirect, url_for, flash, session
from datetime import datetime
from config import Config
from forms import NameForm


app = Flask(__name__)
app.config.from_object(Config)


@app.context_processor
def inject_now():
    # Exemplo: disponibiliza 'now' para usar no rodapé se quiser
    return {"now": datetime.utcnow()}


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        old_name = session.get("name")
        if old_name and old_name != name:
            flash("Looks like you changed your name!", "warning")
        session["name"] = name
        flash("Name saved successfully!", "success")
        return redirect(url_for("index"))


    return render_template(
        "index.html",
        form=form,
        name=session.get("name")
    )


# Páginas de erro bonitinhas (opcional)
@app.errorhandler(404)
def not_found(e):
    return (
        render_template(
            "base.html",
            content_title="404 — Not Found",
            content_body="Page not found."
        ),
        404
    )


@app.errorhandler(500)
def server_error(e):
    return (
        render_template(
            "base.html",
            content_title="500 — Server Error",
            content_body="Something went wrong."
        ),
        500
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
