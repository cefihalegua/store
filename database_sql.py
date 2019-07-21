import pymysql

connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",       # the password section should be adapted accordingly
        db="store",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
)

def insert_category(cat_name):
    try:
        with connection.cursor() as cursor:
            sql = "insert into categories values (null, '{}')".format(cat_name)
            cursor.execute(sql)
            connection.commit()
            result = {
                "STATUS": "SUCCESS",
                "CAT_NAME": cat_name
            }
            return result
    except:
        return {"STATUS": "ERROR","MSG": "Problem with database"}

def return_categories():
    with connection.cursor() as cursor:
        sql = "select * from categories"
        try:
            cursor.execute(sql)
            categories = cursor.fetchall()
            return {
                "STATUS": "SUCCESS",
                "CATEGORIES": categories
            }
        except:
            return {
                "STATUS": "ERROR",
                "MSG": "Cannot get the categories from the database"
            }

def delete_category(id):
    try:
        with connection.cursor() as cur:
            sql = 'Delete From Categories Where id = {}'.format(id)
            cur.execute(sql)
            connection.commit()
            result = {'Status': "Success"}
            return result
    except:
        result = {'Status': "Error", 'MSG': "Category Not Found"}
        return result

def add_edit_product(product_details):
    category = product_details["category"][0]
    title = product_details["title"][0]
    description = product_details["desc"][0]
    price = product_details["price"][0]
    img_url = product_details["img_url"][0]
    try:
        if product_details["favorite"][0] == "on":
            favorite = 1
    except:
        favorite = 0
    try:
        with connection.cursor() as cursor:
            sql = f"insert into products values (null, '{title}', '{description}', {favorite}, {price}, '{img_url}', {category})"
            cursor.execute(sql)
            connection.commit()
            return_status = {"STATUS": "SUCCESS"}
            return return_status
    except:
        return_status = {"STATUS": "ERROR"}
        return return_status


def return_products():
    try:
        with connection.cursor() as cursor:
            sql = "select * from products"
            cursor.execute(sql)
            products = cursor.fetchall()
            return_data = {"STATUS": "SUCCESS", "PRODUCTS": products}
            return return_data
    except:
        return_data = {"STATUS": "ERROR", "PRODUCTS": products}
        return return_data


def return_products_by_category(category_id):
    try:
        with connection.cursor() as cursor:
            sql = f"select * from products where category_id = {category_id}"
            cursor.execute(sql)
            products = cursor.fetchall()
            return_data = {"STATUS": "SUCCESS", "PRODUCTS": products}
            return return_data

    except:
        return_data = {"STATUS": "ERROR", "PRODUCTS": products}
        return return_data

def get_products():
    try:
        with connection.cursor() as cur:
            sql = "Select * From Products"
            cur.execute(sql)
            products = cur.fetchall()
            result = {'STATUS':"SUCCESS", "PRODUCTS":products}
            return result
    except:
        result = {'STATUS': "ERROR", 'MSG': "Internal Error"}
        return result

def get_product(id):
    try:
        with connection.cursor() as cur:
            sql = "Select * From Products Where id = {}".format(id)
            cur.execute(sql)
            data = cur.fetchall()
            result = {'Status': "Success", 'data':data}
            return result
    except:
        result = {'STATUS':"ERROR", 'MSG': "Product not found"}
        return result

def delete_product(id):
    try:
        with connection.cursor() as cur:
            sql = "Delete From Products Where id = {}".format(id)
            cur.execute(sql)
            connection.commit()
            result = {'Status': "Success"}
            return result
    except:
        result = {'STATUS':"ERROR", 'MSG': "Product Not Deleted due to an Error"}
        return result

def products_by_category(id):
    try:
        with connection.cursor() as cur:
            sql = "Select * From Products Where category = {}".format(id)
            cur.execute(sql)
            data = cur.fetchall()
            result = {'STATUS':"SUCCESS","PRODUCTS":data}
            return result
    except:
        result = {'STATUS':"ERROR", 'MSG': "Error"}
        return result
