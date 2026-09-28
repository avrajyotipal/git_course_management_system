from student import Student
from mentor import Mentor
from course import Course
from enrollment import Enrollment

from exception import (
    InvalidEmailException,
    EnrollmentException
)

from logging_config import get_logger


logger = get_logger(__name__)


def create_student():
    print("\n========== Create Student ==========")

    user_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    email = input("Enter student email: ")

    try:
        student = Student.create_student(
            user_id,
            name,
            email
        )

        print("\nStudent created successfully!")
        student.display_profile()

        return student

    except InvalidEmailException as error:
        print(f"\nError: {error}")
        return None


def create_mentor():
    print("\n========== Create Mentor ==========")

    user_id = input("Enter mentor ID: ")
    name = input("Enter mentor name: ")
    email = input("Enter mentor email: ")
    specialization = input("Enter specialization: ")

    try:
        mentor = Mentor.create_mentor(
            user_id,
            name,
            email,
            specialization
        )

        print("\nMentor created successfully!")
        mentor.display_profile()

        return mentor

    except InvalidEmailException as error:
        print(f"\nError: {error}")
        return None


def create_course():
    print("\n========== Create Course ==========")

    title = input("Enter course title: ")
    description = input("Enter course description: ")

    course = Course.create_course(
        title,
        description
    )

    print("\nCourse created successfully!")
    course.display_course()

    return course


def enroll_student(student, course):
    if student is None:
        print("\nPlease create a student first.")
        return

    if course is None:
        print("\nPlease create a course first.")
        return

    print("\n========== Enroll Student ==========")

    try:
        enrollment = Enrollment(
            student,
            course
        )

        enrollment.enroll_student()

        print("\nStudent enrolled successfully!")
        enrollment.display_enrollment()

    except EnrollmentException as error:
        print(f"\nEnrollment failed: {error}")


def display_student(student):
    if student is None:
        print("\nNo student has been created.")
        return

    student.display_profile()

    courses = student.get_courses()

    if courses:
        print("\nEnrolled Courses:")

        for course in courses:
            print(
                f"- {course.course_id}: "
                f"{course.title}"
            )
    else:
        print("\nNo courses enrolled.")


def display_mentor(mentor):
    if mentor is None:
        print("\nNo mentor has been created.")
        return

    mentor.display_profile()

    courses = mentor.get_courses()

    if courses:
        print("\nAssigned Courses:")

        for course in courses:
            print(
                f"- {course.course_id}: "
                f"{course.title}"
            )
    else:
        print("\nNo courses assigned.")


def display_course(course):
    if course is None:
        print("\nNo course has been created.")
        return

    course.display_course()

    students = course.get_students()

    if students:
        print("\nEnrolled Students:")

        for student in students:
            print(
                f"- {student.user_id}: "
                f"{student.name}"
            )
    else:
        print("\nNo students enrolled.")


def main():

    student = None
    mentor = None
    course = None

    while True:

        print("\n")
        print("=" * 55)
        print("        COURSE MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Create Student")
        print("2. Create Mentor")
        print("3. Create Course")
        print("4. Assign Course to Mentor")
        print("5. Enroll Student in Course")
        print("6. Display Student")
        print("7. Display Mentor")
        print("8. Display Course")
        print("9. Demonstrate Polymorphism")
        print("10. Display System Statistics")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":

                student = create_student()

            elif choice == "2":

                mentor = create_mentor()

            elif choice == "3":

                course = create_course()

            elif choice == "4":

                if mentor is None:
                    print("\nPlease create a mentor first.")

                elif course is None:
                    print("\nPlease create a course first.")

                else:
                    mentor.add_course(course)

                    print(
                        f"\nCourse '{course.title}' "
                        f"assigned to mentor "
                        f"'{mentor.name}'."
                    )

            elif choice == "5":

                enroll_student(
                    student,
                    course
                )

            elif choice == "6":

                display_student(student)

            elif choice == "7":

                display_mentor(mentor)

            elif choice == "8":

                display_course(course)

            elif choice == "9":

                print(
                    "\n========== Polymorphism =========="
                )

                users = []

                if student:
                    users.append(student)

                if mentor:
                    users.append(mentor)

                if not users:
                    print(
                        "Create a student or mentor first."
                    )
                else:
                    for user in users:
                        print(
                            f"{user.name} "
                            f"-> {user.get_role()}"
                        )

            elif choice == "10":

                print(
                    "\n========== System Statistics =========="
                )

                print(
                    f"Total Courses: "
                    f"{Course.course_count}"
                )

                print(
                    f"Total Enrollments: "
                    f"{Enrollment.enrollment_count}"
                )

            elif choice == "0":

                print(
                    "\nThank you for using "
                    "Course Management System."
                )

                logger.info(
                    "Application terminated by user."
                )

                break

            else:

                print(
                    "\nInvalid choice. "
                    "Please select a valid option."
                )

        except Exception as error:

            logger.exception(
                "Unexpected application error"
            )

            print(
                f"\nUnexpected error: {error}"
            )


if __name__ == "__main__":
    main()