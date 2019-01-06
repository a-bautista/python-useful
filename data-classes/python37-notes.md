## Installing Python 3.7 and using pyenv

Based on the post from stackoverflow you need to execute the following commands to get up and running Python 3.7.0. (Linux Mint)

`sudo apt-get update`
`sudo apt-get upgrade`
`sudo apt-get dist-upgrade`
`sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus`
`sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev`
`sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev`
`sudo apt-get install libssl-dev openssl`
`sudo apt-get install libffi-dev`

`./configure`
`make`
`sudo make altinstall`

### Installing `##pyenv`

`curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`

### Testing pyenv

`pyenv install 3.7.0` # install a new version in Linux
`pyenv versions`      # see the current versions

### Working with pyenv

Suppose you want to work with a specific version of Python for a project. What you can do is to set a .python-version file and then
execute the main.py file with that particular version of python.

`vi main.py`                # type in this file a hello world program
`pyenv local 3.7.0`         # set the local python version to be 3.7.0
`pyenv exec python main.py` # this will execute the python file with the 3.7.0 version

### Setting up a virtual environment with pyenv

You can create a virtual environment with a specific version of Python by first setting up the Python version you want and then using that
version to create your virtual environment, that is,

`pyenv local 3.7.0`             # set the local version to 3.7.0
`pyenv exec python -m venv env` # create the virtual environment with Python 3.7.0

With the commands from above you can have different virtual environments in various Python versions.

### virtualenvwrapper

export PATH="/home/alexbr/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"



References:

https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul 
https://realpython.com/python-virtual-environments-a-primer/#managing-virtual-environments-with-virtualenvwrapper
