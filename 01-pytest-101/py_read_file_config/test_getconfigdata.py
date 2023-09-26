from utils.myconfigparser import getGmailUrl
from utils.ConfigFileParser import ConfigFileParser

# config = ConfigFileParser()   # default config file
config = ConfigFileParser("prod.ini")


def test_getgmailurl():
    print(getGmailUrl())


def test_getoutlookurl():
    print(config.getOutlookUrl())
