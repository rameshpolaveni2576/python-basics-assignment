def calculate_total(marks):
    total=sum(marks)
    """returns sum of all marks in the list"""
    return total  
def calculate_average(marks):
    """returns the avarage of marks using calculate_total() function"""
    total=calculate_total(marks)
    average=total/len(marks)
    return average
def get_grade(average):
    """returns the Grade based on average"""
    if average>90:
        return "A"
    elif average>75:
        return "B"
    else:
        return "C"
def display_report(marks):
    """Display the Total,Avarage and Grade for the given marks"""
    Total=calculate_total(marks)
    Average=calculate_average(marks)
    Grade=get_grade(Average)
    print(f"Total: {Total}\nAverage: {Average}\nGrade: {Grade}")

display_report([88,76,95,60,82])