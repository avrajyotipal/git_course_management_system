from user import User
from exception import EnrollmentException
from logging_config import get_logger


logger = get_logger(__name__)


class Student(User):

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

        self.__courses = []

        logger.info(
            "Student created: %s",
            self.name
        )

    # Polymorphism

    def get_role(self):
        return "Student"

    def display_profile(self):
        print("\n--- Student Profile ---")
        print(f"ID      : {self.user_id}")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"Courses : {len(self.__courses)}")

    # Instance method

    def enroll(self, course):
        if course in self.__courses:
            logger.warning(
                "%s is already enrolled in %s",
                self.name,
                course.title
            )

            raise EnrollmentException(
                f"{self.name} is already enrolled in "
                f"{course.title}"
            )

        self.__courses.append(course)

        logger.info(
            "%s enrolled in course %s",
            self.name,
            course.title
        )

    def get_courses(self):
        return self.__courses.copy()

    # Class method

    @classmethod
    def create_student(cls, user_id, name, email):
        logger.info(
            "Creating student using class method: %s",
            name
        )

        return cls(user_id, name, email)