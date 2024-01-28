import os
from chameleon import PageTemplateLoader
from pydantic import BaseModel

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class User(BaseModel):
    username: str
    email: str
    age: int

Base = declarative_base()

class Table(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


database_file = 'user_data.db'
database_exists = os.path.isfile(database_file)
engine = create_engine(f'sqlite:///{database_file}')
Session = sessionmaker(bind=engine)

if not database_exists:
    Base.metadata.create_all(engine)


def insert_user_data(user_data):

    try:
        session = Session()
        user = Table(username=user_data.username, email=user_data.email, age=user_data.age)
        session.add(user)
        session.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if session:
            session.close()

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
