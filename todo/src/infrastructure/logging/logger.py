import sys
import logging
import logging.handlers


class Logger:

    @staticmethod
    def make_logger(logLevel):
        log_record_factory = logging.getLogRecordFactory()

        colours = {
            logging.DEBUG: "\033[1;32m",
            logging.INFO: "\033[1;36m",
            logging.WARNING: "\033[1;33m",
            logging.ERROR: "\033[1;31m",
            logging.CRITICAL: "\033[1;41m",
        }

        def decorate_record_factory(*args, **kwargs):
            record = log_record_factory(*args, **kwargs)
            record.levelname_c = "{}{}{}".format(
                colours[record.levelno],
                record.levelname,
                "\033[0m"
            )
            record.name = "{}{}{}".format(
                colours[record.levelno],
                record.name,
                "\033[0m"
            )

            record.msg = "{}{}{}".format(
                colours[record.levelno], record.msg, "\033[0m"
            )

            return record

        logging.setLogRecordFactory(decorate_record_factory)
        logging.getLogger().setLevel((logLevel + 1) * 10)

        terminal_handler = Logger.make_terminal_handler(logging)
        logging.getLogger().addHandler(terminal_handler)

        disk_handler = Logger.make_disk_handler(logging)
        logging.getLogger().addHandler(disk_handler)

        return logging

    @staticmethod
    def make_terminal_handler(logging):
        terminal = logging.StreamHandler(sys.stdout)
        formater = logging.Formatter(
            "[%(asctime)s]--------------------------------\n%(levelname_c)s:%(name)s\n%(message)s\n"
        )
        terminal.setFormatter(formater)

        return terminal

    @staticmethod
    def make_disk_handler(logging):
        disk = logging.handlers.RotatingFileHandler(
            filename = './storage/logs/rotating.log',
            maxBytes = 100000,
            backupCount = 1
        )
        disk.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[ %(asctime)s | %(name)s | %(filename)s | %(funcName)s | %(levelname)s ] %(message)s'
        )

        disk.setFormatter(formatter)

        return disk
