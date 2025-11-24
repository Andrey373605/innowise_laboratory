from typing import List, Dict, Optional, Tuple, Union


def validate_student_name(name: str) -> bool:
    """
    Validate that student name contains only letters.

    Args:
        name: Student name to validate

    Returns:
        True if name is valid, False otherwise
    """
    return name.isalpha()


def validate_grade(grade: float) -> bool:
    """
    Validate that grade is within acceptable range.

    Args:
        grade: Grade value to validate

    Returns:
        True if grade is valid, False otherwise
    """
    return 0 <= grade <= 100


def find_student_by_name(
        students: List[Dict], name: str) -> Optional[Dict]:
    """
    Find student by name (case-insensitive search).

    Args:
        students: List of student dictionaries
        name: Name to search for

    Returns:
        Student dictionary if found, None otherwise
    """
    return next(
        (student for student in students
         if student["name"].lower() == name.lower()
         ),
        None
    )


def is_duplicate_student(
        students: List[Dict], name: str) -> bool:
    """
    Check if student with given name already exists.

    Args:
        students: List of student dictionaries
        name: Name to check

    Returns:
        True if duplicate exists, False otherwise
    """
    return any(student["name"].lower() == name.lower() for student in students)


def calculate_average(
        grades: List[float]) -> Optional[float]:
    """
    Calculate the average of a list of grades.

    Args:
        grades: List of numerical grades

    Returns:
        Average grade as float, or None if grades list is empty
    """
    if not grades:
        return None
    return sum(grades) / len(grades)


def calculate_summary_statistics(
        students: List[Dict]) -> Dict[str, Optional[float]]:
    """
    Calculate summary statistics for all students with grades.

    Args:
        students: List of student dictionaries

    Returns:
        Dictionary with highest, lowest, and overall averages
    """
    averages = []
    for student in students:
        avg = calculate_average(student["grades"])
        if avg is not None:
            averages.append(avg)

    if not averages:
        return {"highest": None, "lowest": None, "overall": None}

    return {
        "highest": max(averages),
        "lowest": min(averages),
        "overall": sum(averages) / len(averages)
    }


def find_top_performer_data(
        students: List[Dict]) -> Tuple[Optional[Dict], Optional[float]]:
    """
    Find the student with the highest average grade.

    Args:
        students: List of student dictionaries

    Returns:
        Tuple of (top_student_dict, average_grade) or (None, None)
        if no students with grades
    """
    students_with_grades = [
        student for student in students if student["grades"]
    ]

    if not students_with_grades:
        return None, None

    top_student = max(
        students_with_grades,
        key=lambda student: calculate_average(student["grades"]) or 0
    )

    top_avg = calculate_average(top_student["grades"])
    return top_student, top_avg


def get_student_name_input() -> str:
    """
    Get and return student name from user input.

    Returns:
        Trimmed student name string
    """
    return input("Enter student name: ").strip()


def get_grade_input() -> Tuple[str, Optional[float]]:
    """
    Get grade input from user.

    Returns:
        Tuple of (input_string, parsed_grade) where grade is None if invalid
    """
    grade_input = input("Grade: ").strip().lower()

    if grade_input == 'done':
        return grade_input, None

    try:
        grade = float(grade_input)
        return grade_input, grade
    except ValueError:
        return grade_input, None


def display_student_report(students: List[Dict]) -> None:
    """
    Display individual student averages.

    Args:
        students: List of student dictionaries
    """
    for student in students:
        avg = calculate_average(student["grades"])
        if avg is None:
            print(f"{student['name']}'s average grade is N/A")
        else:
            print(f"{student['name']}'s average grade is {avg:.2f}")


def display_summary_statistics(
        statistics: Dict[str, Optional[float]]) -> None:
    """
    Display summary statistics.

    Args:
        statistics: Dictionary with highest, lowest, and overall averages
    """
    if statistics["highest"] is None:
        print("No grades available for summary statistics.")
        return

    print("-"*30)
    print(f"Highest average: {statistics['highest']:.2f}")
    print(f"Lowest average: {statistics['lowest']:.2f}")
    print(f"Overall average: {statistics['overall']:.2f}")


