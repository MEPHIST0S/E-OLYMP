#Solution - 1
text = input().strip()
count = 0

for i in range(len(text)):
    if text[i] in '.!?':
        if i == 0 or text[i - 1] not in '.!?':
            count += 1

print(count)

#Solution - 2
import re

text = input().strip()
sentence_endings = re.findall(r'[.!?]+', text)
total_sentences = len(sentence_endings)

print(total_sentences)