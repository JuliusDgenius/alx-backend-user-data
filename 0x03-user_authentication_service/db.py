#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session

from user import Base, User

attrs = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a user
        """
        user = User(email=email, hashed_password=hashed_password)

        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Returns the first row found in the `users` table.
        """
        # if not kwargs:
        #     raise InvalidRequestError("No parameter provided")
        # try:
        #     return self.__session.query(User).filter_by(**kwargs).one()
        # except NoResultFound:
        #     raise NoResultFound("No result found for the parameter")
        # except Exception as e:
        #     raise InvalidRequestError(f"Invalid parameter {e}")
        # finally:
        #     self.__session.close()
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates a user.
        """
        # user = self.find_user_by(id=user_id)
        # if user:
        #     try:
        #         for key, value in kwargs.items():
        #             user.key = value
        #         self.__session.commit()
        #     except ValueError:
        #         print('user has no attribute', key)

        user = self.find_user_by(id=user_id)
        for key, val in kwargs.items():
            if key not in attrs:
                raise ValueError
            setattr(user, key, val)
        self._session.commit()
        return None
