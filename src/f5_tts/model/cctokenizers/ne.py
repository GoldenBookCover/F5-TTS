"""
Tokenizer for Nepali
"""

from .base import is_acsii, is_utf8, BaseTokenizer


class Tokenizer(BaseTokenizer) :
    DEPENDENT_VOWELS = ('ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ')
    DIACRITICS = ('̐', '̥', '़', 'ँ', 'ं', 'ः', '्')
    PUNCTUATIONS = ('。', '，', '、', '；', '：', '？', '！', '《', '》', '【', '】', '—', '…')
    CHAR_MAPPING = str.maketrans(
        {";": ",", "“": '"', "”": '"', "‘": "'", "’": "'"}
    )

    def convert_chars(self, text: str) :
        super().convert_chars(text)
        chars = []
        for c in self.split_chars() :
            if is_acsii(c) and c not in self.PUNCTUATIONS :
                chars.append(' ')
            if is_utf8(c) :
                if c in (self.DEPENDENT_VOWELS | self.DIACRITICS) :
                    c = chars.pop() + c
                elif chars and len(bytes(c, 'utf-8')) > 1 and chars[-1] not in " :'\"" :
                    chars.append(' ')
            chars.append(c)
        return chars
