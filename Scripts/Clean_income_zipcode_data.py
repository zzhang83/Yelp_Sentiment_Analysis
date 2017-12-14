import csv
import numpy
import pandas as pd

#############################In/out############################
def open_file(csvfile):
    reader = pd.read_csv(csvfile)
    return reader

def output_file(df,string):
    df.to_csv(string, index = False)

#############################Clean Data############################






#############################helper function#############################
def clean_zipcode(df):
    # select information according to each state
    az = df[df['state'] == 'AZ']
    pa = df[df['state'] == 'PA']
    nv = df[df['state'] == 'NV']
    nc = df[df['state'] == 'NC']
    il = df[df['state'] == 'IL']
    oh = df[df['state'] == 'OH']
    #concatenate together
    states_df = pd.concat([az, pa, nv, nc, oh, il])
    #select useful columns only
    states_df = states_df.iloc[:, [0, 4,5]]
    #lower case all letters
    states_df['state'] = states_df['state'].str.lower()
    states_df['county'] = states_df['county'].str.lower()
    #create a column that combine state and county name
    states_df['combine'] = states_df['county'] + states_df['state']
    return states_df

def clean_income(df):
    #Select useful columns
    df = df.iloc[:,[2,5]]
    #make two empty list
    state_list = ['s']*(df.shape[0])
    county_list = ['s']*(df.shape[0])
    #fill in two lists with county info and state info
    for i, row in df.iterrows():
        l = row[0].split(", ")
        county_list[i] = l[0]
        state_list[i] = l[1]

    # fill in dataframe columns with lists created aboove
    df['county'] = county_list
    df['county'] = df['county'].str.lower()
    df['state'] = state_list
    df['state'] = df['state'].str.lower()
    # Select info according to states
    AZ = df[df['state'] == 'arizona']
    PA = df[df['state'] == 'pennsylvania']
    NV = df[df['state'] == 'nevada']
    NC = df[df['state'] == 'north carolina']
    OH = df[df['state'] =='ohio']
    IL = df[df['state'] == 'illinois']
    income_dataframe = pd.concat([AZ, PA, NV, NC, OH, IL])
    #Replace state names
    replace = {'arizona': 'az', 'pennsylvania': 'pa', 'nevada': 'nv', 'north carolina': 'nc',
              'ohio': 'oh', 'illinois': 'il'}
    income_dataframe.replace(replace, inplace = True)

    # Delete 'county' from county column
    c_list = []
    for i, row in income_dataframe.iterrows():
        c_list.append(row[2].split(" county")[0])
    income_dataframe['county'] = c_list
    # Combination column
    income_dataframe['combine'] = income_dataframe['county'] + income_dataframe['state']
    #Rename column
    income_dataframe.rename(columns={'HC02_EST_VC02':'income'}, inplace=True)
    #select useful info
    income_df= income_dataframe.iloc[:,[2,1,3,4]]
    return income_df


def clean_income_zip(df1, df2):
    income_zip = pd.merge(df1, df2, on = 'combine', how = 'left')
    #print(income_zip.head())

    income_states = income_zip.dropna()
    income_states = income_states.iloc[:,[0, 1,2,3,5]]
    return income_states



##############################main######################################
def main():
    #open states and income raw data
    states = open_file("data/zip_codes_states.csv")
    df = open_file('data/income.csv')
    #clean states and income data
    states_df = clean_zipcode(states)
    income_df = clean_income(df)
    #print(income_df)
    #export cleaned income data
    output_file(income_df,'data/income_data.csv' )
    # combine states and income data
    income_states = clean_income_zip(states_df,income_df)
    print(income_states.shape)
    output_file(income_states,'data/income_zipcode.csv')




if __name__=="__main__":
    main()
