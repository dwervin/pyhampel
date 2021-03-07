

import multiprocessing as mp
from pyhampel.src.filtering import hampel_filter_df

__all__ = ["hampel_mp"]

# hampel_filter_df(df: pd.DataFrame, vals_col: str, time_col=None, win_size=30, num_dev=3, center_win=True)
# global results
# results = []


def hampel_mp(g_list: list, vals_col: str, time_col=None, win_size=30, num_dev=3, center_win=True):
    # Define window size. Note: Data point being considered is centered so this means that points to the left an right
    # are considered in the median calculation.
    # window_size = 60

    # Define the number of standard deviations about median to use.
    # num_dev = 5

    # The code for the Hampel filter needed to be added to a separate file for
    # this multiprocessing call to work.  HampelFilter.py needs to be in the local directory.
    #import HampelFilter

    # import multiprocessing as mp

    # global results
    results = []
    # if __name__ == '__main__':
    # Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # Step 2: Define callback function to collect the output in 'results' to take
    # advantage of asynchronous calls.
    def collect_result(result):
        # global results
        results.append(result)

    # hampel_filter_df(df: pd.DataFrame, vals_col: str, time_col=None, win_size=30, num_dev=3, center_win=True)

    # Step 3: Use loop to parallelize. This asynchronous call uses the collect_result
    # function defined earlier and adds results to results list.
    # This uses sliding window size of window_size and num_dev standard deviations for outlier detection.
    for row in g_list:
        #pool.apply_async(hampel, args=(row, 7, 3), callback=collect_result)
        #pool.apply_async(hampel, args=(row, window_size, num_dev, True), callback=collect_result)
        pool.apply_async(hampel_filter_df, args=(row, vals_col, time_col, win_size,
                                                 num_dev, center_win), callback=collect_result)

    # Step 4: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

    return results
