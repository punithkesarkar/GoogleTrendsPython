#!/usr/bin/env python3
"""


Generate CSV files containing Google Trends data of given KEYWORD(s) provided via file or console

"""

INFILE = r"PATH_TO_YOUR_KEYWORDS_FILE" ## The r"" syntax is to escape characters in order to remove errors
OUTFILE = r"PATH_TO_YOUR_OUTPUT_FILE"
COLUMN_NAME = "NAME_OF_COLUMN_WHERE_KEYWORDS_ARE_WRITTEN" ## It's "Company" in the `sample_keywords_list.csv` file

# Sample Data
# INFILE = r"C:\Users\user\Documents\sample_keywords_list.csv"
# OUTFILE = r"C:\Users\user\Documents\awesome_results.csv"
# COLUMN_NAME = "Company"

import pandas as pd
from pytrends.request import TrendReq

def get_google_trends_data(KEYWORDS, out_filename=None):

pytrends.build_payload(KEYWORDS, cat=0, geo='US',timeframe='all' ,gprop='')

df = pytrends.interest_over_time()

if not df.columns.any():
raise Exception("Keyword `{kw}` not present in Google Trends".format(kw=KEYWORDS[0]))
if 'isPartial' in df.columns:
df = df.drop(columns=['isPartial'])

ofname = out_filename
if ofname:
if not ofname.endswith('.csv'):
ofname = ofname + '.csv'
df.to_csv(ofname)
else:
ofname = "Google Trends Results.csv"
df.to_csv(ofname)
return ofname


if __name__ == "__main__":

df = pd.read_csv(INFILE)
COLUMN_TO_BE_USED = COLUMN_NAME
keywords = None
if COLUMN_TO_BE_USED in df.columns and len(df[COLUMN_TO_BE_USED]) > 0:
keywords = list(df[COLUMN_TO_BE_USED])
else:
raise Exception("`{col}` not present in input CSV file: {f}".format(col=COLUMN_TO_BE_USED, f=INFILE))
try:
print("Setting up Google instance...")
pytrends = TrendReq(hl='en-US')
res_file = get_google_trends_data(keywords, out_filename=OUTFILE)
if res_file:
print("Successfully stored Google Trend results in `{rf}` for {kw}".format(kw=keywords, rf=res_file))

except Exception as e:
print("Something unexpected has occured. Please find the error below...")
print("Error: ", e)
