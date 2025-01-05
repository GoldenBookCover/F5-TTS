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


class BaseTokenizer :
    PUNCTUATIONS = ('。', '，', '、', '；', '：', '？', '！', '《', '》', '【', '】', '—', '…')

    # Normalize text by converting special characters to common ones.
    CHAR_MAPPING = str.maketrans(
        {";": ",", "“": '"', "”": '"', "‘": "'", "’": "'"}
    )

    def convert_chars(self, text) :
        self.set_text(text)
        self.translate_chars()

    def set_text(self, text: str) :
        self.text = text

    def translate_chars(self) :
        # TODO: Normalize punctuations
        # TODO: Remove uncommon punctuations and characters
        # TODO: Handle mistakes and unrecognizable characters
        self.text = self.text.translate(self.CHAR_MAPPING)

    def split_chars(self, text) :
        return text
