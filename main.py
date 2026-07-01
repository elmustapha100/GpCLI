from grading import convert_grade_point
from calculator import calculate_gp, calculate_cgpa
from category import result_class

def course_details():
    """course details input from user
    Args : a key-value pair collection in a list 
    
    Return : courses based on input from users """
    courses = []
    num_of_courses = int(input("How many courses are you offering ? "))
    for i in range(num_of_courses) :
        course_code = input("Enter course code (e.g MTH 101) : ")
        course_unit = int(input(f"Enter course unit for {course_code} : "))
        try : 
            if course_unit == 0 :
                raise Exception ("\n Error.")
        except Exception as e :
            print(e)        

        course_grade = input(f"Enter your grade : ")
        """storing the course details as a dict"""
        courses.append({
            "course_code" : course_code,
            "course_unit" : course_unit,
            "course_grade" : course_grade,
        })

    return courses     
        
def main():
    print("Calculate your GP & CGPA\ninstantly and correctly.")    
    semester1_courses = course_details()
    semester1_gpa = calculate_gp(semester1_courses)

    print("Calculation complete")
    print(f"Your GPA is \n {semester1_gpa}\n out of 5.00\n Based on {num_of_courses}.{total_course_unit} total units ")
    print("Ready to lock in your GPA ?\n Track your progress , Study rigorously\n and have a blast in all your courses.")

    """If users want to check for CGPA in an academic session"""
    check_cgpa = input("Do you want to check your cumulative grade point average for the session ? (y/n)")
    if check_cgpa == "y": 
        semester2_courses = course_details()
        cgpa = calculate_cgpa(semester1_courses , semester2_courses)
        print(f"Your CGPA for the session is \n {cgpa}")

if __name__ == "__main__":
    main()     
