from enum import Enum

__all__ = ["LINEMoji"]

CODEPAIR_POINTER = "\udbc0"
CODEPAIR_BUFFER = "\udbff\udfff"
PLACEHOLDER_STRING = "placeholder"

class LINEMoji(Enum):
    """
    https://developers.line.biz/en/docs/messaging-api/emoji-list/
    Use product_id to lookup how the emojis looks like
    """
    STARTER_PACK = ("\udbc0\udd03", 350, "5ac1bfd5040ab15980c9b435")
    PASTEL = ("\udbc9\ude04", 149, "5ac21a13031a6752fb806d57")
    BLACK_N_WHITE = ("\udbc2\udf01", 150, "5ac21ef5031a6752fb806d5e")
    WORDS = ("\udbc2\udc01", 170, "5ac21cc5031a6752fb806d5c")
    HAND_N_GESTURES = ("\udbc2\ude01", 222, "5ac21e6c040ab15980c9b444")
    BLACK_WHITE_OUTLINE = ("\udbca\udd01", 149, "5ac21b4f031a6752fb806d59")
    PEOPLE = ("\udbc1\udf02", 221, "5ac21c46040ab15980c9b442")
    RELATIONSHIPS = ("\udbc3\udf02", 252, "5ac2206d031a6752fb806d5f")
    EVERYDAY_STUFF = ("\udbc1\udc02", 248, "5ac21542031a6752fb806d55")
    FESTIVE_AND_BIRTHDAY = ("\udbc5\udf01", 157, "5ac223c6040ab15980c9b44a")

    @property
    def range(self):
        return self.value[0]
    
    @property
    def length(self):
        return self.value[1]
    
    @property
    def product_id(self):
        return self.value[2]
    
    @classmethod
    def get_all_ranges(cls):
        return [e.name for e in cls]
    
    def get_emoji(self, emojiNo: int = 1):
        if emojiNo > self.length:
            raise IndexError("Index out of range for the selected emoji range")
        __unicode = self.range + CODEPAIR_POINTER + chr(0xdd00 + emojiNo) + PLACEHOLDER_STRING + CODEPAIR_BUFFER
        return __unicode.encode('utf-16', 'surrogatepass').decode('utf-16').encode('utf-8').decode()
    
    def get_all_emojis(self, splits: int = 0):
        __emojis = []
        for emojiNo in range(1, self.length + 1):
            __unicode = self.range + CODEPAIR_POINTER + chr(0xdd00 + emojiNo) + PLACEHOLDER_STRING + CODEPAIR_BUFFER
            __emojis.append(__unicode.encode('utf-16', 'surrogatepass').decode('utf-16').encode('utf-8').decode())
        if splits > 0:
            __emojis = [__emojis[i:i + splits] for i in range(0, len(__emojis), splits)]
        return __emojis
        