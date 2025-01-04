"""
Basic tools for all tokenizers
"""

from functools import lru_cache


@lru_cache(maxsize=1024)
def is_acsii(c) :
    byte_len = len(bytes(c, "UTF-8"))
    return byte_len == len(c)


@lru_cache(maxsize=65535)
def is_utf8(c) :
    byte_len = len(bytes(c, "UTF-8"))
    return byte_len == 3 * len(c)
