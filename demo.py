"""
ClimateAI Data Challenge starter code 

read data from pickle file, summarize the contents, and create a dataframe 

'uke_eggedal_data_challenge.pkl' contains a dictionary with the following items:
    'obs_lon_lat' - location of flow data observations
    'flow' - time series of flow data
    'flow_dates' - dates of flow data
    'obs_tas' - 9 time series of temperature data
    'obs_pr' - 9 time series of precipitation data
    'obs_dates' - dates of temperature and precipitation observations
"""
import pickle

import pandas as pd 


def main():
    with open('uke_eggedal_data_challenge.pkl', 'rb') as f:
        data_dict = pickle.load(f)
    ## summarize data in pickle file
    for k, v in data_dict.items():
        print(k)
        print(type(v))
        try:
            print(v.shape)
        except AttributeError:
            print(len(v))
    ## create dataframe with flow data
    flow_df = pd.DataFrame(data=data_dict['flow'], index=data_dict['flow_dates'], 
                           columns=['flow'])
    ## column names
    n_locs = data_dict['obs_pr'].shape[1]
    tas_cols = ['tas_{:d}'.format(i) for i in range(n_locs)]
    pr_cols = ['pr_{:d}'.format(i) for i in range(n_locs)]
    ## create dataframes for temperature and precipitation data
    tas_df = pd.DataFrame(data=data_dict['obs_tas'], index=data_dict['obs_dates'], 
                          columns=tas_cols)
    pr_df = pd.DataFrame(data=data_dict['obs_pr'], index=data_dict['obs_dates'], 
                         columns=pr_cols)
    ## create one dataframe for all data
    df = pd.concat((tas_df, pr_df, flow_df), join='inner', axis=1)
    print(df.head())
    print(df.shape)


if __name__ == '__main__':
    main()