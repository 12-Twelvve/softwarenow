# Question 3 
# Write a program that asks the user how many students are in the class (minimum 3, 
# maximum 10). For each student, input their name and score (0-100). Calculate and 
# display:  
# • Each student's grade (HD: 85-100, D: 75-84, C: 65-74, P: 50-64, F: 0-49).  
# • Class average 
# • Highest and lowest score and student name 
# • Lowest score and student name 
 
# Example: 
# How many students? 3 
# Student 1 name: Alice 
# Alice's score: 78 
# Student 2 name: Bob 
# Bob's score: 92 
# Student 3 name: Carol 
# Carol's score: 45 
 
# Results: 
# Alice: 78 (D) 
# Bob: 92 (HD) 
# Carol: 45 (F) 
 
# Average score: 71.67 
# Highest: Bob (92) 
# Lowest: Carol (45)

def get_grade(score):
    if 85 <= score <= 100:
        return 'HD'
    elif 75 <= score < 85:
        return 'D'
    elif 65 <= score < 75:
        return 'C'
    elif 50 <= score < 65:
        return 'P'
    else:
        return 'F'
def main():
    num_students = int(input("How many students? "))
    if num_students < 3 or num_students > 10:
        print("Number of students must be between 3 and 10.")
        return
    students = []
    for i in range(num_students):
        name = input(f"Student {i + 1} name: ")
        score = int(input(f"{name}'s score: "))
        students.append((name, score))
    print("\nResults:")
    total_score = 0
    highest_student = ("", -1)
    lowest_student = ("", 101)
    for name, score in students:
        grade = get_grade(score)
        print(f"{name}: {score} ({grade})")
        total_score += score
        if score > highest_student[1]:
            highest_student = (name, score)
        if score < lowest_student[1]:
            lowest_student = (name, score)
    average_score = total_score / num_students
    print(f"\nAverage score: {average_score:.2f}")
    print(f"Highest: {highest_student[0]} ({highest_student[1]})")
    print(f"Lowest: {lowest_student[0]} ({lowest_student[1]})")