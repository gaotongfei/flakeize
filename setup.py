from setuptools import setup

setup(
    name='flakeize',
    version='0.1.0',
    author='Taff Gao',
    author_email='gaotongfei199@gmail.com',
    url='https://github.com/gaotongfei/flakeize',
    py_modules=['flakeize'],
    install_requires=[
        'Click',
	'yapf'
    ],
    entry_points='''
        [console_scripts]
        flakeize=flakeize:cli
    ''',
)
