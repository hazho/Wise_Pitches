from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns index page 
    '''
    message= "Hello"
    title = 'Welcome To One Minute Pitch'
    return render_template('index.html', message=message,title=title)
