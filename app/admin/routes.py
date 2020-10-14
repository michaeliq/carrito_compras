from flask import render_template, url_for, redirect

from . import admin

@admin.route('/admin/front/')
def front():
    return render_template('admin/front.html')

@admin.route('/admin/control_panel/')
def control_panel():
    pass

