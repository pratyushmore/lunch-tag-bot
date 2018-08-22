# Lunch Tag Bot

Often, as organizations grow, it can be difficult to meet different kinds of people. Lunch Tag Bot aims to address that by randomly pairing interested individuals to have lunch together, and thus get to know each other.

This project has been set up to enable easy modification and integration into any workplace or organization. It will first support UI integration with slack only. In the future, though, this can be extended to many other organizational chat/communication systems.

## Using Lunch Tag Bot for your organization

### Pre-requisites

We expect you to have the following installed:

* Python 2.7
* Pip
* Virtualenv and Virtualenvwrapper

### Setting up the repository

1. Create a new virtual environment
```
mkvirtualenv <<virtual_env_name>>
```

2. Enter virtual environment
```
workon <<virtual_env_name>>
```

3. Create your builder
```
(echo "LTB_VIRTUAL_ENV_DIRECTORY=$WORKON_HOME/<<virtual_env_name>>"; cat build_common.txt) > build.sh
```

4. Install dependencies
```
pip install -r requirements.txt
```

### Integrating with your organization

All you need to do in order to use this project for your own organization is make the following changes to `settings.py`.

***(In Progress ...)***

## Building and Deploying on AWS Lambda

We designed this project to run on AWS Lambda. Here's how you can get it runningTo

1. Build your project
```
bash build.sh
```
You should see a file named `build.zip`.

2. ***In Progress ...***
