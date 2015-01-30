'''
Created on Jan 27, 2015

@author: wangshiyuan
'''
import csv


#f = open(sys.argv[1],'rb')]
class ZipCodeReader:
    def _init_(self):
        pass
         
    def extractZipStateMap(self, dir):
        zipStateMap = {}
        f = open(dir,'rb')
        try:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "zip":
                    continue
                zipStateMap[row[0]]= row[5]
        finally:
            f.close()
        return zipStateMap
if __name__ == '__main__':
    pass