from flask import render_template, redirect, url_for

from . import sell

@sell.route('/home')
def home():
    return render_template('sell/home_page.html')


