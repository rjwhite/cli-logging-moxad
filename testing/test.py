import os
import sys
import argparse
import logging
from cli_logging import setup_cli_logging

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true", 
                    help="Enable debug logging")
args = parser.parse_args()

setup_cli_logging(debug=args.debug, progname=os.path.basename(sys.argv[0]))

logging.debug("Debug message")
logging.info("Info message")
logging.warning("This is a warning!")
logging.error("This is an ERROR!")
logging.critical("Critical issue!!!")

sys.exit(0)
