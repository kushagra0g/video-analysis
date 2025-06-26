import logging

def logging_config(path_to_logging_directory):
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s-%(levelname)s-%(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        filename=path_to_logging_directory
                        )