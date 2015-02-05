'''
Created on Feb 4, 2015

@author: wangshiyuan
'''
from ZipCodeReader import ZipCodeReader
import sys
from sets import Set
def readFromFileToList(inputDir):
    taxSimpleInfolst = []
    with open(inputDir,'r') as input:
        for line in input:
            array = line.split(",")
            taxSimpleInfolst.append(array[2].split(':')[1].strip('u\'')+", "+array[5].split(':')[1].strip('u\'')+",  "+array[7].split(':')[1].strip('u\''))
    return taxSimpleInfolst
    
def writeFromListToFile(taxSimpleInfolst, outputDir):
    with open(outputDir,'w') as output:
        for line in taxSimpleInfolst:
            output.write(line)
            output.write("\n")
def findMissing(zipStateMap, taxSimpleInfolst):
    taxSimpleInfoSet = Set()
    with open("output/missing",'w') as w:
        for simpleInfo in taxSimpleInfolst:
            zipCode = str(simpleInfo.split(',')[1].strip(' u\'')) 
            taxSimpleInfoSet.add(zipCode) 
            
        for zipCode in zipStateMap:
            if zipCode not in taxSimpleInfoSet:
                w.write(zipCode)
                w.write("\n")
        
    
if __name__ == '__main__':
    #writeFromListToFile(readFromFileToList("input/TaxRateInfo"),"output/TaxRateSimpleInfo")
    stateZipMap = ZipCodeReader().extractZipStateMap("input/zip_code_database.csv")
    taxSimpleInfolst = readFromFileToList("input/TaxRateInfo")
    findMissing(stateZipMap , taxSimpleInfolst)
    