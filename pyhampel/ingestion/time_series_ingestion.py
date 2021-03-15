import pandas as pd

__all__ = ["ingest_list_of_files"]


def ingest_list_of_files(data_files: list, conv: dict, header: int = 0) -> pd.DataFrame:
    """
    This function reads data contained in the list of files and returns a single dataframe
    containing all the data.

    Parameters
    ----------
    data_files: list
        list of data files to read.  These files should all have the same headers and number of columns
    conv: dict
        dictionary containing column names and data types for columns.  This will override default
        data types inferred by pandas when reading data.
            e.g.:
            conv = {'MEASR_ID': str}
    header: int
        Integer designation for row number containing headers in data file.

    Returns
    -------
    df: pd.DataFrame
        Pandas dataframe containing data from all files.
    """

    li = []
    cols = []

    for filename in data_files:
        frame = pd.read_csv(filename, index_col=None, header=header, converters=conv)
        if len(cols) == 0:
            cols = list(frame.columns)
        elif set(cols) != set(list(frame.columns)):
            raise Exception("Can't read files. Column names in files do not match.")
        li.append(frame)

    df = pd.concat(li, axis=0, ignore_index=True)

    return df
