from loguru import logger
import os
from pathlib import Path

directpath = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, os.path.pardir))
logger.add(str(directpath) + "\\" + "tests" + "\\" + "debug_tests.log", format="{time} {level} {message}", level="DEBUG")