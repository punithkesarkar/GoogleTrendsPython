#!/usr/bin/env python3
"""
usage: in cmd run python google_trends_advanced.py [-h] (-kw KW [KW ...] | -f INFILE) [-fh FILE_HEADER] [-o OUTFILE]

Generate CSV files containing Google Trends data of given KEYWORD(s) provided via file or console

optional arguments:
  -h, --help            show this help message and exit
  -kw KW [KW ...], --keywords KW [KW ...]
                        Keyword whose trends to be found
  -f INFILE, --infile INFILE
                        Path to CSV file that contains keywords whose trends to be found
  -fh FILE_HEADER, --file_header FILE_HEADER
                        Column containing list of keywords in CSV file passed as input (default: Company)
  -o OUTFILE, --outfile OUTFILE
                        Output file name (default for files: `Google Trends Results.csv`; default for console: `KW[ & KW...] - Google Trends.csv`)
"""

import argparse
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
    parser = argparse.ArgumentParser(description='Generate CSV files containing Google Trends data of given KEYWORD(s) provided via file or console')
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-kw', '--keywords', metavar='KW', nargs="+", type=str, help="Keyword whose trends to be found")
    group.add_argument('-f', '--infile', type=str, help="Path to CSV file that contains keywords whose trends to be found")

    parser.add_argument('-fh', '--file_header', type=str, help="Column containing list of keywords in CSV file passed as input (default: Company)", default='Company')
    parser.add_argument('-o', '--outfile', type=str, help="Output file name (default for files: `Google Trends Results.csv`; default for console: `KW[ & KW...] - Google Trends.csv`)")
    
    args = parser.parse_args()

    try:
        if args.keywords and not args.outfile:
            args.outfile = ' & '.join(args.keywords) + " - Google Trends.csv"
        if args.infile:
            df = pd.read_csv(args.infile)
            COLUMN_TO_BE_USED = args.file_header
            if COLUMN_TO_BE_USED in df.columns and len(df[COLUMN_TO_BE_USED]) > 0:
                args.keywords = list(df[COLUMN_TO_BE_USED])
            else:
                raise Exception("`{col}` not present in input CSV file: {f}".format(col=COLUMN_TO_BE_USED, f=args.infile))

        print("Setting up Google instance...")
        pytrends = TrendReq(hl='en-US')
        res_file = get_google_trends_data(args.keywords, out_filename=args.outfile)
        if res_file:
            print("Successfully stored Google Trend results in `{rf}` for {kw}".format(kw=args.keywords, rf=res_file))
            
    except Exception as e:
        print("Something unexpected has occured. Please find the error below...")
        print("Error: ", e)

