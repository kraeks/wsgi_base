import os
from chameleon import PageTemplateLoader
from pydantic import BaseModel
import sqlite3

class User(BaseModel):
    username: str
    email: str
    age: int

def insert_user_data(user):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    username TEXT, 
                    email TEXT, 
                    age INTEGER)''')

    cursor.execute("INSERT INTO users (username, email, age) VALUES (?, ?, ?)",
                       (user.username, user.email, user.age))

    conn.commit()
    conn.close()

def application(environ, start_response):

    headers = [('Content-type', 'text/html; charset=utf-8')]
    path = os.path.dirname(__file__)
    templates = PageTemplateLoader(os.path.join(path, "templates"))
    template = templates["user_form.pt"]

    path_info = environ.get('PATH_INFO', '/')

    if path_info == '/':
        body = template()
        status = '200 OK'

    elif path_info == '/submit' and environ['REQUEST_METHOD'] == 'POST':
        input_data = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0)))
        form_data = input_data.decode('utf-8')
        user_data = dict(x.split("=") for x in form_data.split("&"))
        print(user_data)

        try:
            user = User(**user_data)
            insert_user_data(user)
            message = f"Valid User Data:\nUsername: {user.username}, Email: {user.email}, Age: {user.age}"
            status = '200 OK'
            body = template(message = message)
        except Exception as e:
            status = '500'
            message = f"Invalid User Data: {e}"
            body = template(message = message)

        headers.append(('Location', '/'))

    else:
        status = '404 Not Found'
        body = '404 Not Found'

    start_response(status, headers)
    return [body.encode('utf-8')]
