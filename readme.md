# Monoprice 8x1 RS232 Control #


## Installation ##

1. Clone this repo: `git clone git@github.com:kurohai/hdmi-control.git`
1. Install with pip: `pip install --editable .`


## Usage ##

Must use superuser to connect to device.


### Activate Ports ###

```bash
# show help
sudo hdmictl --help

# syntax
sudo hdmictl switch <port 1-8> [--debug, -d]

# activate port 3
sudo hdmictl switch 3
```


### Test All Ports ###

```bash
sudo hdmictl test
```
