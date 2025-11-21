"""
PyQuotex - Unofficial Quotex API Client

Modified version of PyQuotex by Cleiton Leonel Creton
Original: https://github.com/cleitonleonel/pyquotex
License: GNU GPL v3

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

__version__ = "1.0.0"
__author__ = "Cleiton Leonel Creton (Original), Modified Version"
__license__ = "GPL-3.0"

import logging


def _prepare_logging():
    """Prepare logger for PyQuotex module"""
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())
    
    websocket_logger = logging.getLogger("websocket")
    websocket_logger.setLevel(logging.DEBUG)
    websocket_logger.addHandler(logging.NullHandler())


_prepare_logging()
