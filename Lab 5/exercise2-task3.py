students = [
[201, "Amina", [78, 85, 90]],
[202, "Rahim", [65, 70, 68]],
[203, "Nadia", [92, 88, 95]],
[204, "Hasan", [55, 60, 65]],
[205, "Tania", [80, 80, 80]]
 ]
def calculate_average(marks):
    if len(marks)==0:
        return None
    total = sum(marks)
    average= total/len(marks)
    return average
 
def classify_performance(average):
    if average >=80:
        return "Excellent"
    elif average >=70:
        return "Good"
    elif average >=60:
        return " Satisfactory"
    else :
        return "Needs Improvement"
 
def  display_report(students):
    for x in students:
        student_id = x[0]
        student_name=x[1]
        marks = x[2]
        average =calculate_average(marks)
        print("Id:",student_id)
        print("Name: ",student_name)
        print("Average: ", average)
        print("Performace: ",classify_performance(average) )
display_report(students)