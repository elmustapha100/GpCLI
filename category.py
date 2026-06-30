def result_class(cgpa:float): 
# First Class Honours (CGPA: 4.50 - 5.00)
# Second Class Honours, Upper Division (CGPA: 3.50 - 4.49)
# Second Class Honours, Lower Division (CGPA: 2.40 - 3.49)
# Third Class Honours (CGPA: 1.50 - 2.39)
# Pass (CGPA: 1.00 - 1.49)


    if cgpa >= 4.50 : 
        return "First Class"
    elif cgpa >= 3.50:
        return "Second Class Upper"
    elif cgpa >= 2.40:
        return "Second Class Lower"
    elif cgpa >= 1.50:
        return "Third Class"
    elif cgpa >= 1.00:
        return "Pass"
    else:
        return "Fail"

    if cgpa > 5.00 and cgpa < 1.00: 
        return "Invalid"    

