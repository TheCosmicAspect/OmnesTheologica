from flask import Flask, render_template

# create Flask instance
app = Flask(__name__)

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

# ------------------- #
# --- Error pages --- #
# ------------------- #

@app.errorhandler(404)
def page_not_found():
	return '404! Page not found!'
