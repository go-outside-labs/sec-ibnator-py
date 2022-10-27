# IBnator - A Tool for Security Analysts 

<br>

## Installing

Create and activate a virtual environment, installing dependences:

```
$ make venv
```

Install IBnator (this will install the binary at `/usr/local/bin/IBnator`):

```
$ make install
```

API keys:
* For Duo requests: `duoadminapi_ikey` and `duoadminapi_skey`.
* For Slack requests.


## Usage

```
$ IBnator -h

usage: IBnator [-h] [-d] [-p] [-a]

optional arguments:
 -h, --help            Show this help message and exit
 -d, --duo_lockout     Use duo Admin API to determine which users are locked
 -p, --ping_locked_users
 -a, --alerts          Read alerts.
```

