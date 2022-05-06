import googletrans
from googletrans import Translator
 
d = googletrans.LANGUAGES
 
text1 = "Hello welcome to my website!"
 
translator = Translator()
 
print(translator.detect(text1))

for i in d:
    trans1 = translator.translate(text1, src='ko', dest=i)
    print(f"{d.get(i)} 의 인사말 : ", trans1.text)
