import logging
from logging.config import dictConfig
dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
    'BASE_FORMAT': {
        'format': '[%(name)s][%(levelname)-6s] %(message)s',
        },

    'FILE_FORMAT': {
        'format': '[%(asctime)s] [%(name)s][%(levelname)-6s] %(message)s',
        },

    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'BASE_FORMAT',
            'stream': 'ext://sys.stdout'
            },
        'debug_console_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'FILE_FORMAT',
            'stream': 'ext://sys.stdout'
            }
    },
    'root': {
    'level': 'INFO',
    'handlers': ['console','debug_console_handler']
        }
    })

# logger = logging.getLogger()
# logger.info('Hi')
logging.info('Hi')