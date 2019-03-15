from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import csv

tuits = csv.reader(open('./DJTUITS/tuits.csv'),delimiter=',')
archivo = open('./DJTUITS/syntax.csv', 'w')

next(tuits,None)
for row in tuits:
    print(row[0])
    texto = row[1]
    client = language.LanguageServiceClient()
    #text = u'Hello, world!'
    document = types.Document(
        content=texto,
        type=enums.Document.Type.PLAIN_TEXT)
    tokens = client.analyze_syntax(document).tokens
    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM','PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    pos_class=[] 
    dependency=[]
    for token in tokens:
        pos_class.append(u'{}: {}'.format(token, token.text.content))
        #dependency.append(token.dependencyEdge.headTokenIndex + token.text.content)
    #print(line)
    str1 = u''.join(pos_class).encode('utf-8').strip()
    #print((str1))
    archivo.write(str1)
    archivo.write('\n')
archivo.close()
