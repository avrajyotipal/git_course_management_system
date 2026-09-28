from datetime import datetime

from exception import EnrollmentException
from logging_config import get_logger


logger = get_logger(__name__)


class Enrollment:

    enrollment_count = 0

    def __init__(self, student, course):
        self.__student = student
        self.__course = course
        self.__enrollment_date = datetime.now()

        Enrollment.enrollment_count += 1

        logger.info(
            "Enrollment created: %s -> %s",
            student.name,
            course.title
        )

    @property
    def student(self):
        return self.__student

    @property
    def course(self):
        return self.__course

    @property
    def enrollment_date(self):
        return self.__enrollment_date

    def enroll_student(self):

        try:
            self.__student.enroll(self.__course)
            self.__course.add_student(self.__student)

            logger.info(
                "Enrollment successful: %s -> %s",
                self.__student.name,
                self.__course.title
            )

        except Exception as error:

            logger.error(
                "Enrollment failed: %s",
                error
            )

            raise EnrollmentException(
                f"Unable to enroll "
                f"{self.__student.name} "
                f"in {self.__course.title}"
            ) from error

    def display_enrollment(self):

        print("\n--- Enrollment ---")
        print(f"Student : {self.student.name}")
        print(f"Course  : {self.course.title}")
        print(
            f"Date    : "
            f"{self.enrollment_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )