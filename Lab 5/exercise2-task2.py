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
    avg= total/len(marks)
    return avg
def classify_performance(avg):
    if avg >=80:
        return "Excellent"
    elif avg >=70:
        return "Good"
    elif avg >=60:
        return " Satisfactory"
    else :
        return "Needs Improvement"
   
#print(calculate_average([78, 85, 90]))
print("Performance:",classify_performance(70))