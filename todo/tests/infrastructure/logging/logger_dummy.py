class LoggerDummy:

    def getLogger(self, name):
        return self

    def debug(self, message):
        pass
