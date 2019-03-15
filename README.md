# 🐰IBnator - A Tool for Security Analysts 🐰

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


----


## License

When making a reference to my work, please use my [website](http://bt3gl.github.io/index.html).

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
