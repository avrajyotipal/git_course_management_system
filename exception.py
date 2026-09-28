class CourseManagementException(Exception):
    """Base exception for the Course Management System."""
    pass


class InvalidEmailException(CourseManagementException):
    """Raised when an invalid email is provided."""
    pass


class DuplicateCourseException(CourseManagementException):
    """Raised when a course already exists."""
    pass


class CourseNotFoundException(CourseManagementException):
    """Raised when a course cannot be found."""
    pass


class EnrollmentException(CourseManagementException):
    """Raised when enrollment fails."""
    pass


class UserNotFoundException(CourseManagementException):
    """Raised when a user cannot be found."""
    pass