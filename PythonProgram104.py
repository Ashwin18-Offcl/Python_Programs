#Remove special symbols /puncuations from a string
#expected-->"John is developer musician"

sentence = "/Jon is @developer & musician"

import re
clean_sentence=re.sub('[^A-Za-z0-9\s]+',"",sentence)
print(clean_sentence)

