
import pandas as pd


def gen_list_of_frames(df_ts: pd.DataFrame, grp_keys: list):
    """
    This function takes a single dataframe of time-series data and groups them based
    upon a key value for each distinct time series.

    For example, if you have time series for 10 company's stocks, you can separate these 10 company's stock
    time-series into a list of dataframes, where each dataframe is an individual time-series for each stock.

    Parameters
    ----------
    df_ts: pd.DataFrame
        Dataframe containing many different time series that can be grouped by some key.
    grp_keys: list
        A list of one or mor keys on which to uniquely extract a time series.  For example,
        if we were processing time series of many stock tickers, the stock ticker
        could be the key.

    Returns
    -------
        grp_list: list
            A list of dataframes with each dataframe containing a uniquely identified time series.
    """

    grp_list = []
    df_groups = df_ts.groupby(grp_keys)

    for name, df in df_groups:
        grp_list.append(df)

    return grp_list
