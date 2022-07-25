from .ipcq import QueueManager


class QueueManagerClient(QueueManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connect()


if 'get_queue' not in QueueManagerClient._registry:
    QueueManagerClient.register('get_queue')
