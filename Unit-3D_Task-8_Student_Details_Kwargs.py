def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
student_details(name="anu", maths=85)
