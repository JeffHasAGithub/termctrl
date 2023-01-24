class TermError(Exception):
    """Base Package Error"""


class AttrError(TermError):
    """Attrribute Error"""


class CursorError(TermError):
    """Cursor Error"""
