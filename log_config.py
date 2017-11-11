import logging
import sys


if '-d' in [i for i in sys.argv[1:]]:
    level = logging.DEBUG
else:
    level = logging.INFO


log = logging.getLogger('hdmi-rs232')

log.setLevel(level)
sh = logging.StreamHandler(stream=sys.stdout)
sh.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    fmt='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
sh.setFormatter(formatter)
log.addHandler(sh)
