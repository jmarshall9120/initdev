import os
import json
import argparse
import configparser

#config path
config_path = "./.bandzdev.ini"

#git repo
initial_repo = "https://github.com/jmarshall9120/initdev.git"

#venv_name
venv_name = "bandz_env"

#default settings
default_settings = {
    "env_name": "bandz_env",
    "remote_repo": "initial_repo"
}

config = configparser.ConfigParser()

#ensure config exits
if not os.path.exists(config_path):
    config["DEFAULT"] = default_settings
    with open(config_path, "w") as f:
        config.write(f)

config.read("./bandzdev.ini")
# config.sections()
# config["DEFAULT"]["env_name"]



def init():
    _initEnv()
    _initGit()
    return

def _initGit():
    if not os.path.exists(".git"):
        rtn = os.system('git init')
        rtn = os.system('python -m pip install --upgrade pip')
    if not os.path.exists(".gitignore"):
        with open(".gitignore\n", "w") as f:
            f.write(config["DEFAULT"]["env_name"] + "/")
    rtn = os.system('git add .')
    return

def _initEnv():
    if not os.path.exists(env:=config.get("DEFAULT","env_name")):
        rtn = os.system(f'python -m venv "{env}"')
    rtn = os.system('python -m pip install --upgrade pip')
    
    return


prePushHook= f"""
#!/bin/sh
echo "Working Test 2!!!" > 1
{get_sys_env_path()} freeze > requirements.txt
git add requirements.txt
git commit --reuse-message=HEAD
""".lstrip('\n')
prePushHook

# $env = python -c "import initdev; print(initdev.config.get('DEFAULT','env_name'));"
# ./bandz_env/Scripts/pip.exe freeze
# pip freeze > requirements.txt

def _writePrePushHook():
    if not os.path.exists(".git/hooks/pre-push"):
        with open(".git/hooks/pre-push", "w") as f:
            f.write(prePushHook)
    return
_writePrePushHook()

def get_sys_env_path():
    path = f"./{config.get('DEFAULT','env_name')}/Scripts/pip.exe"
    return os.path.normpath(path)
get_sys_env_path()

def _doPrePush():
    
    return



if __name__ == "__main__":
    init()