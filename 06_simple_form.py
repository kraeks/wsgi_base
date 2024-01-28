import os
from chameleon import PageTemplateLoader

def application(environ, start_response):

    headers = [('Content-type', 'text/html; charset=utf-8')]
    path = os.path.dirname(__file__)
    templates = PageTemplateLoader(os.path.join(path, "templates"))
    template = templates["simple_form.pt"]

    path_info = environ.get('PATH_INFO', '/')

    if path_info == '/':
        body = template()
        status = '200 OK'

    elif path_info == '/submit' and environ['REQUEST_METHOD'] == 'POST':
        input_data = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0)))
        form_data = input_data.decode('utf-8')
        user_data = dict(x.split("=") for x in form_data.split("&"))
        print(user_data)

        status = '303 See Other'
        headers.append(('Location', '/'))
        body = template()

    else:
        status = '404 Not Found'
        body = '404 Not Found'

    start_response(status, headers)
    return [body.encode('utf-8')]
