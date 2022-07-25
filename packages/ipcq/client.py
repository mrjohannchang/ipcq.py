from .ipcq import QueueManager


class QueueManagerClient(QueueManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connect()


if not 'get_queue' in QueueManagerClient._registry:
    QueueManagerClient.register('get_queue')
