import os
from chameleon import PageTemplateLoader

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

def index_page(environ, start_response):

    path = os.path.dirname(__file__)
    templates = PageTemplateLoader(os.path.join(path, "templates"))
    template = templates["bootstrap.pt"]

    rendered_template = template(users=users)

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, headers)

    return [rendered_template.encode('utf-8')]

def about_page(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    body = "<h1>Über uns</h1><p>Das ist eine unformatierte Über uns Seite</p>"
    response_body = body.encode('utf-8')

    start_response(status, headers)

    return [response_body]

def not_found(environ, start_response):
    status = '404 Not Found'
    headers = [('Content-type', 'text/plain')]

    response_body = b"404 - Not Found"

    start_response(status, headers)

    return [response_body]

def application(environ, start_response):
    url_mapping = {
        '/': index_page,
        '/about': about_page,
    }

    path = environ.get('PATH_INFO', '/')

    handler = url_mapping.get(path, not_found)

    return handler(environ, start_response)
