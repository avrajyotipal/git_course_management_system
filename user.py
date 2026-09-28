user.py

from abc import ABC, abstractmethod
from exception import InvalidEmailException
from logging_config import get_logger


logger = get_logger(__name__)


class User(ABC):

    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name

        if not self.validate_email(email):
            logger.error("Invalid email provided: %s", email)
            raise InvalidEmailException(
                f"Invalid email address: {email}"
            )

        self.__email = email

        logger.info(
            "User created: %s (%s)",
            self.__name,
            self.__user_id
        )

    # Encapsulation through getters

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    # Static method

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email.split("@")[-1]

    # Abstract method

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def display_profile(self):
        pass