import os
from chameleon import PageTemplateLoader
from cgi import FieldStorage

def application(environ, start_response):

    path = os.path.dirname(__file__)
    templates = PageTemplateLoader(os.path.join(path, "templates"))
    template = templates["form.pt"]

    form_data = FieldStorage(fp=environ['wsgi.input'], environ=environ)

    if form_data:
        print('Formdaten:')
        print(form_data)
    else:
        print('Es sind keine Formdaten vorhanden')

    name = form_data.getvalue('name', 'John Doe')
    print(name)
    email = form_data.getvalue('email', 'john@example.com')
    print(email)

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    rendered_template = template(name=name, email=email)

    start_response(status, headers)

    return [rendered_template.encode('utf-8')]
