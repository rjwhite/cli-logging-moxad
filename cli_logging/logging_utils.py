import os
import sys
import logging
import argparse

_VERSION = '0.3.0'

# ANSI color codes
COLORS = {
    "DEBUG": "\033[36m",    # Cyan
    "INFO": "\033[32m",     # Green
    "WARNING": "\033[33m",  # Yellow
    "ERROR": "\033[31m",    # Red
    "CRITICAL": "\033[41m", # Red background
    "RESET": "\033[0m",
}


class ColorFormatter(logging.Formatter):
    def __init__(self, fmt=None, use_color=True):
        super().__init__(fmt)
        self.use_color = use_color

    def format(self, record):
        if self.use_color:
            color = COLORS.get(record.levelname, COLORS["RESET"])
            record.levelname = f"{color}{record.levelname}{COLORS['RESET']}"
        return super().format(record)


class MaxLevelFilter(logging.Filter):
    """Only allow records with levelno <= max_level."""
    def __init__(self, max_level):
        super().__init__()
        self.max_level = max_level

    def filter(self, record):
        return record.levelno <= self.max_level


def setup_cli_logging(debug: bool = False, progname: str | None = None,
                      use_color: bool = True ):
    """Configure CLI logging with split streams, colors
    Setup logging:
        - DEBUG/INFO -> stdout
        - WARNING/ERROR/CRITICAL -> stderr
        - Colors are only applied if the stream is a terminal
    Arguments:
        1) debug=False
            If debug is True, then logging.debug() is enabled
        2) progname=None
            If progname is given, the message is prepended with it
        3) use_color=True
            By default, use colors in the message level (ERROR, etc)
    Returns:
        None
    """

    level = logging.DEBUG if debug else logging.INFO
    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()

    fmt = f"%(levelname)s: %(message)s"
    if progname and progname != "":
        fmt = f"{progname}: {fmt}"

    # stdout handler for DEBUG/INFO
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(MaxLevelFilter(logging.INFO))
    color_flag = sys.stdout.isatty() if use_color == True else False
    stdout_handler.setFormatter(ColorFormatter(fmt, color_flag))

    # stderr handler for WARNING+
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.WARNING)
    color_flag = sys.stderr.isatty() if use_color == True else False
    stderr_handler.setFormatter(ColorFormatter(fmt, color_flag))

    root.addHandler(stdout_handler)
    root.addHandler(stderr_handler)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", 
                        help="Enable debug logging")
    parser.add_argument("--nocolor", action="store_false", 
                        help="Enable debug logging")
    args = parser.parse_args()

    setup_cli_logging(debug=args.debug,
                      progname=os.path.basename(sys.argv[0]),
                      use_color=args.nocolor,
    )

    logging.debug("Debug message")
    logging.info("Info message")
    logging.warning("This is a warning!")
    logging.error("This is an ERROR!")
    logging.critical("Critical issue!!!")

    sys.exit(0)
