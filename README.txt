write out messages with various levels:  INFO, ERROR, etc...

Description
===========
This module gives you a routine to write out a message of various
levels such as DEBUG, INFO, WARNING, ERROR and CRITICAL.

The messages are high-lighted with different colors if they are
going to a terminal.  If output has been redirected to a file,
then the colors are turned off.  You can also spefic to not use
colors at all.

Levels DEBUG and INFO go to stdout, while WARNING, ERROR and CRITICAL
go to stderr.

Messages for level DEBUG will only be printed if the 1st optional argument
debug is set to True.

The second argument (progname) is an optional program name to be printed
at the beginning of the message provided.

The thrid argument (use_color) is an optional program name to control
whether to use color on the message level or not.  default is True.

Code example
============
    import os
    import sys
    import argparse
    import logging
    from cli_logging import setup_cli_logging

    # check for options --debug and --nocolor
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", 
                        help="Enable debug logging")
    parser.add_argument("--nocolor", action="store_false", 
                        help="Enable debug logging")
    args = parser.parse_args()

    setup_cli_logging(debug=args.debug,
                      progname=os.path.basename( sys.argv[0]),
                      use_color=args.nocolor,
    )

    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("This is a warning!")
    logging.error("This is an ERROR!")
    logging.critical("Critical issue!!!")
