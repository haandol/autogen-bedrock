import logging

logger = logging.getLogger("autogen")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
