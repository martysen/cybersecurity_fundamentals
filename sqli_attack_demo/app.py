# install our dependencies - flask, sqlite3
import sqlite3
from flask import Flask, request, render_template_string, g

'''
1. initialize an instance of your flask web application 
2. declare a database name 
3. establish connection with our DB (func)
4. close the db connection (func)
5. initialize the db --> insert mock data (func)
6. web server routes || functionalities 
6.1. for the home page (func)
6.2. for the login functions (func) --> query the db : vulnerability for sqli attacks
7. main function 
     -- run the db initialization function (step 5)
     -- run the web applications 
Summarized 
1. learned to implement a minimalistic full stack web application using the Flask Python framework and sqlite
2. key component of Flask - syntaxes 
3. how to wrtie and execute sql queries in python
4. demo of sql injection attacks and how to solve it - focus on separation between query and data
'''
# initialize an instance of your flask web application 
app = Flask(__name__)

# declare a database name 
DATABASE = 'users.db'

# create the database with name in the loc above if it does not exist already 
# establish a connection with the db after creating it 
def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
  return db

# close the connection when the operations agains the db has been completed 
@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

# init the db and insert some mock data 
def init_db():
  with app.app_context():
    db = get_db()
    # object relation mapping
    # a cursor is used to execute SQL queries and fetch results from the relational DB  
    cursor = db.cursor()
    # create table inside my db 
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

    # add mock data into these tables 
    cursor.execute("INSERT INTO users (username, password) VALUES ('alice', 'password123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('bob', 'securepass')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('charlie', 'mypassword')")

    # push the data permanently into the database 
    db.commit()

# start creating the web server routes 
# url route for home page is '/' 
@app.route('/')
def home():
  # render_template_string allows us to write HTML code as a string
  return render_template_string('''
  <h1>Login</h1>
  <form method="POST" action="/login">
      <input type="text" name="username" placeholder="enter your username" required />
      <br />
      <input type="password" name="password" placeholder="enter your password" required />
      <br />
      <input type="submit" value="Login" />
  </form>
  '''
  )

# craete the route for /login
@app.route("/login", methods=['POST'])
def login():
  # unpack the http request form and grab the username and pwd and store in varibales
  # sql query using the user input -- inject the vulnerability for sqli attacks 
  username = request.form['username'] 
  password = request.form['password']

  # vulnerability := no clear separation between query and data 
  # username := alice'; DROP TABLE users; --
  # query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
  query = "SELECT * FROM users WHERE  username = ? AND password = ?"

  # cursor object to run the query 
  cursor = get_db().cursor()
  cursor.execute(query, (username, password))
  user = cursor.fetchone()

  # check if successful response or not 
  if user:
    return "Login Successful"
  else:
    return "Invalid credentials."


# main function 
if __name__ == '__main__':
  init_db()
  app.run(debug=True)

# run this in terminal; open a web browser and type the following url - localhost:5000 or 127.0.0.1:5000
# if there is any other application that is running on port 5000 you will get an error ! 