def display_top_performer(
        top_student: Optional[Dict], top_avg: Optional[float]
) -> None:
    """
    Display top performer information.

    Args:
        top_student: Top student dictionary or None
        top_avg: Average grade of top student or None
    """
    if top_student is None:
        print("No students with grades available.")
        return

    print("\n--- Top Performer ---")
    print(f"The student with the highest average is {top_student["name"]}"
          f" with a grade of {top_avg:.2f}")


def create_new_student(
        name: str) -> Dict[str, Union[str, List[float]]]:
    """
    Create a new student dictionary.

    Args:
        name: Student name

    Returns:
        New student dictionary with empty grades list
    """
    return {"name": name, "grades": []}


def add_grades_to_student(student: Dict) -> None:
    """
    Add grades to a specific student through user input.

    Args:
        student: Student dictionary to add grades to
    """
    print(f"\nAdding grades for {student['name']}")
    print("Enter grades (0-100) or 'done' to finish:")

    grades_added = 0
    while True:
        grade_input, grade = get_grade_input()

        if grade_input == 'done':
            break

        if grade is None:
            print("Error: Invalid input! Please enter a number or 'done'.")
            continue

        if not validate_grade(grade):
            print("Error: Grade must be between 0 and 100!")
            continue

        student["grades"].append(grade)
        grades_added += 1
        print(f"Success: Grade {grade} added!")

    print(f"Completed: {grades_added} grades added for {student['name']}. "
          f"Total grades: {len(student['grades'])}")


def display_menu() -> None:
    """Display the main menu options for the Student Grade Analyzer."""
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")


def add_student(students: List[Dict]) -> None:
    """
    Add a new student to the system.

    Args:
        students: List of student dictionaries
    """
    name = get_student_name_input()

    if not validate_student_name(name):
        print("Error: Name should consist only of letters")
        return

    if is_duplicate_student(students, name):
        print(f"Error: Student '{name}' already exists!")
        return

    new_student = create_new_student(name)
    students.append(new_student)
    print(f"Success: Student '{name}' added successfully!")


def add_grades(students: List[Dict]) -> None:
    """
    Add grades for an existing student.

    Args:
        students: List of student dictionaries
    """
    if not students:
        print("Error: No students available. Please add students first.")
        return

    name = get_student_name_input()
    student = find_student_by_name(students, name)

    if student is None:
        print(f"Error: Student '{name}' not found!")
        return

    add_grades_to_student(student)


def show_report(students: List[Dict]) -> None:
    """
    Display comprehensive report of all students and summary statistics.

    Args:
        students: List of student dictionaries
    """
    if not students:
        print("No students available.")
        return

    print("--- Student Report ---")
    display_student_report(students)

    statistics = calculate_summary_statistics(students)
    display_summary_statistics(statistics)


def find_top_performer(students: List[Dict]) -> None:
    """
    Find and display the student with the highest average grade.

    Args:
        students: List of student dictionaries
    """
    if not students:
        print("Error: No students available.")
        return

    top_student, top_avg = find_top_performer_data(students)
    display_top_performer(top_student, top_avg)


def main() -> None:
    """
    Main program function for Student Grade Analyzer.

    Handles the main program loop and menu navigation.
    """
    students: List[Dict] = []

    print("Welcome to Student Grade Analyzer!")

    while True:
        display_menu()

        try:
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                add_student(students)
            elif choice == '2':
                add_grades(students)
            elif choice == '3':
                show_report(students)
            elif choice == '4':
                find_top_performer(students)
            elif choice == '5':
                print("Thank you for using Student Grade Analyzer. "
                      "Goodbye!")
                break
            else:
                print("Error: Invalid choice! "
                      "Please enter a number between 1-5.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
