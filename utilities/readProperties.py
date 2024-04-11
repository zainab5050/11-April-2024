import configparser

config = configparser.RawConfigParser()
config.read(".\\configuartions\\config.ini")


class Readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
