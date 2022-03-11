from ibapi.contract import Contract
from synchronous_functions import *
import numpy as np
import pandas as pd

contract = Contract()
contract.symbol = 'ALGM'
contract.secType  = 'STK'
contract.exchange = 'SMART'
contract.currency = 'USD'

historical_data = fetch_historical_data(contract=contract,
                                        endDateTime='',
                                        durationStr='1 D',
                                        barSizeSetting='1 hour',
                                        whatToShow='MIDPOINT',
                                        useRTH=True)

print(historical_data)