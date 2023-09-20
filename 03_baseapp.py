from chameleon import PageTemplateLoader

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

def application(environ, start_response):

    loader = PageTemplateLoader(".")
    template = loader["bootstrap.pt"]

    rendered_template = template(users=users)

    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, headers)

    return [rendered_template.encode('utf-8')]
