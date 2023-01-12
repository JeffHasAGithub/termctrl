ANSI_ESC = "\033"


def escape(s: str) -> str:
    """Given a str, prepend an ANSI escape character to it"""
    return ANSI_ESC + s
