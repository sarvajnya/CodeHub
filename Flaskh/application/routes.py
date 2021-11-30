from application import app  # api
# from application.delete_code import delete_code
from application.models import User, Enrollment, Savedcode, Deletecode
from application.forms import LoginForm, RegistrationForm, Compiler
from datetime import datetime
from application import db
from application.Compiler.compilecode import Compile, creating_file
from flask import render_template, request, flash, redirect, url_for, session, send_file
# from application.course_list import course_list
from application.code_save import code_save
# from flask_restplus import Resource
from config import Config_info

################################################################


# @api.route('/api', '/api/')
# class GetAndPost(Resource):
#     # GET
#     def get(self):
#         return jsonify(User.objects.all())
#
#     # POST
#     def post(self):
#         data = api.payload
#         user = User(user_id=data['user_id'], email=data['email'], first_name=data['first_name'],
#                     last_name=data['last_name'])
#         user.set_password(data['password'])
#         user.save()
#         return jsonify(User.objects(user_id=data['user_id']))
#
#
# @api.route('/api/<idx>')
# class GetUpdateDelete(Resource):
#
#     # GET One
#     def get(self, idx):
#         return jsonify(User.objects(user_id=idx))
#
#     # PUT
#     def put(self, idx):
#         data = api.payload
#         User.objects(user_id=idx).update(**data)
#         return jsonify(User.objects(user_id=idx))
#
#     # DELETE
#     def delete(self, idx):
#         data = api.payload
#         User.objects(user_id=idx).delete()
#         return jsonify("user is deleted!")
#
# ################################################################


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    form = Compiler()

    if form.validate_on_submit():
        result = []
        code = request.form['code']
        input = request.form['input']
        language = form.language.data
        title = request.form['title']
        description = request.form['description']
        if code == "":
            flash(u"Code is Empty", "Warning")
            return render_template("index.html", form=form, index=True)
        if request.form.get("Save"):
            if not session.get('user_name'):
                return redirect(url_for('login'))
            user_id = session.get('user_id')
            now = datetime.now()
            date = now.strftime("%d/%m/%Y %H:%M:%S")
            Savedcode(user_id=user_id, title=title, description=description, code=code,
                      language=language, date=date).save()
            flash("Code is successfully Saved", "success")
        elif request.form.get("Run"):
            result = Compile(code, language.upper(), input)
            form.code.data = code
            form.output.data = result
            form.input.data = input
        elif request.form.get("Download"):
            file_name = creating_file(code, language.upper())
            return send_file(file_name, as_attachment=True)
    return render_template("index.html", form=form, index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('user_name'):
        return redirect(url_for('index'))
    form = LoginForm()
    empty_form = Compiler()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(user.first_name + " ,you are successfully logged in", "success")
            session['user_id'] = user.user_id
            session['user_name'] = user.first_name
            return render_template("index.html", form=empty_form, index=True)
        else:
            flash("Something went wrong", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('user_name', None)
    return redirect(url_for("index"))


@app.route("/AboutUs")
def AboutUs():
    return render_template("AboutUs.html")


@app.route("/SavedCode", methods=['GET', 'POST'])
def SavedCode():
    if not session.get('user_name'):
        return redirect(url_for('login'))
    else:
        title = request.values.get('title')
        if request.values.get('edit') == "":
            ide_form = Compiler()
            title = request.form.get('title')
            ide_form.code.data = request.form.get('code')
            ide_form.language.data = request.form.get('language')
            ide_form.title.data = request.form.get('title')
            ide_form.description.data = request.form.get('description')
            return render_template("index.html", form=ide_form, index=True)
        elif request.values.get('delete') == "":
            title = request.form.get('title')
            user_id = session.get('user_id')
            date = request.form.get('date')
            delete = Savedcode.objects.get(user_id=user_id, title=title, date=date)
            delete.delete()
            flash(title + " , successfully Deleted", "success")
        elif request.values.get('Download') == "":
            code = request.values.get('code')
            language = request.values.get('language')
            file_name = creating_file(code, language.upper())
            return send_file(file_name, as_attachment=True)
        savedCode = Savedcode.objects.order_by('-date')
    return render_template("savedcode.html", savedCode=savedCode)


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('user_name'):
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        user = User(first_name=first_name, last_name=last_name, user_id=user_id, email=email)
        user.set_password(password)
        user.save()
        # save data to database
        flash("You are successfully Registered.", "Success")
        return redirect(url_for("index"))
        # return form.errors()
    return render_template("Register.html", title="Register", form=form, Register=True)


# @app.route("/api/")
# @app.route("/api/<idx>")
# def api(idx=None):
#     if idx is None:
#         jdata = courseData
#     else:
#         jdata = courseData[int(idx)]
#     return Response(json.dumps(jdata), mimetype="application.json")


@app.route("/user")
def user():
    user = User.objects.all()
    return render_template("user.html", user=user)
