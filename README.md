# LINEMoji
Reverse engineered LINE's legacy unicode emoji


## Usage
```python
from line_emoji import LINEMoji

print(LINEMoji.get_all_ranges()) # Get all available emoji ranges
print(LINEMoji.PASTEL.get_emoji(1)) #Get an emoji from specific range
print(LINEMoji.PASTEL.get_all_emojis()) #Get all emojis from specific range
```

## Why?
to use with LINE's Official API Chatbots, for those who finds using unicode emoji suits their hands better.


..or paste it into the chat for funsies, whatever man.

## References
[Official Documentations](https://developers.line.biz/en/docs/messaging-api/emoji-list)
