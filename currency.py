import pandas as pd
import tabulate

data = pd.read_csv('eurofxref.csv')
data.columns = data.columns.str.replace(' ', '')
data_hist = pd.read_csv('eurofxref-hist.csv')

out_df = pd.DataFrame()
out_df['CURRENCY'] = ['USD','SEK','GBP','JPY']
out_df['RATE'] = [data['USD'][0],data['SEK'][0],data['GBP'][0],data['JPY'][0]]
out_df['MEAN HISTORICAL RATE'] = [data_hist['USD'].mean(),data_hist['SEK'].mean(),data_hist['GBP'].mean(),data_hist['JPY'].mean()]

print(out_df)

with open('etl.md', 'w+') as etl:
    etl.write(out_df.to_markdown())



