grade_point = {
        "A" : 5 ,
        "B" : 4 ,
        "C" : 3,
        "D" : 2,
        "E" : 1 ,
        "F" : 0 ,
    }

def convert_grade_point(grade):
    """Convert grade letter to its equivalent point value"""
    grade = grade.strip().upper()
    if grade not in grade_point : 
        raise ValueError(f"Invalid grade '{grade}'.Instead use {" ,".join(grade_point.keys())}  ")
    return grade_point[grade]    