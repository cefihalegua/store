import pymysql

db = {
    "last_category_id": 0
}

connection = pymysql.connect(
        host="localhost",
        user="root",
        password="codeforPRES413!",       # the password section should be adapted accordingly
        db="store",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )


def insert_category(cat_name):
    with connection.cursor() as cursor:
        cat_id = db["last_category_id"] + 1
        sql = f"insert into categories values({cat_id}, '{cat_name}')"
        try:
            cursor.execute(sql)
            db["last_category_id"] = cursor.lastrowid
            connection.commit()
            result = {
                "STATUS": "SUCCESS",
                "CAT_ID": cat_id,
                "CAT_NAME": cat_name
            }
            return result
        except:
            return {
                "STATUS": "ERROR",
                "MSG": "Problem with database"
            }


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