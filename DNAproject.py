# -*- coding: utf-8 -*-
"""
@author: Rikard
"""
import Sequence as seq
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Create an instance of the Sequence class.
example_sequence1 = seq.Sequence('AGCT')

# Call the first_base method on our instance. Notice that we don't specify the 'self' parameter when we call the method.
example_first_base = example_sequence1.first_base()
print(f'The first base is: {example_first_base}')

#Creating an example instance of sequence
example = seq.Sequence("ACGT")
print("First base of example: {}".format(example.first_base()))

#Defining a function
def readgenome(data):
    gene= open(data, 'r')
    return seq.Sequence(gene.readlines()[1])

#Reading first genome
DNA01 = readgenome("genome_01.dat")
print("Total number of bases in genome_01: {}".format(DNA01.number_of_bases())) 

#Separating
genes01 = DNA01.sep()
print("Lenght of first gene: {}".format(len(genes01[0])))

geneseq = [seq.Sequence(genes) for genes in genes01]
genelengths = [len(genes) for genes in genes01]

#Plotting a histogram
fig1, ax1 = plt.subplots()
fig1.set_size_inches(8, 5)
plt.hist(genelengths, bins = 50, color = "darkred", edgecolor = "black")
ax1.set(xlabel='Genelengths', ylabel='Number of genes', title='Histogram over genelengths')
ax1.grid()
fig1.savefig("Histogram")

#Reading the second genome
DNA02 = readgenome("genome_02.dat")
genes02 = DNA02.sep()

#Finding number of swap mutations
number_of_swaps = []
for i in range(len(geneseq)):
    number_of_swaps.append(geneseq[i].swap(genes02[i]))

#Scatter plot
#(Remember genes in genome01 and genome02 have same lenghts)
fig2, ax2 = plt.subplots()
fig2.set_size_inches(8, 5)
plt.scatter(genelengths, number_of_swaps)
ax2.set(xlabel='Genelengths', ylabel='Number of swaps', title='Swap mutations and genelengths')
ax2.grid()
fig2.savefig("Scatter")

#Task 10
#Linear regresseion using sklearn
#We ignore the very last point, which dosent really fit in with the rest
np_lenght = np.array(genelengths[:-1])
X = np_lenght.reshape(-1, 1)

reg = LinearRegression().fit(X, number_of_swaps[:-1])
Y = reg.predict(X)

fig3, ax3 = plt.subplots()
fig3.set_size_inches(8, 5)
plt.plot(X, Y)
plt.scatter(genelengths[:-1], number_of_swaps[:-1], color = "green")
ax3.set(xlabel='Genelengths', ylabel='Number of swaps', title='Linear Regresseions')
ax3.grid()
fig3.savefig("Regression")

#Printing the "score" of the regression
print("Score of regression {}".format(reg.score(X, number_of_swaps[:-1])))

#Task 11
#Visualising DNA using imgshow

#function that represents gene as numbers
def geneNumb(gene1, gene2=[]): 
    dic = {"A": 1, "C": 2, "G": 3, "T": 4}
    if gene2 == []:
        return [dic[g] for g in gene1 ]
    else:    #This case handles task 12
        assert len(gene1) == len(gene2), "**Error: Genes must be same length!"
        result = []
        for i in range(len(gene1)):
            if gene1[i]!=gene2[i]:   #Swap sequences
                result.append(7)     #The number 7 yields a pleasant color difference in the final plot 
            else:
                result.append(dic[gene1[i]])
        return result
                
geneArray = [geneNumb(g) for g in genes01]
#Function that returns numpy array of first 500 elements of each gene, with zeros 
#to compensate for short sequences 
def plotfunc(Array):
    result = []    
    for gene in Array:
        for i in range(max(genelengths) - len(gene)):
            gene.append(0)
        result.append(gene[:500])
    return np.array(result)

#Imshow plot
cmap =plt.cm.get_cmap("magma", 10)
fig4, ax4 = plt.subplots()
fig4.set_size_inches(8, 5)
plt.imshow(plotfunc(geneArray), cmap = cmap, aspect=5)
plt.colorbar(ticks=np.linspace(0,4,5), label = "A=1, C=2, G=3, T=4")
ax4.set(xlabel='Bases', ylabel='Genes', title='DNA visualisation (Without swaps)')
fig4.savefig("Imshow1")

#Task 12
#I did not figure out a clever way to do this using numpy
#We want to see swap mutation, thus calling geneNumb with two input arguments
geneArray2 = []
for i in range(len(genes01)):
    geneArray2.append(geneNumb(genes01[i], genes02[i]))
    
#Imshow plot with swaps
cmap =plt.cm.get_cmap("magma", 10)
fig5, ax5 = plt.subplots()
fig5.set_size_inches(8, 5)
plt.imshow(plotfunc(geneArray2), cmap = cmap, aspect=5)
plt.colorbar(ticks=np.linspace(0,7,8), label = "A=1, C=2, G=3, T=4, Swaps = 7")
ax5.set(xlabel='Bases', ylabel='Genes', title='DNA visualisation (With swaps)')   
fig5.savefig("Imshow2")
































