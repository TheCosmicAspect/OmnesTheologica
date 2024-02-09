from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create Flask instance
app = Flask(__name__)

app.config['SECRET_KEY'] = "kj13D4T2dgTs4S5ghmni8HI98H9832vdo82h"

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
	display_name = None
	form = UserForm()

	# Validate Form
	if form.validate_on_submit():
		display_name = form.display_name.data
		form.display_name.data = ''

	return render_template('signup.html',
		display_name = display_name,
		form = form
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
