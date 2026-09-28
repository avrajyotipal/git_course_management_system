from exception import DuplicateCourseException
from logging_config import get_logger


logger = get_logger(__name__)


class Course:

    course_count = 0

    def __init__(self, course_id, title, description):
        self.__course_id = course_id
        self.__title = title
        self.__description = description
        self.__students = []

        Course.course_count += 1

        logger.info(
            "Course created: %s - %s",
            self.__course_id,
            self.__title
        )

    @property
    def course_id(self):
        return self.__course_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    # Encapsulation

    def add_student(self, student):

        if student in self.__students:
            logger.warning(
                "%s is already registered for %s",
                student.name,
                self.title
            )

            raise DuplicateCourseException(
                f"{student.name} is already registered "
                f"for {self.title}"
            )

        self.__students.append(student)

        logger.info(
            "%s added to course %s",
            student.name,
            self.title
        )

    def get_students(self):
        return self.__students.copy()

    # Static method

    @staticmethod
    def generate_course_id(title):
        cleaned_title = title.upper().replace(" ", "-")
        return f"CRS-{cleaned_title[:10]}"

    # Class method

    @classmethod
    def create_course(cls, title, description):
        course_id = cls.generate_course_id(title)

        logger.info(
            "Creating course using class method: %s",
            title
        )

        return cls(
            course_id,
            title,
            description
        )

    def display_course(self):

        print("\n--- Course Details ---")
        print(f"Course ID   : {self.course_id}")
        print(f"Title       : {self.title}")
        print(f"Description : {self.description}")
        print(f"Students    : {len(self.__students)}")