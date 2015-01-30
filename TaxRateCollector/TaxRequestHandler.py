'''
Created on Jan 27, 2015

@author: wangshiyuan
'''
import urllib2
import json
import os
class TaxRequestHandler(object):

    def __init__(self, zipStateMap, apiKey, outDir):
        self.zipStateMap = zipStateMap
        self.apiKey = apiKey
        self.outDir = outDir
        
    def formURLRequest(self, zip, state):
        urlheader = 'http://api.zip-tax.com/request/v20?'
        apiKeySegment = 'key=' + self.apiKey+'&'
        zipCodeSegment = 'postalcode='+zip+'&'
        stateSegment = 'state='+state+'&'
        formatSegment = 'format==JSON'
        return urlheader + apiKeySegment +zipCodeSegment+stateSegment+formatSegment
    
    def getTaxInfo(self):
        if not os.path.exists(self.outDir):
            os.makedirs(self.outDir)
        taxInfolst = []
        id = 0
        limit = 5000
        fileName = "TaxRateInfo"
        for zip in self.zipStateMap:
            state = self.zipStateMap[zip]
            url = self.formURLRequest(zip, state)
            print "requesting tax Info for "+zip+", "+state
            response = urllib2.urlopen(url).read()
            responseloaded =  json.loads(response)
            if(responseloaded["rCode"]!=100):
                continue
            else:
                taxInfolst.append(str(responseloaded["results"][0]))
            if len(taxInfolst) == limit:
                self.writeToFile(taxInfolst, self.outDir,fileName+str(id))
                taxInfolst = []
                id += 1
        self.writeToFile(taxInfolst, self.outDir, fileName+str(id))
    
    def writeToFile(self, taxInfolst, outDir, fileName):
        filePath = outDir+"/"+fileName
        print "Writing Tax information to "+filePath
        target = open(filePath, 'w')
        for i in xrange(0, len(taxInfolst)):
            target.write(taxInfolst[i])
            target.write("\n")
        target.close()
