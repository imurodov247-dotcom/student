from student.models import Student



    
    
def add_three_students():
    students_data = [
{"name": "Ali", "yoshi": 19, "kurs": 1, "guruhi": "A1", "universitet": "Toshkent Universiteti"},
{"name": "Laylo", "yoshi": 20, "kurs": 2, "guruhi": "B2", "universitet": "Fargona Universiteti"},
{"name": "Karim", "yoshi":17, "kurs" :1 , "guruhi" : "C1", "universitet":"Admi"}
    ]

    
def get_first_year_students():
        return Student.objects.filter(kurs=1)
    
    
    
    
def delete_under_18():

    qs = Student.objects.filter(age__lt=18)
    deleted_info = qs.delete() 
    return deleted_info


def change_ali_to_alijon():
    updated_count = Student.objects.filter(name__iexact='ali').update(name='Alijon')
    return updated_count


def run():
    print("funksiya ishlayapti")
    