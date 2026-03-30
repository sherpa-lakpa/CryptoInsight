import logging
import os
from datetime import datetime

def get_logger(name="pipeline", log_dir="/Volumes/workspace/cryptoinsight/logs/"):
    logger = logging.getLogger(name)

    if not logger.handlers:
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(
            log_dir,
            f"{name}_{datetime.now().strftime('%Y-%m-%d')}.log"
        )

        file_handler = logging.FileHandler(log_file)
        file_format = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(file_format)


        print_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        print_handler.setFormatter(formatter)


        # ------------------------
        # Add Handlers
        # ------------------------
        logger.addHandler(print_handler)
        logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)
    return logger