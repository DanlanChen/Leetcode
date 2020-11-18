import datetime
#pinterest

def bad_phrase(bad_phrases, s):
    s = set(s.lower().split(' '))
    bad_phrases = set([s.lower() for s in bad_phrases])
    # bad_phrase_dic = dict.fromkeys(bad_phrases,0)
    # print(type(bad_phrase_dic))
    # for c in s:
    #     if not bad_phrase_dic.get(c,None):
    #         return True
    if len(s & bad_phrases) > 0:
      return True
    return False
t1 = datetime.datetime.now()
bad_phrases = {'porn', 'world war II', 'world war'}
s = 'I like porn hah hahaa hahh'
print(bad_phrase(bad_phrases, s))
t2 = datetime.datetime.now()
print(t2-t1)
