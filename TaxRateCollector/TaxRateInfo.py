'''
Created on Jan 27, 2015

@author: wangshiyuan
'''

class TaxRateInfo(object):
    def __init__(self, results):
        self.infoMap = results
#         self.geoPostalCode = results["geoPostalCode"]
#         self.geoCity = results["geoCity"]
#         self.geoCounty = results["geoCounty"]
#         self.geoState = results["geoState"]
#         self.taxSales = results["taxSales"]
#         self.taxUse = results["taxUse"]
#         self.stateSalesTax = results["stateSalesTax"]
#         self.stateUseTax = results["stateUseTax"]
#         self.citySalesTax = results["citySalesTax"]
#         self.cityUseTax = results["cityUseTax"]
#         self.cityTaxCode = results["cityTaxCode"]
#         self.countySalesTax = results["countySalesTax"]
#         self.countyUseTax = results["countyUseTax"]
#         self.countyTaxCode = results["countyTaxCode"]
#         self.districtSalesTax = results["districtSalesTax"]
#         self.districtUseTax = results["districtUseTax"]
    def toString(self):
        return str(self.results)
