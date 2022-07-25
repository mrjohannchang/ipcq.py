import multiprocessing
from typing import AnyStr, Dict, Union

from .ipcq import QueueManager

qs: Dict[Union[AnyStr, int, type(None)], multiprocessing.Queue] = dict()


class QueueManagerServer(QueueManager):
    pass


def get_queue(ident: Union[AnyStr, int, type(None)] = None) -> multiprocessing.Queue:
    global qs

    if ident not in qs:
        qs[ident] = multiprocessing.Queue()

    return qs[ident]


if 'get_queue' not in QueueManagerServer._registry:
    QueueManagerServer.register('get_queue', get_queue)
