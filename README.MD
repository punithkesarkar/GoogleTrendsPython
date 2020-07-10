## Instructions for running:

    1.  After opening command prompt in this directory, type the following command to 
        install dependencies.
        
        pip install -r requirements.txt

    After successful completion of the previous command, you can run the Python 
    script `google_trends_scraper.py`.

    2. You can get usage instructions on how to run this script by the following 
    command.

        python google_trends_advanced.py --help

        (OR)
        
        python google_trends_advanced.py -h

    3. Get Google Trends data for keywords present in file `sample_keywords_list.csv` which is in same drectory
    with column name containing keywords as `Company` with output file set as `tech_companies.csv` by the 
    following command.

    python google_trends_advanced.py -o tech_companies.csv -f sample_keywords_list.csv

    4. Check if `tech_companies.csv` with required data is generated.

    5. Enjoy using this program! :D




## Examples

    (i) To get the Google Trends data for keywords present in a CSV file, 
    for example, `sample_keywords_list.csv` present in SAME directory, use the 
    following command to generate a default csv file named `Google Trends Results.csv`.

            python google_trends_advanced.py -f sample_keywords_list.csv
            (OR)
            python google_trends_advanced.py --infile sample_keywords_list.csv
    
    ------------------------------------------------------------------------------
    (ii)  To get the Google Trends data for keywords present in a CSV file, 
    for example, `sample_keywords_list.csv` present in SAME directory, and save it 
    in a custom file named, for example, `custom_results.csv`, 
    use the following command to generate it.

            python google_trends_advanced.py -o custom_results.csv -f sample_keywords_list.csv
            (OR)
            python google_trends_advanced.py --outfile custom_results.csv -f sample_keywords_list.csv
    ------------------------------------------------------------------------------
    (iii)  To get the Google Trends data for keywords present in a CSV file, 
    for example, `sample_keywords_list.csv` present in SOME OTHER directory, and save it 
    in a custom file named, for example, `custom_results.csv`, 
    use the following command to generate it.

            python google_trends_advanced.py -o custom_results.csv -f /path/to/sample_keywords_list.csv
            (OR)
            python google_trends_advanced.py --outfile custom_results.csv -f /path/to/sample_keywords_list.csv
    ------------------------------------------------------------------------------
    (iv)  To get the Google Trends data for keywords present in a CSV file, 
    for example, `sample_keywords_list.csv` present in SAME directory, but the column 
    under which keywords are stored is different from `Company` but instead is, for example,
     `SOME_OTHER_COLUMN`,  and save it in a custom file named, for example, `custom_results.csv`,
    use the following command to generate it.

            python google_trends_advanced.py -o custom_results.csv -f sample_keywords_list.csv -fh SOME_OTHER_COLUMN
    ------------------------------------------------------------------------------
    (v) To get the Google Trends data for the keyword `Apple`, use the
        following command to generate a csv file named 
        `Apple - Google Trends.csv` that contains its Google Trends data.

            python google_trends_advanced.py -kw Apple
            (OR)
            python google_trends_advanced.py --keywords Apple
    
    ------------------------------------------------------------------------------
    
    (vi) To get the Google Trends data for the keyword `Maple Syrup`,
         use the following command to generate a csv file named 
         `Maple Syrup - Google Trends.csv` that contains its Google Trends data.

            python google_trends_advanced.py -kw "Maple Syrup"

    ------------------------------------------------------------------------------

    (vii) To get the Google Trends data for the keywords (`Apple Watch', 
          'Amazon Web Services', 'Microsoft Office', 'Google'), use the 
          following command to generate a csv file named 
          `Apple Watch & Amazon Web Services & Microsoft Office & Google - Google Trends.csv`
          that contains its Google Trends data.
        
            python google_trends_advanced.py -kw "Apple Watch" "Amazon Web Services" "Microsoft Office" Google

    ------------------------------------------------------------------------------
    
    (viii) To give a custom filename such as `tech_companies` for the output CSV
         file, use the `--outfile` or `-o` argument to generate 
         `tech_companies.csv` containing required Google Trends data.

            python google_trends_advanced.py -o tech_companies -kw Apple Amazon Microsoft Google
            (OR)
            python google_trends_advanced.py --outfile tech_companies -kw Apple Amazon Microsoft Google



-----------------------------------------------------------------------------------------------------
