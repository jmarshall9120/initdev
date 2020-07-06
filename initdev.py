import os
import json
import configparser

#config path
config_path = "./.bandzdev.ini"

#git repo
initial_repo = ""

#default settings
default_settings = {
    "env_name": "bandz_env"
}

config = configparser.ConfigParser()

#ensure config exits
if not os.path.exists(config_path):
    config["DEFAULT"] = default_settings
    with open(config_path, "w") as f:
        config.write(f)

config.read("./bandzdev.ini")
config.sections()
config["DEFAULT"]["env_name"]



def init():
    return

def _initGit():
    if not os.path.exists(".git"):
        rtn = os.system('git init')
    return

def _writeCommitHooks():
    return



if __name__ == "__main__":
    init()