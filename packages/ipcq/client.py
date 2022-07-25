from .ipcq import QueueManager


class QueueManagerClient(QueueManager):
    pass


if not 'get_queue' in QueueManagerClient._registry:
    QueueManagerClient.register('get_queue')
