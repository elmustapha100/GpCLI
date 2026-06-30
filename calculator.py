from grading import convert_grade_point 

def calculate_gp(courses :list[dict]): 
    """
    Args :  Calculate GPA for a single semester.
 
    Each course dict must have:
     'units' (int): credit units
    'grade' (str): letter grade e.g. 'A', 'B'

    Return : GPA to 2 decimal place."""
    total_course_unit = 0 
    total_points = 0 

    for course in courses : 
        course_units = course['course_units']
        # grade = course["grade"].upper()
        grade_point = convert_grade_point(course["grade"])

        total_points += course_units * grade_point
        total_course_units += course_units

    if total_units == 0 :
        return 0

    return round((total_points/total_course_units), 2)

#Calculating for Cumulative grade point average 
def calculate_cgpa(semester1_courses: list[dict], semester2_courses: list[dict]) :
    """
    Args : Calculate CGPA across two semesters by pooling all courses together
    and applying the same weighted formula.
 
    Returns CGPA rounded to 2 decimal places.
    """
    all_courses = semester1_courses + semester2_courses
    return calculate_gpa(all_courses)    