class LoggerDummy:

    def getLogger(self, name):
        return self

    def debug(self, message):
        pass

    def info(self, message):
        pass

    def warning(self, message):
        pass

    def error(self, message):
        pass

    def critical(self, message):
        pass
