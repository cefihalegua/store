from bottle import run, template, static_file, get, post, delete, request, TEMPLATE_PATH
import json
import os
import database_sql

TEMPLATE_PATH.insert(0, os.path.dirname(__file__))

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

@delete('/category/<id>')
def delete_category(id):
    result = database_sql.delete_category(id)
    return json.dumps(result)

@post('/product')
def add_edit_product():
    data = request.POST.dict
    result = database_sql.add_edit_product(data)
    return result

@get('/products')
def get_products():
    result = database_sql.get_products()
    return json.dumps(result)

@get('/product/<id>')
def get_product(id):
    result = database_sql.get_product(id)
    return result

@delete('/product/<id>')
def delete_product(id):
    result = database_sql.delete_product(id)
    return json.dumps(result)

@get('/category/<id>/products')
def products_by_category(id):
    result = database_sql.products_by_category(id)
    return result

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

