from ibapi.contract import Contract
from synchronous_functions import *
import numpy as np
import pandas as pd
us_stock = pd.read_csv("nasdaq_screener.csv")
us_stock.dropna(subset = ["Sector"],inplace=True)
us_stock = us_stock[['Symbol','Name','Sector','Industry']]
stock_symbol = list(us_stock['Symbol'])
tech_stock = us_stock[us_stock['Sector']=='Technology']
tech_stock = list(tech_stock['Symbol'])

noData = pd.read_csv('noDataRecord.csv')
noData_list = list(noData.iloc[:,1])

contract = Contract()
contract.symbol = 'AAPL'
contract.secType  = 'STK'
contract.exchange = 'SMART'
contract.currency = 'USD'

noDataRecord = []

historical_data = fetch_historical_data(contract=contract,
                                        endDateTime='',
                                        durationStr='2 Y',
                                        barSizeSetting='1 min',
                                        whatToShow='MIDPOINT',
                                        useRTH=True)
extracted_data = pd.DataFrame()
extracted_data['date'] = historical_data['date']
extracted_data = extracted_data.set_index('date')
for i, st in enumerate(tech_stock):
    try:
        if st in noData_list:
            continue
        contract.symbol = st
        historical_data = fetch_historical_data(contract=contract,
                                                endDateTime='',
                                                durationStr='2 Y',
                                                barSizeSetting='1 min',
                                                whatToShow='MIDPOINT',
                                                useRTH=True)

        dataToMerge = historical_data[['date','close']]

        dataToMerge = dataToMerge.rename(columns={'close':st})
        #extracted_data = pd.merge(extracted_data, dataToMerge)
        extracted_data = extracted_data.join(dataToMerge.set_index('date'))

        print(extracted_data.head())
        extracted_data.to_csv("stock_data_mintick.csv")
        print(f"--------------------------Complete {i} / {len(tech_stock)} stocks extraction!--------------------------")
    except:
        noDataRecord.append(st)

noDataRecord = pd.DataFrame(noDataRecord)
noDataRecord.to_csv('noDataRecord2.csv')


print(extracted_data)