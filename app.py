#!/home/eburt/.virtualenvs/hdmi-rs232/bin/python


import serial
from log_config import log, logging
from codes import ports
import click
import time
from config import DefaultConfig


def serial_setup(port='/dev/ttyUSB0'):
    cfg = DefaultConfig()
    com = serial.Serial(**cfg)
    log.debug(com)
    com.flush()
    return com


def loglevelset(debug):
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)


@click.group()
def cli():
    pass


@cli.command('test')
@click.option('--debug', '-d', is_flag=True, default=False)
def function_test(debug):
    loglevelset(debug)
    com = serial_setup()
    p = [i for i in ports.values()]
    p.sort()
    log.debug(str(p))

    for k, v in enumerate(p):
        log.info('Switching to port: {0}'.format(k + 1))
        log.info('Using hex code: {0}'.format(v.encode('hex')))
        com.write(v)
        log.info(com.in_waiting)
        log.info(com.read(com.in_waiting).encode('hex'))
        log.info(com.read(com.in_waiting).encode('hex'))
        time.sleep(2)
    com.close()



@cli.command('switch')
@click.argument('port')
@click.option('--debug', '-d', is_flag=True, default=False)
def hdmi_input_switch(port, debug):
    loglevelset(debug)
    com = serial_setup()
    com.reset_input_buffer()
    com.reset_output_buffer()
    code = ports['p0{0}'.format(int(port))]
    com.write(code)
    log.info('Activated port {0}'.format(int(port)))
    log.debug(com.in_waiting)
    log.debug(com.read(com.in_waiting).encode('hex'))
    log.debug(com.read(com.in_waiting).encode('hex'))
    # com.flush()
    com.write(code)

    log.debug(com.in_waiting)
    log.debug(com.read(com.in_waiting).encode('hex'))
    log.debug(com.read(com.in_waiting).encode('hex'))
    com.close()


@cli.command('reboot')
@click.option('--debug', '-d', is_flag=True, default=False)
def hdmi_device_reboot(debug):
    loglevelset(debug)
    com = serial_setup()
    com.dsrdtr = True
    com.rtscts = True
    com.break_condition = True
    com.send_break()

if __name__ == '__main__':
    cli()
