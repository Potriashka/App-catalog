from flask import Flask, redirect, url_for, render_template, request
import firebase
import python-firebase

app = Flask(__name__)

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
		result = firebase.post('my-awesome-project-46dd8/Customer', data)
		print(result)
		return redirect(url_for("home"))
	else:
		return render_template('login.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/sites')
def sites():
    return render_template('sites.html')

@app.route('/about-us')
def aboutus():
    return render_template('contacts.html')

@app.route('/peter')
def peter():
    return render_template('peter.html')

@app.route('/bekhruz')
def bekhruz():
    return render_template('bekhruz.html')

@app.route('/user')
def user123():
	return f"{username}<br/>{password}"

@app.route('/social-app')
def social_app():
	return render_template('social-app.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/', methods=["POST", "GET"])
def home():
	if request.method == "POST":
		user = request.form["search_field"]
		return redirect(url_for("user", usr=user))
	else:
		return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
