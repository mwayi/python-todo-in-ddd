# Todo

## About

A simple todo application written in python that is more about design patterns than anything else.

The is to allow a user to:-
- add todo items
- mark todo items as done 
- see items done/not done
- remove todo items

## Install

pre-requisites
- sudo apt-get install python3
- sudo apt-get install python3-pip
- sudo pip3 install virtualenv 

1. Clone repository and enter its directory
```
git clone {repo}
cd {repo-name}
```

2. Create and activate environment
```
virtualenv -p python3 env
. env/bin/activate
```

3. Install requirements
```
pip3 install -r requirements.txt
```

## Configure

## Use

- [x] add --t="Do x"
- [ ] remove --id=[1,2,3]
- [x] view --filter="status = done and date between 00/00/00,00/00/00"
- [x] complete --id=[1,2,3]

### Logging

By default the log level is set to a minimum of INFO. You can change this when running use cases by using the flag `--log-level=1`. The log level options are enums of integers between 0 and 4. This means:-

- DEBUG = 0
- INFO = 1 (default)
- WARNING = 2
- ERROR = 3
- CRITICAL = 4

*The debug level lets you know what queries were executed*

Rotating log files will be persisted to `./storage/logs` at a DEBUG level.

## Contribute

### Running tests
```
coverage run -m unittest2 discover -p="*Test.py"
coverage html
```

or use

```
bash bin/run-tests
```

```
bash bin/run-tests *Test.py
```