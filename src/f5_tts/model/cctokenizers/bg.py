"""
Tokenizer for Bulgarian
"""

from .base import is_acsii, is_utf8, BaseTokenizer


class Tokenizer(BaseTokenizer) :
    PUNCTUATIONS = ('!', '?', ':', ',', '.', '"', "'", '(', ')', '/', '%')

    CHAR_MAPPING = str.maketrans({
        '-': ' ',
        '—': ' ',
        ';': ",",
        '…': '.',
        "‘": "'",
        "’": "'",
        '“': '"',
        '„': '"',
        '«': '"',
        '»': '"',
        '(': '(',
        ')': ')',
        '/': ' ',
        '%': '%',
    })

    def convert_chars(self, text: str) :
        super().convert_chars(text)
        chars = []
        for c in self.split_chars() :
            if is_acsii(c) and c not in self.PUNCTUATIONS :
                chars.append(' ')
            if is_utf8(c) and chars and chars[-1] not in " :'\"" :
                chars.append(' ')
            chars.append(c)
        return chars
