
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Devs'}
	posts = [
		{
			'author' : {'nickname' : '승우'}
			,'body' : 'BBBBBBBBBBBBBBADFADFADFBeautiful!!!!!!!! day in Portleand!'
		}
		,{
			'author' : {'nickname' : 'John2'}
			,'body' : 'The Avengers movie was so cool!'
		}
	]
	return render_template("index.html",
		title = 'Home'
		,user = user
		,posts = posts)


@app.route('/login',methods = ['GET' , 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for openid="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html'
						,title = 'Sign In'
						,form = form
						,providers = app.config['OPENID_PROVIDERS'])