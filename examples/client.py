import os

import ipcq


qmc: ipcq.QueueManagerClient = ipcq.QueueManagerClient(address=ipcq.Address.CWD, authkey=ipcq.AuthKey.DEFAULT)
qmc.connect()

message: str = f"A message from {os.getpid()}"
qmc.get_queue().put(message)
print(f"[SENT] {message}")
