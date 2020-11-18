import re
PLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z .]')


def clean_text(text):

    text = text.lower() # lowercase text
    text = PLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    
    return text
    
# textDummy = "hello world 3423#$%@$ +__==324#$#2e34ertvfhnf2gr hello world"
# print( " in clean text file : " + clean_text(textDummy))

def extract_distance(text):
    RE_KM1 = re.compile(' [0-9][0-9].[0-9][0-9]km')
    RE_KM2 = re.compile(' [0-9].[0-9][0-9]km')
    RE_KM3 = re.compile(' [0-9][0-9].[0-9]km')
    RE_KM4 = re.compile(' [0-9][0-9][0-9]km')
    RE_KM5 = re.compile(' [0-9][0-9][0-9] km')
    RE_KM6 = re.compile(' [0-9][0-9].[0-9][0-9] km')
    RE_KM7 = re.compile(' [0-9] km')
    RE_KM8 = re.compile(' [0-9]km')
    RE_KM9 = re.compile(' [0-9][0-9] km')
    RE_KM10 = re.compile(' [0-9][0-9]km')

    dist = []
    dist += RE_KM1.findall(text) 
    dist += RE_KM2.findall(text) 
    dist += RE_KM3.findall(text) 
    dist += RE_KM4.findall(text) 
    dist += RE_KM5.findall(text) 
    dist += RE_KM6.findall(text) 
    dist += RE_KM7.findall(text) 
    dist += RE_KM8.findall(text) 
    dist += RE_KM9.findall(text) 
    dist += RE_KM10.findall(text) 
    return dist