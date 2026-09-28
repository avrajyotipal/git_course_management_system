from user import User
from logging_config import get_logger


logger = get_logger(__name__)


class Mentor(User):

    def __init__(self, user_id, name, email, specialization):
        super().__init__(user_id, name, email)

        self.__specialization = specialization
        self.__courses = []

        logger.info(
            "Mentor created: %s",
            self.name
        )

    @property
    def specialization(self):
        return self.__specialization

    # Polymorphism

    def get_role(self):
        return "Mentor"

    def display_profile(self):
        print("\n--- Mentor Profile ---")
        print(f"ID             : {self.user_id}")
        print(f"Name           : {self.name}")
        print(f"Email          : {self.email}")
        print(f"Specialization : {self.specialization}")
        print(f"Courses        : {len(self.__courses)}")

    # Instance method

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

            logger.info(
                "Course %s assigned to mentor %s",
                course.title,
                self.name
            )

    def get_courses(self):
        return self.__courses.copy()

    # Class method

    @classmethod
    def create_mentor(
        cls,
        user_id,
        name,
        email,
        specialization
    ):
        logger.info(
            "Creating mentor using class method: %s",
            name
        )

        return cls(
            user_id,
            name,
            email,
            specialization
        )