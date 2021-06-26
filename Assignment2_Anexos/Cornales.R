BiocManager::install("pcaMethods")
if (!requireNamespace("BiocManager", quietly = TRUE))
        install.packages("BiocManager")

#Com isto, vamos instalar o package pcaMethods, que nos permite realizar analises de Componentes Principais.
#Este package faz parte de um conjunto de packages conhecido como BioConductor, pelo que ha uma condicao para instalar o manager, caso este nao esteja instalado ainda.



BiocManager::install("LEA")

library(pcaMethods)
library(LEA)

#O package LEA, usado para poder carregar ficheiros geno e instalado, e carregado junto do pcaMethods com a funcao library.

corn_data = read.geno("cornales.geno")

View(corn_data)
#O ficheiro geno e carregado.
#O ficheiro geno contem a matriz do genotipo, os individuos estao dispostos da esquerda para a direita, enquanto que as posicoes dos SNP estao dispostas de cima para baixo.

cores<-rep(c(4), times=c(90))
types<-rep(c("bland","pungent"),times=c(88,2))
print(types)
#Estes vetores sao usados na funcao legend.

corn_data1 = replace(corn_data,corn_data==9, NA)
View(corn_data1)
corn_data2 = corn_data1[rowSums(is.na(corn_data1))!=ncol(corn_data1), ]

cores[86]=2
cores[85]=2
print(cores)

corn_pca=pcaMethods::pca(corn_data2, scale="none", center=T, nPcs = 2, method="nipals")
slplot(corn_pca,
       scol=cores,
       scoresLoadings=c(TRUE, FALSE),
       sl=NULL,  
       spch="x")


legend("bottomright",
       legend=(unique(types)),
       col=unique(cores),
       pch="x",
       title="Plant Types")


#A funcao slplot permite uma visualizacao rapida das scores e dos loadings das PCAs, no entanto, os loadings nao sao mostrados, apenas as scores.
#A funcao legend serve unicamente para identificar os individuos presentes no score plot.

#No Score plot, e formada uma elipse, sendo que cada diametro corresponde a variabilidade do "score" de cada PCA, os pontos dispostos ao longo do diametro grande (PCA 1) variam bastante, 
#enquanto que os que estao dispostos ao longo do diametro pequeno (PCA 2), tem variabilidade reduzida.
#os pontos fora da elipse sao outliers, a sua variabilidade nao e explicada pelas PCAs.

#Os individuos estao agrupados em dois grupos, bland e pungent, e como podemos observar, existe uma percentagem muito superior de individuos bland que de individuos pungent.




library(data.table)
print(corn_pca@R2)



