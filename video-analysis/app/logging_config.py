import logging

def logging_config():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s-%(levelname)s-%(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        filename=r"logs.log"
                        )