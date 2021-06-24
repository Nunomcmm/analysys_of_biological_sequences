import sys #importa-se a biblioteca sys
import Bio #importa-se a biblioteca Biopython
from Bio import Entrez #importa-se o pacote Entrez da biblioteca Biopython

#Fornecer um email à NCBI
Entrez.email = ""
#Atribui-se à variável handle a função esearch, onde insere-se o primeiro argumento da consola como a base de dados a pesquisar, o segundo argumento como a espécie, o máximo de resultados e o histórico, respetivamente.
handle = Entrez.esearch(db=sys.argv[1], term=sys.argv[2], retmax=sys.argv[3] , usehistory="y")
#Atribui-se à variável result a função read que vai ler a variável handle
result = Entrez.read(handle)
#Atribui-se à variável identifiers a IdList do result
identifiers = result['IdList']
#Atribui-se à variável webenv a lista de WebEnv do result
webenv = result['WebEnv']
#Atribui-se à variável query_key a lista das QueryKey do result
query_key = result['QueryKey']
#Atribui-se à variável handle a função efetch que vai buscar toda a informação de cada identificador, o rettype reescreve em formato fasta e o retmode em ficheiro txt.
handle = Entrez.efetch(db=sys.argv[1], id= identifiers,retmax=sys.argv[3],rettype="fasta", retmode="text", webenv = webenv, query_key = query_key)
#Atribui-se à variável record o ficheiro em formato FASTA
record = handle.read()
#Imprimir a variável record na consola
print(record)
