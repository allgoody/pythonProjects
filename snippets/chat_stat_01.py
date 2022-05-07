# 
import json

fname = input('Enter file name:')
if len(fname) < 1:
    fname = './test_data/chat06052022.json'
    
str_data = open(fname).read()
json_data = json.loads(str_data)

singleRow = json_data['stats'][0]['rows']
for entry in singleRow:
    trackCode = entry[0]
    rawHits = entry[1]
    uniqueHits = entry[2]
    freeReg = entry[3]
    refBroad = entry[4]
    totalSpent = entry[5]
    payout = entry[6]
    
    if freeReg > 0 or payout > 0:
        print(f'tracking code: {trackCode}| free registrations: {freeReg}| pay: {payout}')
        
totals = json_data['stats'][0]['totals']

print(f'Total registrations: {totals["Free Registrations"]}| Total spent: {totals["Total Money Spent"]}| Total payout: {totals["Payout"]} ')