# ipcq

A simple inter-process communication (IPC) Queue built on top of the built-in library [multiprocessing](https://docs.python.org/3/library/multiprocessing.html).

## Quick Start

### On the server side

```
import ipcq


with ipcq.QueueManagerServer(address=ipcq.Address.DEFAULT, authkey=ipcq.AuthKey.DEFAULT) as server:
  server.get_queue().get()
```

### On the client side

```
import ipcq


client = ipcq.QueueManagerClient(address=ipcq.Address.DEFAULT, authkey=ipcq.AuthKey.DEFAULT)
client.get_queue().put('a message')
```

## Example

Please checkout out the [examples](examples) folder.

## API

### class ipcq.QueueManagerServer

#### Constructor

The same with [multiprocessing.managers.BaseManager](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager), please refer to it.

#### Methods

All methods in [multiprocessing.managers.BaseManager](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager) are inherited.
The followings are the addtions.

##### get_queue(ident: Optional[Union[AnyStr, int, type(None)]] = None) -> queue.Queue

`ident` is the identity, it can be string-like objects, `int` or `None`. The default is `None`. This is for differetiate the obtained queues.

Return a queue corresponded with then `ident`.

### class ipcq.QueueManagerClient

#### Constructor

The same with [multiprocessing.managers.BaseManager](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager), please refer to it.

#### Methods

All methods in [multiprocessing.managers.BaseManager](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager) are inherited.
The followings are the addtions.

##### get_queue(ident: Optional[Union[AnyStr, int, type(None)]] = None) -> queue.Queue

`ident` is the identity, it can be string-like objects, `int` or `None`. The default is `None`. This is for differetiate the obtained queues.

Return a queue corresponded with then `ident`.
