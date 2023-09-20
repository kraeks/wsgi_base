def application(environ, start_response):
    """ 
        * def application ist der Standard Endpunkt der WSGI-Applikation 
        * environ - dict mit Informationen über den eingehenden Request
        * start_response - Funktion zum Setzen des Status-Codes und der Response Header
    """
    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    message = "Hello World"
    response_content = message.encode('utf-8')

    start_response(status, headers)
    return [response_content] #Eine Liste von Bytestrings wg. Streaming

    #return [b'Hello ', b'World']
