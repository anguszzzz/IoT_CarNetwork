
from flask import request, render_template,  flash, redirect, url_for

from app.web import web
from app.forms.userForm import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from flask_login import login_user






@web.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm(request.form)
    if request.method =='POST' and form.validate():
        user=User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('register.html',form=form)


@web.route('/login',methods=['GET','POST'])
def login():
    form =LoginForm(request.form)
    if request.method=='POST' and form.validate():
       user=User.query.filter_by(email=form.email.data).first()
       if not user:
           flash('This email has not been registered')
       if user and  user.check_password(form.password.data):
           next= request.args.get('next')

           if not next or next.startswith('/'): #redirect attack
               next = url_for('web.index')
           login_user(user,remember= True)

           return redirect(next)
       else:
           flash('Please enter correct password')
    return render_template('login.html',form=form)

@web.route('/account',methods=['GET','POST'])
def account():
    return render_template('account.html')

