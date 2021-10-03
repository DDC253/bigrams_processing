from typing import Text
import pandas as pd
import os

#stabilisce il path locale in cui sit rova il file
os.chdir(os.path.dirname(os.path.abspath(__file__)))


##DOPO SCRIPT ROBERTO e prima ahah
def sentences(file_text):
    # load dataframe and ignoring initial spaces
    df_ID_sent =  pd.read_csv(file_text, sep='|', header=None , engine='python', index_col=False)
    # Split only on first space
    aux0 = df_ID_sent[0].str.split(' ',1, expand = True)
    # Store back to df
    df_ID_sent[0] = aux0[0]   
    df_ID_sent[1] = aux0[1] 
    
    # Rename columns
    df_ID_sent = df_ID_sent.rename(columns={0:'ID', 1:'sentence'})
    #select "sentence" column
    sentences = df_ID_sent['sentence']
    return sentences

#print(sentences("de_cv_dev.txt"))
rows = sentences('de_cv_dev.txt')

def list_sentences(sentences):
    list = [[row] for row in rows]
    return list

frasi = list_sentences(sentences)

#for l in frasi:
  #  lista = list(row)

#print(lista)


#print(list_sentences(sentences))
lista_1 = []
for l in frasi:
    for i in range(len(frasi)-1): 
            lista_1.append([[i[i]], [i[i+1]]])

print(lista_1[1:3])