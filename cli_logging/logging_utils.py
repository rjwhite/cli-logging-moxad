import os
import sys
import logging
import argparse

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


def setup_cli_logging(debug: bool = False, progname: str | None = None):
    """
    Configure logging for CLI scripts with module names included.
    """
    if progname is None:
        progname = os.path.basename(sys.argv[0])
    if progname == "":
        progname = None

    level = logging.DEBUG if debug else logging.INFO
    handler = logging.StreamHandler(sys.stderr)
    use_color = handler.stream.isatty()

    # Include module name in log output
    if progname:
        fmt = f"{progname}: %(name)s: %(levelname)s: %(message)s"
    else:
        fmt = f"%(name)s: %(levelname)s: %(message)s"
    formatter = ColorFormatter(fmt, use_color=use_color)
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)

    if not root.handlers:
        root.addHandler(handler)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", 
                        help="Enable debug logging")
    args = parser.parse_args()

    setup_cli_logging(debug=args.debug)

    logger_root = logging.getLogger()
    logger_root.error("This is an error")

    logger_main = logging.getLogger("main")
    logger_main.debug("Debug message from main")
    logger_main.info("Info message from main")

    logger_utils = logging.getLogger("utils")
    logger_utils.warning("Warning from utils module")
    logger_utils.error("Error from utils module")
    logger_utils.critical("Critical issue from utils")

    sys.exit(0)
