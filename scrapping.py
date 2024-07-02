
#scrapping

#scrapping a web page 
'''
from urllib.request import urlopen
from  bs4 import BeautifulSoup
url=urlopen("http://bit.ly/1D7wKcH").read()
soup=BeautifulSoup(url,"html.parser")
text=soup.p.contents
print(text)
'''

#scrapping a text from pdf

# import PyPDF2
# try:
#   with open(r"C:\Users\m\Downloads\lect1.pdf", 'rb') as pdf_file:
#     pdf = PyPDF2.PdfReader(pdf_file)
#     content = pdf.pages[0].extract_text()
#     print(content)
# except Exception as e:
#   print(f"Cannot open PDF file with error: {str(e)}")






#nltk uses
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,punkt
from nltk.stem import PorterStemmer


text="MICHael is gooing to zoo by bycecle and he is good but he is bad also if he does this"
text=text.lower()
print(text)
swords=set(stopwords.words("english"))
words=word_tokenize(text)
words=[word for word in words if word.lower() not in swords]
print(words)
text=" ".join(words)
print(text)
st = PorterStemmer()
words=word_tokenize(text)
words=[st.stem(word) for word in words ]
text=" ".join(words)
print(text)
words=word_tokenize(text)
text_bi=nltk.bigrams(text)
print(list(text_bi))
text_n=nltk.ngrams(text,5)
print(list(text_bi))
"""

"""
import re
#Python
p=re.compile('colou?r')#uisoptional
#re.search(pattern, sequence)
x=re.search(p,'colour').start() #returns 0
print(x) #prints color
x=re.search(r'Co.k.e','Cookie').group() #note the prefix r for raw
print(x)
p=re.compile('[aA]pple.')
x='Apples'
if re.search(p,x):
    print("match")
else:
    print("not match")    
"""
#scrap text file
"""
with open(r"D:\versionc.txt",'r') as file:
    file_contents=file.read()
print(file_contents)
"""

