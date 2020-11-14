import re
from typing import *
from typing import Pattern


def search_by_regex(pattern: Pattern[AnyStr], string: AnyStr) -> Optional[AnyStr]:
    """
    It searches for a pattern (without flags) inside a given string.
    """
    if (match := re.search(pattern, string)) :
        start, end = match.start(), match.end()
        return string[start:end]
    return None
