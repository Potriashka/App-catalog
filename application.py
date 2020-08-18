from flask import Flask, redirect, url_for, render_template, request, session
from firebase import firebase

app = Flask(__name__)
app.secret_key = 'secret_key'

firebase = firebase.FirebaseApplication("https://my-awesome-project-46dd8.firebaseio.com/", None)

@app.route('/login2', methods=["POST", "GET"])
def reallogin():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["pass"]
		data = {
			'Username':username,
			'Password':password
		}
		result = firebase.post('my-awesome-project-46dd8/User', data)
		print(result)
		session["username"] = username
		session["password"] = password
		return redirect(url_for("home"))
	else:
		return render_template('login.html')

@app.route('/data')
def data1():
	if "username" in session:
		return render_template('search.html', username=session["username"], password = session["password"])
	else: 
		return redirect(url_for("reallogin"))

@app.route('/games')
def games():
	if "username" in session:
		return render_template('games.html')
	else: 
		return redirect(url_for("reallogin"))

@app.route('/apps')
def apps():
	if "username" in session:
		return render_template('apps.html')
	else: 
		return redirect(url_for("reallogin"))

@app.route('/logout')
def logout():
	session.pop("username", None)
	session.pop("password", None)
	return redirect(url_for("home"))

@app.route('/sites')
def sites():
	if "username" in session:
		return render_template('sites.html')
	else: 
		return redirect(url_for("reallogin"))

@app.route('/about-us')
def aboutus():
	if "username" in session:
		return render_template('contacts.html')
	else: 
		return redirect(url_for("reallogin"))

@app.route('/peter')
def peter():
	if "username" in session:
		return render_template('peter.html')
	else: 
		return redirect(url_for("reallogin"))

@app.route('/bekhruz')
def bekhruz():
	if "username" in session:
		return render_template('bekhruz.html')
	else: 
		return redirect(url_for("reallogin"))

@app.route('/user')
def user123():
	if "username" in session:
		return f"{username}<br/>{password}"
	else: 
		return redirect(url_for("reallogin"))

@app.route('/social-app')
def social_app():
	if "username" in session:
		return render_template('social-app.html')
	else: 
		return redirect(url_for("reallogin"))

@app.route("/<usr>")
def user(usr):
	if "username" in session:
		return f"<h1>{usr}</h1>"
	else:
		return redirect(url_for("reallogin"))

@app.route('/', methods=["POST", "GET"])
def home():
	if "username" in session:
		if request.method == "POST":
			user = request.form["search_field"]
			return redirect(url_for("user", usr=user))
		else:
			return render_template('home.html')
	else: return redirect(url_for("reallogin"))

if __name__ == "__main__":
	app.run(debug=True)
