import multiprocessing.managers
import os
from typing import AnyStr, Union


class QueueManager(multiprocessing.managers.BaseManager):

    def get_queue(self, ident: Union[AnyStr, int, type(None)] = None) -> multiprocessing.Queue:
        pass


class Address:
    AUTO: type(None) = None
    DEFAULT: str = os.path.join(os.getcwd(), f".{os.path.basename(__package__)}")


class AuthKey:
    AUTO: type(None) = None
    DEFAULT: bytes = os.path.join(os.getcwd(), os.path.basename(__package__)).encode()
