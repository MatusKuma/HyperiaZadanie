import logging

def setup_logging(log_file='logs/app.log'):
    """
    Sets up the logging configuration.
    
    Args:
        log_file (str): The path to the log file.
    
    Returns:
        None
    """
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    
    logger = logging.getLogger()
    logger.handlers = []
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
