# 클래스가 필요한 이유

# 학생 3명의 정보를 다룬다면?
# 학생 : 이름, 학번, 학년, 성별, 점수1, 점수2

# 학생1
# 이름 리스트 생성
student_names_list = ["Kim", "Park", "Cho"]
# 학번 리스트 생성
student_number_list = [1, 2, 3]
# 학년 리스트 생성
student_grade_list = [1, 2, 3]
# 상세정보 리스트 생성
student_detail_list = [
    {"gender" : "male", "score1" : 95, "score2" : 88},
    {"gender" : "female", "score1" : 75, "score2" : 68},
    {"gender" : "male", "score1" : 99, "score2" : 89}
]

print(student_names_list)
print(student_number_list)
print(student_grade_list)
print(student_detail_list)

# for문
for i in range(3):
    print(
        "이름 : {}, 학번 : {}, 학년 : {}, 학생정보 : {}".format(
            student_names_list[i],
            student_number_list[i],
            student_grade_list[i],
            student_detail_list[i],
        )
    )


