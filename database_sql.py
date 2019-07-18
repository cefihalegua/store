import pymysql

db = {
    "last_category_id": 0
}

connection = pymysql.connect(
        host="localhost",
        user="root",
        password="ch",       # the password section should be adapted accordingly
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