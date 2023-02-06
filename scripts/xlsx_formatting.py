import pandas as pd

# set path and file name
path_save = ''
file_name = ''

# pip install xlsxwriter
writer = pd.ExcelWriter(path_save+'/'+file_name+'.xlsx',engine='xlsxwriter')
workbook = writer.book

for i in range(1,3):
    # update parts
    sheet_name = f'sheet{i}'
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    contents_gap = 4 # the number of rows between dfs

    # set the sheet
    worksheet=workbook.add_worksheet(sheet_name)
    writer.sheets[sheet_name] = worksheet

    # contents
    worksheet.write_string(0,0,'dataframe 1') # title of 1st df
    df1.to_excel(writer,sheet_name = sheet_name, startrow=1, startcol=0) # 1st df

    worksheet.write_string(df1.shape[0]+contents_gap,0,'dataframe 2') # title of 2nd df
    df2.to_excel(writer,sheet_name = sheet_name, startrow=df2.shape[0]+contents_gap+1, startcol=0) # 2nd df

workbook.close() # you have to run this script to open the xlsx file.