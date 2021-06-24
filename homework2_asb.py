import sys, re, traceback, os
import django
from django.db import models
from django.core.validators import FileExtensionValidator

def ler_fasta():
    """
    Recebe um ficheiro fasta como argumento 1, depois verifica as linhas que começam com ">"
    e converte os cabeçalhos para o tipo utilizado em nexus.

    Primeiro, verifica se existe como argumento um ficheiro fasta, se não existe envia para um ficheiro de erros.
    Abre-se o ficheiro e cria-se um dicionário. Verifica-se em todas as linhas do ficheiro as
    que se iniciam com ">" que vão ser os cabeçalhos e as restantes linhas as sequências, restringe-se
    o nome da sequência a 99 caracteres.

    Args:
        f (ficheiro): Recebe o ficheiro

    Returns:
        seqdict: dicionário

    Raises:
        Exception: Envia para um ficheiro de erros.

    """

    try:
        sys.argv[1]
    except IndexError:
        print('É necessário escolher um ficheiro.', file = sys.stderr)
        error = open('erros.txt', 'w')
        traceback.print_exc(file=error)
        return 0


    f = open(sys.argv[1], 'r')
    seq_dict = {}


    for line in f:
        line = line.strip()
        try:
            if line.startswith('>'):

                if len(line)==1:
                    continue
                header = line.replace('>', '')
                header = header.replace(' ','_')
                header = header[:99]
                seq_dict[header] = ''

            else:
                seq_dict[header] += line
        except Exception:
            error = open('erros.txt', 'w')
            traceback.print_exc(file=error)
            continue



    return seq_dict

def print_nex():
    """
    Imprime no ficheiro nexus as informações necessárias.

    Verifica-se se existe os argumentos 2 e 3, outgroup e replicações respetivamente,
    caso não existam imprime uma mensagem para o utilizador e é enviado um erro para
    o ficheiro de erros. Também deverá contar o número de sequências que existem no Ficheiro
    e o seu tamanho.

    Args:
        outgroup (string): Nome do outgroup utilizado
        ngen (int): Número de replicações pretendidas
    Returns:
        STDOUT: Visualização do ficheiro nexus na shell.

    Raises:
        Exception: Envia para um ficheiro de erros.

    """

    try:
        sys.argv[2]
    except IndexError:
        print('É necessário escolher um outgroup e um número de replicações.', file = sys.stderr)
        error = open('erros.txt', 'w')
        traceback.print_exc(file=error)
        return 0
    outgroup=sys.argv[2]

    try:
        sys.argv[3]
    except IndexError:
        print('É necessário escolher o número de replicações.', file = sys.stderr)
        error = open('erros.txt', 'w')
        traceback.print_exc(file=error)
        return 0
    ngen=sys.argv[3]
    seqs=ler_fasta()
    count = 0
    length = 0 #used for length of the alignment
    num_seqs = len(seqs) #number of sequences in file
    if len(seqs)==0:
        print('Ficheiro vazio.', file=sys.stderr)
        return 0
    while count <= 1:
        for i in seqs:
            length = len(seqs[i])
            count += 1


    #Prints initial nexus block
    print('#NEXUS')
    print('begin data;')
    print(' dimensions ntax={} nchar={};'.format(num_seqs, length))
    print(' format datatype=DNA missing=N gap=-;')
    print('matrix')


    #End of nexus file
    for seq in sorted(seqs):
        print("\t{} {}".format(seq, seqs[seq]))
    print(';')
    print('end;\n')
    print('begin mrbayes;')
    print('\tset autoclose=yes;')
    print('\toutgroup {};'.format(outgroup))
    print('\tmcmcp ngen={} printfreq=1000 samplefreq=100 diagnfreq=1000 nchains=4 savebrlens=yes filename=MyRun01;'.format(ngen))
    print('\tmcmc;')
    print('\tsumt filename=MyRun01;')
    print('end;')

#main
seqs={}
print_nex()
