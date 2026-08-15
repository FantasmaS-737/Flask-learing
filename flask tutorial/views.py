from main import app
from flask import render_template

@app.route("/")
def homePage():
	return render_template("homepage.html")
	
@app.route("/blog")
def blogPage():
	return render_template("blogpage.html")
	
@app.route("/contatos")
def contatospage():
	return render_template("contatospage.html")
	
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
	return render_template("usuarios.html", nome_usuario = nome_usuario)

@app.route("/primeiro_aprendizado")
def primeiro_aprendizado():
	return render_template("primeiro.html")