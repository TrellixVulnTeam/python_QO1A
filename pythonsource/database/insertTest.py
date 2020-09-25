import pymysql

try:
    # mysql 접속
    db = pymysql.Connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "12345",
        db = "ecommerce",
        charset = "utf8",
    )
    # cursor 생성
    cursor = db.cursor()
    
    # sql 구문 생성
    sql = """
        insert into product values(
            '21567340',
            '스위트 바나 여름신상5900원~롱원피스티셔츠/긴팔/반팔',
            23000,
            6900,
            70,
            'F'
        )
    """

    # sql 실행
    str = "삽입성공" if cursor.execute(sql) else "삽입실패"
    print(str)

    # commit
    db.commit()

except Exception as e:
    print(e)
finally:
    db.close()
