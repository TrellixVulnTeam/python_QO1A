import pymysql

try:
    conn = pymysql.Connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "12345",
        db = "ecommerce",
        charset = "utf8",
    )
    print("연결성공")
except Exception as e:
    print(e)

