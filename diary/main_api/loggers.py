import os
import logging
import platform

if platform.system() == "Linux":
    PATH_TO_SAVE = '{}/logs/'.format(
        os.path.dirname(__file__))

# elif platform.system() == "Windows":
#     PATH_TO_SAVE = '{}\\logs\\.log'.format(
#         os.path.dirname(__file__))

formatter = logging.Formatter("%(asctime)s: %(name)s | %(message)s")

creations_logger = logging.getLogger('CreatesLoger')
creations_logger.setLevel(logging.INFO)
creations_file_handler = logging.FileHandler(f'{PATH_TO_SAVE}CREATED.log')
creations_file_handler.setFormatter(formatter)
creations_logger.addHandler(creations_file_handler)


updates_logger = logging.getLogger('UpdatesLoger')
updates_logger.setLevel(logging.INFO)
updates_file_handler = logging.FileHandler(f'{PATH_TO_SAVE}UPDATED.log')
updates_file_handler.setFormatter(formatter)
updates_logger.addHandler(updates_file_handler)


deletions_logger = logging.getLogger('DeletesLoger')
deletions_logger.setLevel(logging.INFO)
deletions_file_handler = logging.FileHandler(f'{PATH_TO_SAVE}DELETED.log')
deletions_file_handler.setFormatter(formatter)
deletions_logger.addHandler(deletions_file_handler)
