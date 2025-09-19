# Grading System in Python

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    print("---- Grading System ----")
    subjects = int(input("Enter number of subjects: "))
    total_marks = 0

    for i in range(1, subjects + 1):
        mark = float(input(f"Enter marks for subject {i} (out of 100): "))
        total_marks += mark

    percentage = total_marks / subjects
    grade = calculate_grade(percentage)

    print("\n--- Result ---")
    print(f"Total Marks: {total_marks}/{subjects*100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
