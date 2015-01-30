'''
Created on Jan 27, 2015

@author: wangshiyuan
'''
import sys
from ZipCodeReader import ZipCodeReader
from TaxRequestHandler import TaxRequestHandler

class TaxRateCollector(object):
 

    def __init__(self, apiKey=None, inputDir=None, outDir=None):
        self.apiKey = apiKey
        self.inputDir = inputDir
        self.outDir = outDir

    def collectTaxRate(self):
        stateZipMap = ZipCodeReader().extractZipStateMap(self.inputDir)
        TaxRequestHandler(stateZipMap, self.apiKey, self.outDir).getTaxInfo()
        
if __name__ == '__main__':
    taxRateCollector = TaxRateCollector(sys.argv[1], sys.argv[2], sys.argv[3] ) 
    taxRateCollector.collectTaxRate()
       