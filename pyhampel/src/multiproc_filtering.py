"""
This module contains filtering function that leverage multiprocessor capability
"""

import multiprocessing as mp
import pandas as pd

__all__ = ["hampel_mp", "hampel_with_dev_mp"]


def hampel_mp(g_list: list, vals_col: str, time_col=None, win_size=30, num_dev=3, center_win=True):
    """

    Parameters
    ----------
    g_list: list(pd.DataFrame)
        list of time series dataframes usually generated from gen_list_of_frames() function, but can also be
        individually compiled list of time series dataframes as long as columns are consistently named in each one.
    vals_col: str
        Name of column containing the original values to be processed.
    time_col: str
        Name of column containing datetime for time series.  This is optional if dataframe index consists of
        DatetimeIndex.  If time_col contains string representation of date, it will be converted to datetime64.
    win_size: int
        Value of width (time periods) of sliding window.  If time periods are in days, this is the width in number
        of days.  If time periods are in hours, this is the width in hours.
    num_dev: int
        Number of standard deviations used in calculating threshold used to determine an outlier.
    center_win: boolean
        Boolean to indicate if point considered is at center of window or leading edge of window.  If False,
        calculations are similar to moving median with point to be considered on right side of window and points in
        past used for MAD calculation.

    Returns
    -------
    Function returns a list of dataframes,  with each dataframe consisting of original values columns along with
    the Hampel filtered data, outlier values and boolean flags where outliers found.

    """

    # The code for the Hampel filter needed to be added to a separate file for
    # this multiprocessing call to work.  HampelFilter.py needs to be in the local directory.
    from HampelFiltering import hampel_filter_df

    __name__ = '__main__'

    global results
    results = []
    if __name__ == '__main__':
        # Step 1: Init multiprocessing.Pool()
        pool = mp.Pool(mp.cpu_count())

        # Step 2: Define callback function to collect the output in 'results' to take
        # advantage of asynchronous calls.
        def collect_result(result):
            # global results
            results.append(result)

        # Step 3: Use loop to parallelize. This asynchronous call uses the collect_result
        # function defined earlier and adds results to results list.
        # This uses sliding window size of window_size and num_dev standard deviations for outlier detection.
        for row in g_list:
            pool.apply_async(hampel_filter_df,
                             args=(row, vals_col, time_col, win_size,num_dev, center_win),
                             callback=collect_result)

        # Step 4: Close Pool and let all the processes complete
        pool.close()
        pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

        return results


def hampel_with_dev_mp(g_list: list, vals_col: str, time_col=None, win_size=30, num_dev=3, center_win=True):
    """

    Parameters
    ----------
    g_list: list(pd.DataFrame)
        list of time series dataframes usually generated from gen_list_of_frames() function, but can also be
        individually compiled list of time series dataframes as long as columns are consistently named in each one.
    vals_col: str
        Name of column containing the original values to be processed.
    time_col: str
        Name of column containing datetime for time series.  This is optional if dataframe index consists of
        DatetimeIndex.  If time_col contains string representation of date, it will be converted to datetime64.
    win_size: int
        Value of width (time periods) of sliding window.  If time periods are in days, this is the width in number
        of days.  If time periods are in hours, this is the width in hours.
    num_dev: int
        Number of standard deviations used in calculating threshold used to determine an outlier.
    center_win: boolean
        Boolean to indicate if point considered is at center of window or leading edge of window.  If False,
        calculations are similar to moving median with point to be considered on right side of window and points in
        past used for MAD calculation.

    Returns
    -------
    Function returns a list of dataframes,  with each dataframe consisting of original values columns along with
    the Hampel filtered data, outlier values and boolean flags where outliers found.

    """

    # The code for the Hampel filter needed to be added to a separate file for
    # this multiprocessing call to work.  HampelFilter.py needs to be in the local directory.
    from HampelFiltering import hampel_filter_with_dev_df

    __name__ = '__main__'

    global results
    results = []
    if __name__ == '__main__':
        # Step 1: Init multiprocessing.Pool()
        pool = mp.Pool(mp.cpu_count())

        # Step 2: Define callback function to collect the output in 'results' to take
        # advantage of asynchronous calls.
        def collect_result(result):
            # global results
            results.append(result)

        # Step 3: Use loop to parallelize. This asynchronous call uses the collect_result
        # function defined earlier and adds results to results list.
        # This uses sliding window size of window_size and num_dev standard deviations for outlier detection.
        for row in g_list:
            pool.apply_async(hampel_filter_with_dev_df,
                             args=(row, vals_col, time_col, win_size,num_dev, center_win),
                             callback=collect_result)

        # Step 4: Close Pool and let all the processes complete
        pool.close()
        pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

        return results
