from flask import render_template, url_for, redirect, flash
from paskey.forms import openKey, generateKey
from paskey.models import Keys
from random import randint
from paskey import app, db


@app.route("/", methods=["GET", 'POST'])
def index():
    form1 = openKey()
    if form1.validate_on_submit():
        query = Keys.query.filter_by(key=form1.paskey.data).first()
        if query:
            return redirect(query.link)
        else:
            flash(f'Key not found !', '#CD5C5C')
            return redirect(url_for('index'))
    return render_template('home.html', form=form1, title="Paskey | World of keys")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    form2 = generateKey()
    if form2.validate_on_submit():
        gkey = str(randint(1000,9999))
        while Keys.query.filter_by(key=gkey).first():
            gkey = randint(1000,9999)
        glink = form2.url.data
        addkey = Keys(link=glink, key=gkey)
        db.session.add(addkey)
        db.session.commit()
        flash(f"Key Generated ! Your Key is : {gkey}", '#00ffc7')
        return redirect(url_for('index'))
    return render_template('generate.html', form=form2, title="Generate Paskey")

@app.route("/<ukey>")
def redirector(ukey):
    if Keys.query.filter_by(key=ukey).first():
        ulink = Keys.query.filter_by(key=ukey).first().link
        return redirect(ulink)
    else:
        return render_template('404.html')