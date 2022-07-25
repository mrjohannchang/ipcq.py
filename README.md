# ipcq

A simple inter-process communication (IPC) Queue built on top of the built-in library [multiprocessing](https://docs.python.org/3/library/multiprocessing.html).

![](examples/showcase.gif)

* [Quick Start](#quick-start)
* [API](#api)
    + [class ipcq.**QueueManagerServer**(*address*: Optional[str], *authkey*: Optional[bytes])](#class-ipcqqueuemanagerserveraddress-optionalstr-authkey-optionalbytes)
        - [def **get_queue**(*ident*: Union[AnyStr, int, type(None)] = None) -> queue.Queue](#def-get_queueident-unionanystr-int-typenone--none---queuequeue)
    + [class ipcq.**QueueManagerClient**(*address*: Optional[str], *authkey*: Optional[bytes])](#class-ipcqqueuemanagerclientaddress-optionalstr-authkey-optionalbytes)
        - [def **get_queue**(*ident*: Union[AnyStr, int, type(None)] = None) -> queue.Queue](#def-get_queueident-unionanystr-int-typenone--none---queuequeue-1)

## Quick Start

**Server**

```
import ipcq


with ipcq.QueueManagerServer(address=ipcq.Address.DEFAULT, authkey=ipcq.AuthKey.DEFAULT) as server:
    server.get_queue().get()
```

**Client**

```
import ipcq


client = ipcq.QueueManagerClient(address=ipcq.Address.DEFAULT, authkey=ipcq.AuthKey.DEFAULT)
client.get_queue().put('a message')
```

Please checkout out the [examples](examples) folder for more examples.

## API

### class ipcq.**QueueManagerServer**(*address*: Optional[str], *authkey*: Optional[bytes])

This class inherits [multiprocessing.managers.BaseManager](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager).

*address* can be `ipcq.Address.AUTO`, `ipcq.Address.CWD` or any other path described in `str`.
When it's given `ipcq.Address.AUTO`, a random address will be chosen.
`ipcq.Address.CWD` means using a file that lives in the current working directory.

*authkey* is just like the password for authentication. It can be `ipcq.AuthKey.AUTO`, `ipcq.AuthKey.DEFAULT`, `ipcq.AuthKey.EMPTY` or any other arbitrary `bytes`.

#### def **get_queue**(*ident*: Union[AnyStr, int, type(None)] = None) -> queue.Queue

The method returns a `queue.Queue` corresponding with *ident*.
The returned queue is shared between the server and the client.
So both the server and the client access to the same queue.

*ident* is the identity, it can be any string-like object, `int` or `None`.
The default is `None`.
It is used for differetiate the obtained queues.
Different *ident*s refer to different queues.

### class ipcq.**QueueManagerClient**(*address*: Optional[str], *authkey*: Optional[bytes])

This class inherits [multiprocessing.managers.BaseManager](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager).

*address* can be `ipcq.Address.CWD` or any other path described in `str`.
When the server is set with `ipcq.Address.CWD` and the client is running in the same CWD that the server runs, the client can be set with `ipcq.Address.CWD` as well.
Otherwise, it should be the same with the *address* field in the server instance.

*authkey* is just like the password for authentication. It has to be the same with what's set on the server .
If the server was set with `ipcq.AuthKey.DEFAULT` or `ipcq.AuthKey.EMPTY`, the client can just be set with the same.

#### def **get_queue**(*ident*: Union[AnyStr, int, type(None)] = None) -> queue.Queue

The method returns a `queue.Queue` corresponding with *ident*.
The returned queue is shared between the server and the client.
So both the server and the client access to the same queue.

*ident* is the identity, it can be any string-like object, `int` or `None`.
The default is `None`.
It is used for differetiate the obtained queues.
Different *ident*s refer to different queues.
