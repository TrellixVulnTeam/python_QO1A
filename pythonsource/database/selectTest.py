import pymysql

try:
    db = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="12345",
        db="ecommerce",
        charset="utf8",
    )

    cursor = db.cursor()

    sql = """
        select * from product
    """

    cursor.execute(sql)

    rows = cursor.fetchall()

    for r in rows:
        print("{}\t{}\t{}\t{}".format(r[0], r[1], r[2], r[3]))
        print(r)

except Exception as e:
    print(e)
finally:
    db.close()
