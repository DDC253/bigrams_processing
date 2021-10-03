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

mega_list = []
frasi = list_sentences(sentences)
for el in frasi:
    for el1 in el:
        word = el1.split(' ')
        mega_list.append(word)
        

#print(mega_list)        
    
lista_1 = []
for l in mega_list:
    for i in range(len(l)-1): 
           lista_1.append([[l[i]], [l[i+1]]])

#print(lista_1)

bigrams_list =[]
for el in lista_1:
   for i,j in zip(el[0],el[1]):
            bigrams_list.append([i+' '+j])



textfile = open("de_cv_dev_bi.txt", "w")
for element in bigrams_list:
    for bi in element:
        textfile.write(''.join(element) + "\n")
textfile.close()
