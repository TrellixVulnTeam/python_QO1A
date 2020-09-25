import pymysql

try:
    db = pymysql.Connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "12345",
        db = "ecommerce",
        charset = "utf8",
    )

    cursor = db.cursor()

    sql = """
        delete from product
        where product_code='21567340'
    """

    if cursor.execute(sql):
        db.commit()
        print("삭제 성공")
        print(cursor.rowcount)   # rowcount : sql 쿼리 실행 결과

except Exception as e:
    print(e)
finally:
    db.close()
