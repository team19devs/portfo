from flask import Flask, render_template, redirect, request
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/<string:get_page>")
def page(get_page):
	return render_template(get_page)

def data_collector(data):
	with open("database.txt", mode="a") as database:
		sender = data["sender"]
		subject = data["subject"]
		message = data["message"]
		database.write(f'\n\nfrom: {sender}\n\tsubject: {subject}\nmessage: {message}')

def csv_collector(excel_data):
	with open('database.csv', mode="a", newline="") as csv_data:
		sender = excel_data["sender"]
		subject = excel_data['subject']
		message = excel_data["message"]
		userdata = csv.writer(csv_data, delimiter="," ) #,quotechar=" ", quoting=csv.QUOTE_MINIMAL
		userdata.writerow([sender,subject,message])

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		csv_collector(data)
		return redirect("/thank_you.html")
	else:
		return "smth went wrong"
