from setuptools import setup

setup(
    name='hdmi-control',
    version='0.1',
    py_modules=[
        'app',
        'codes',
        'log_config',
        'dicto',
        'config',
    ],
    include_package_data=True,
    install_requires=[
        'pySerial',
        'click',
    ],
    entry_points='''
        [console_scripts]
        hdmictl=app:cli
    ''',
)
