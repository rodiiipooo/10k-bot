# Ensure that API_KEY is defined somewhere in your code
API_KEY = ''
from sec_api import ExtractorApi
from IPython.display import display, HTML
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

extractorApi = ExtractorApi(API_KEY)

def pront(text, line_length=100):
  words = text.split(' ')
  lines = []
  current_line = ''
  for word in words:
    if len(current_line + ' ' + word) <= line_length:
      current_line += ' ' + word
    else:
      lines.append(current_line.strip())
      current_line = word
  if current_line:
    lines.append(current_line.strip())
  print('\n'.join(lines))

def ten_k_review(filing_10_k_url):
    required_sections = ['8']

    for section in required_sections:
        try:
            if section == '6':
                try:
                    item_6_html = extractorApi.get_section(filing_10_k_url, section, 'html')
                    print('Extracted Item 6 (HTML)')
                    print('-----------------------')
                    # read HTML table from a string and convert to dataframe
                    tables = pd.read_html(item_6_html)
                    # first table includes the financial statements
                    df = tables[0]
                    # drop all columns with NaN values except if the first cell is not NaN
                    mask = (df.iloc[1:, :].isna()).all(axis=0)
                    financial_statements = df.drop(df.columns[mask], axis=1).fillna('')
                    print('Consolidated financial statements as dataframe:')
                    print(financial_statements[financial_statements.columns[:4]])
                    print('-----------------------')
                except Exception as e:
                    print(f"Error processing section {section}: {e}")
            elif section == '8':
                try:
                    # Extract HTML section for Financial Statements and Supplementary Data
                    item_8_html = extractorApi.get_section(filing_10_k_url, section, 'html')
                    # Read HTML tables from the string and convert to DataFrames
                    tables = pd.read_html(item_8_html)
                    revenue_table = tables[2]
                    balance_table = tables[16]
                    extracted_tables = [revenue_table, balance_table]

                    for table in extracted_tables:
                        print(f'Extracted Table from Item 8')
                        print('-----------------------')
                        mask = (table.iloc[1:, :].isna()).all(axis=0)
                        table.drop(table.columns[mask], axis=1).fillna('')
                        df = table
                        # Assuming you want to display or process the balance sheet table here
                        print(df[df.columns[:4]])
                        print('-----------------------')
                except Exception as e:
                    print(f"Error processing Item 8: {e}")
            else:
                # extract HTML section "Item 1 - Business" from 10-K
                item_1_html = extractorApi.get_section(filing_10_k_url, section, 'text')

                print('Extracted Item 1 (txt)')
                print('-----------------------')
                pront(item_1_html[0:3000])
                print('-----------------------')
        return item_1_html
        except Exception as e:
            print(f"Error processing section {section}: {e}")

def issue_check(text, search_type)
  lower(text)
  problem_phrases = ["going concern"]
  
links_list = []
for link in links_list:
  # Replace with actual URL of the 10-K filing
  issue_check(ten_k_review(link))
  
  # check for issues
  

  

