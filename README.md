# write out messages with various levels:  INFO, ERROR, etc...

## Description
This module gives you a routine to write out a message of various
levels such as DEBUG, INFO, WARNING, ERROR and CRITICAL.

The messages are high-lighted with different colors if they are
going to a terminal.  If output has been redirected to a file,
then the colors are turned off.

Levels DEBUG and INFO go to stdout, while WARNING, ERROR and CRITICAL
go to stderr.

Messages for level DEBUG will only be printed if the 1st argument debug
is set to True.

The second argument (progname) is an optional program name to be printed
at the beginning of the message provided.

## Code example
    import os
    import sys
    import argparse
    import logging
    from cli_logging import setup_cli_logging

    # provide a --debug option
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", 
                        help="Enable debug logging")
    args = parser.parse_args()

    setup_cli_logging(debug=args.debug,
                      progname=os.path.basename(sys.argv[0]))

    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("This is a warning!")
    logging.error("This is an ERROR!")
    logging.critical("Critical issue!!!")
