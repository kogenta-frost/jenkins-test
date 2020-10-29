try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup
setup(
    name='campus_clarity',
    version='0.1',
    packages=['campus_clarity', 'campus_clarity.tests'],
    license='MIT',
    description='package for processing Parchment transcript requests',
    install_requires=['configparser', 'ldap3', 'paramiko', 'pyodbc', 'pyyaml', 'SQLAlchemy', 'scp'],
    python_requires='>=3',
    url='http://github.com/kogenta-frost/jenkins-test.git',
    author='Mike Kromarek',
    author_email='mkromarek@highline.edu'
)