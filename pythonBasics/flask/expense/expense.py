from flask import Flask, render_template, request


app = Flask(__name__)

# Home Page
@app.route("/home")
def home():
    return render_template('home.html')

#Registration Page
@app.route("/login")
def login():
    return render_template('login.html')
#About Page
@app.route('/login_validation', methods = ['POST'])
def login_validation():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    cnfpassword = request.form.get('cnfpassword')
    return "The name is {} and  email is {} and the password is {}".format(name,email,password)
#Contacts page
 

if __name__ == '__main__':
    app.run(debug=True)