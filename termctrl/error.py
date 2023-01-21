class TermError(Exception):
    """Base Package Error"""

    def __init__(self, msg: str):
        self.msg = f"{__package__} error: {msg}"
