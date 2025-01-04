"""
Tokenizer for Nepali
"""

from .base import is_acsii, is_utf8


class Tokenizer :
    DEPENDENT_VOWELS = {'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ'}
    DIACRITICS = {'̐', '̥', '़', 'ँ', 'ं', 'ः', '्'}
    PUNCTUATIONS = {'。', '，', '、', '；', '：', '？', '！', '《', '》', '【', '】', '—', '…'}

    def convert_chars(self, text) :
        chars = []
        for c in self.split_chars(text) :
            if is_acsii(c) and c not in self.PUNCTUATIONS :
                chars.append(' ')
            if is_utf8(c) :
                if c in (self.DEPENDENT_VOWELS | self.DIACRITICS) :
                    c = chars.pop() + c
                elif chars and len(bytes(c, 'utf-8')) > 1 and chars[-1] not in " :'\"" :
                    chars.append(' ')
            chars.append(c)
        return chars

    def split_chars(self, text) :
        return text
