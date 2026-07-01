from calculator import calculate_gp, calculate_cgpa


def course_details():
    """Collect course details from the user and return them as a list of dictionaries."""
    courses = []
    num_of_courses = int(input("How many courses are you offering? "))

    for _ in range(num_of_courses):
        course_code = input("Enter course code (e.g. MTH101): ")
        course_unit = int(input(f"Enter course unit for {course_code}: "))

        if course_unit == 0:
            print("Error .Course unit cannot be zero.")
            continue

        course_grade = input("Enter your grade: ")
        courses.append({
            "course_code": course_code,
            "course_units": course_unit,
            "grade": course_grade,
        })

    return courses


def main():
    print("Calculate your GP & CGPA\ninstantly and correctly.")
    semester1_courses = course_details()
    gpa = calculate_gp(semester1_courses)

    total_units = sum(course["course_units"] for course in semester1_courses)
    print("Calculation complete")
    print(f"Your GPA is \n{semester1_gpa}\nout of 5.00\nBased on {len(semester1_courses)} courses and {total_units} total units")
    print("Ready to lock in your GPA?\nTrack your progress, study rigorously, and have a blast in all your courses.")

    check_cgpa = input("Do you want to check your cumulative grade point average for the session? (y/n): ")
    if check_cgpa.lower() == "y":
        semester2_courses = course_details()
        cgpa = calculate_cgpa(semester1_courses, semester2_courses)
        print(f"Your CGPA for the session is \n{cgpa}")


if __name__ == "__main__":
    main()
