import configparser
from pathlib import Path

cfgFile = "qa.ini"
cfgFileDirectory = "config"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)

config.read(CONFIG_FILE)


def getGmailUrl():
    return config["gmail"]["url"]


def getGmailUser():
    return config["gmail"]["user"]


def getGmailPass():
    return config["gmail"]["pass"]


print(getGmailUrl())


# print("\n\n")
# print(__file__)
# print(__name__)
# print(__package__)
# print(__doc__)
# print(__annotations__)
# print()
# # print(__dict__)
# print(__builtins__)
# print(__cached__)
# print(__loader__)
# # print(__path__)

# print("*" * 60)
# print(type(__file__))
# print(type(__name__))
# print(type(__package__))
# print(type(__doc__))
# print(type(__annotations__))
# print()
# # print(type(__dict__))
# print(type(__builtins__))
# print(type(__cached__))
# print(type(__loader__))
# print(__path__)
