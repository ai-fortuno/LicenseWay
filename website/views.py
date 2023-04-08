from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for 
from flask_login import login_required, current_user
from .models import Home
from . import db
import json

views = Blueprint('views', __name__)

formData = {}
@views.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST': 
        firstName = request.form['firstName']
        lp = request.form['lp']
        ti = request.form['ti']
        formData['firstName'] = firstName
        formData['firstName'] = firstName

    return render_template('home.html', user=current_user)






@views.route('/records')
def records():
    return render_template("records.html", user=current_user)
@views.route('/history')
def history():
    return render_template("history.html", user=current_user)
