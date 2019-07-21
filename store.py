from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql
import database_sql


@get("/admin")
def admin_portal():
    return template("pages/admin.html")


@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


@post("/category")
def post_category_to_database():
    entered_category = request.POST.get("name")
    result = database_sql.insert_category(entered_category)
    return json.dumps(result)


@get("/categories")
def send_categories():
    result = database_sql.return_categories()
    return json.dumps(result)


@post("/product")
def add_edit_product():
    product_details = request.POST.dict
    result = database_sql.add_edit_product(product_details)
    return json.dumps(result)


@get("/products")
def display_products():
    result = database_sql.return_products()
    return json.dumps(result)


@get("/category/<id>/products")
def display_products_by_category(id):
    result = database_sql.return_products_by_category(id)
    return json.dumps(result)


run(host='localhost', port=8000)

