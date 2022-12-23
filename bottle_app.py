from bottle import default_app, route, post, get, template

@route('/')
def bmi_app():
    return template("bmi_frontpage.html")

@post('/result')
def result():
    return template ("result.html")


application = default_app()

