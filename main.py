from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create Flask instance
app = Flask(__name__)
# secret key
app.config['SECRET_KEY'] = "kj13D4T2dgTs4S5ghmni8HI98H9832vdo82h"
# users db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# init db
db = SQLAlchemy(app)

app.app_context().push() 

# ------------------ #
# ----- Routes ----- #
# ------------------ #

# Home
@app.route('/')
def index():
	return render_template('index.html')

# Theology
@app.route('/theology')
def theology():
	return render_template('theology.html')

# Denoms
@app.route('/denominations/<denom>')
def denomination(denom):
	return render_template('denomination.html', denom = denom)

# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = UserForm()

	# Validate Form
	if form.validate_on_submit():
		user = UsersDB.query.filter_by(email=form.email.data).first()
		if user is None:
			user = UsersDB(
				display_name = form.display_name.data,
				email = form.email.data
				)
			
			# finalize changes
			db.session.add(user)
			db.session.commit()

		# clear form
		form.display_name.data = ''
		form.email.data = ''
	our_users = UsersDB.query.order_by(UsersDB.date_added)


	return render_template('signup.html',
		form = form,
		our_users = our_users
		)

# ------------------- #
# --- Error pages --- #
# ------------------- #

@app.errorhandler(404)
def page_not_found():
	return '404! Page not found!'


# ------------------- #
# ----- Classes ----- #
# ------------------- #

# Form Class
class UserForm(FlaskForm):
	display_name = StringField('Display Name: ')
	email = StringField('Email: ', validators=[DataRequired()])
	username = StringField('Username: ', validators=[DataRequired()])
	submit = SubmitField('Submit')

# DB Model
class UsersDB(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	display_name = db.Column(db.String(25))
	email = db.Column(db.String(100), nullable = False, unique = True)
	username = db.Column(db.String(50), unique = True)
	date_added = db.Column(db.DateTime, default = datetime.utcnow)

	# I think this is important
	def __repr__(self):
		return '<Name %r>' % self.name