# -*- coding: utf-8 -*-
"""
@author: Rikard
"""

class Sequence:
  
    def __init__(self, bases):
        self.bases = bases

    def first_base(self):
        result = self.bases[0]
        return result

#Counting number of bases    
    def number_of_bases(self):
        return len(self.bases)

#Checking if sequence is DNA
    def is_dna(self):
        char = ["C", "G", "A", "T"]
        a = True    
        for s in self.bases:
            if s not in char:  #One single character wrong => not DNA
                a = False
        return a
    
    def compl(self):
        t = ""
        dic = { "A": "T" , "T": "A", "G": "C", "G": "C" }
        for s in self.bases:
            t += dic[s]  #Creating new string with opposite base
        return Sequence("t")
    
    def compr(self, seq):
        #Assume seq is sequence object  
        match = False
        assert len(self.bases) == len(seq.bases), "**Error: Genes must be same length!"
        for i in range(len(self.bases)):
            if self.bases[i] != seq.bases[i]:
                return i #Returning indices of non-matching bases
            else:
                match = True
        if match:
            return -1

    def sep(self):
        return self.__sep(self.bases, []) #Calling recursive held method
    
    def __sep(self, base, genes): #help method
        stop = "A"*10 + "T"*10
        stopindex = base.find(stop)
        if stopindex == -1:
            genes.append(base)
            return genes
        else:
            genes.append(base[:stopindex])
            return self.__sep(base[stopindex + len(stop):], genes)
        
    def swap(self, seq): #Swap method
        assert len(self.bases) == len(seq), "**Error: Genes must be same length!"
        count = 0
        for i in range(len(self.bases)):
            if self.bases[i] != seq[i]:
                count += 1 #Counting swap sequences
        return count
            
    
    def __str__(self):  #Optional trivial string method
        return self.bases
    
    
    
    
    
    
    
    
    
    