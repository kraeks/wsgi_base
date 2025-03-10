import os
from chameleon import PageTemplateLoader
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

def write_to_excel(user_data):
    """Daten nach Excel schreiben"""

def application(environ, start_response):

    headers = [('Content-type', 'text/html; charset=utf-8')]
    path = os.path.dirname(__file__)
    templates = PageTemplateLoader(os.path.join(path, "templates"))
    template = templates["simple_form.pt"]

    path_info = environ.get('PATH_INFO', '/')

    if path_info == '/':
        # Render the form
        body = template()
        status = '200 OK'

    elif path_info == '/submit' and environ['REQUEST_METHOD'] == 'POST':
        # Process form submission
        input_data = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0)))
        form_data = input_data.decode('utf-8')
        user_data = dict(x.split("=") for x in form_data.split("&"))
        print(user_data)

        try:
            # Validate the data using the Pydantic model
            user = User(**user_data)
            message = f"Valid User Data:\nUsername: {user.username}, Email: {user.email}, Age: {user.age}"
            status = '200 OK'
            body = template(message = message)
        except Exception as e:
            status = '500'
            message = f"Invalid User Data: {e}"
            body = template(message = message)

        # Redirect back to the form page
        #status = '303 See Other'
        #headers.append(('Location', '/'))
        #body = template()

    else:
        status = '404 Not Found'
        body = '404 Not Found'

    start_response(status, headers)
    return [body.encode('utf-8')]
