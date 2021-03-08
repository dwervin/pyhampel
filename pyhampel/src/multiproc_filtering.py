

import multiprocessing as mp
import pandas as pd

__all__ = ["hampel_mp"]


def hampel_mp(g_list: list, vals_col: str, time_col=None, win_size=30, num_dev=3, center_win=True):

    # The code for the Hampel filter needed to be added to a separate file for
    # this multiprocessing call to work.  HampelFilter.py needs to be in the local directory.
    from HampelFiltering import hampel_filter_df

    __name__ = '__main__'
    # print("__name__", __name__)

    global results
    results = []
    if __name__ == '__main__':
        # Step 1: Init multiprocessing.Pool()
        pool = mp.Pool(mp.cpu_count())
        print("After Pool Creations")

        # Step 2: Define callback function to collect the output in 'results' to take
        # advantage of asynchronous calls.
        def collect_result(result):
            #global results
            print("Running collect")
            results.append(result)

        # Step 3: Use loop to parallelize. This asynchronous call uses the collect_result
        # function defined earlier and adds results to results list.
        # This uses sliding window size of window_size and num_dev standard deviations for outlier detection.
        for row in g_list:
            pool.apply_async(hampel_filter_df, args=(row, vals_col, time_col, win_size,num_dev, center_win), callback=collect_result)

        # Step 4: Close Pool and let all the processes complete
        pool.close()
        pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

        return results
