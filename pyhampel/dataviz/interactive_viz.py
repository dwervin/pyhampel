import plotly.graph_objects as go
from ipywidgets import widgets
from ..src.filtering import hampel_filter_df, hampel_filter_with_dev_df

__all__ = ["hampel_interactive", "hampel_interactive_with_dev"]


def hampel_interactive(df_list: list, key_col, orig_col: str, filtered_col: str, outlier_col: str):
    """
    Function to create interactive plots from list of Hampel filter dataframes

    Parameters
    ----------
    df_list: list(pd.DataFrame)
        List of time series dataframes.  Generally the output from hampel_mp, but can also be individually
        compiled list of time series dataframes as long as columns are consistently names in each one.
    key_col: str
        This is the column name that uniquely identifies the time series parent.  For example, this could
        be a time series dataframe of stock prices so the column name might be "STOCK_TICKER".
    orig_col: str
        Column name for original values.
    filtered_col: str
        Name of column containing filtered values.
    outlier_col: str
        Name of column containing outlier values.

    Returns
    -------
    This returns an interactive plot of original values, filtered values, and outlier values constructed using
    IPyWidgets and plotly.
    """

    # Define widgets
    list_idx = widgets.IntSlider(value=1.0, min=1.0, max=len(df_list) - 1, step=1.0, description='List IDX:',
                                 continuous_update=False)
    recalc_outlier = widgets.Checkbox(description='Recalc Outlier?: ', value=False, )
    center_window = widgets.Checkbox(description='Center Window?: ', value=True, )
    window_size = widgets.IntSlider(value=30, min=2, max=120, step=1, description='Window Size:',
                                    continuous_update=False, )
    dev_size = widgets.IntSlider(value=3, min=1, max=12, step=1, description='Deviation Size:',
                                 continuous_update=False, )

    #
    container = widgets.HBox(children=[list_idx])
    container2 = widgets.HBox(children=[recalc_outlier, center_window])
    container3 = widgets.HBox(children=[window_size, dev_size])

    # # Assign an empty figure widget with traces
    trace1 = go.Scatter(x=df_list[0].index, y=df_list[0][orig_col], name='Original', line=dict(color='blue', width=2))
    trace2 = go.Scatter(x=df_list[0].index, y=df_list[0][filtered_col], name='Filtered',
                        marker=dict(size=7, color='green'), mode='markers')
    trace3 = go.Scatter(x=df_list[0].index, y=df_list[0][outlier_col], name='Outliers',
                        marker=dict(size=7, color='red'), mode='markers')

    # Define FigureWidget that will contain traces
    g = go.FigureWidget(data=[trace1, trace2, trace3],
                        layout=go.Layout(title=dict(text="Usage for " + str(df_list[0][key_col].unique()[0])), ))

    # Define Handler Function
    # noinspection PyTypeChecker,PyUnusedLocal
    def response(change):

        if recalc_outlier.value:
            # noinspection PyTypeChecker
            temp_df = df_list[list_idx.value][[key_col, orig_col]]
            new_df = hampel_filter_df(temp_df, vals_col=orig_col, time_col=None,
                                      win_size=window_size.value,
                                      num_dev=dev_size.value,
                                      center_win=center_window.value)
            with g.batch_update():
                pass
                g.data[0].x = new_df.index
                g.data[0].y = new_df[orig_col]
                g.data[1].x = new_df.index
                g.data[1].y = new_df[filtered_col]
                g.data[2].x = new_df.index
                g.data[2].y = new_df[outlier_col]
                g.layout.title = "Usage for " + str(df_list[list_idx.value][key_col].unique()[0])
                g.layout.xaxis.title = 'Date'
                g.layout.yaxis.title = 'Usage'

        else:
            with g.batch_update():
                g.data[0].x = df_list[list_idx.value].index
                g.data[0].y = df_list[list_idx.value][orig_col]
                g.data[1].x = df_list[list_idx.value].index
                g.data[1].y = df_list[list_idx.value][filtered_col]
                g.data[2].x = df_list[list_idx.value].index
                g.data[2].y = df_list[list_idx.value][outlier_col]
                g.layout.title = "Usage for " + str(df_list[list_idx.value][key_col].unique()[0])
                g.layout.xaxis.title = 'Date'
                g.layout.yaxis.title = 'Usage'

    # Register handler function with widgets
    list_idx.observe(response, names='value')
    recalc_outlier.observe(response, names="value")
    center_window.observe(response, names="value")
    window_size.observe(response, names="value")
    dev_size.observe(response, names="value")

    # return Interactive Plot
    return widgets.VBox([container, container2, container3, g])


def hampel_interactive_with_dev(df_list: list, key_col, orig_col: str, filtered_col: str, outlier_col: str,
                                lower_dev_col: str, upper_dev_col: str):
    """
    Function to create interactive plots from list of Hampel filter dataframes, also including
    lower and upper deviation values.

    Parameters
    ----------
    df_list: list(pd.DataFrame)
        List of time series dataframes.  Generally the output from hampel_mp, but can also be individually
        compiled list of time series dataframes as long as columns are consistently names in each one.
    key_col: str
        This is the column name that uniquely identifies the time series parent.  For example, this could
        be a time series dataframe of stock prices so the column name might be "STOCK_TICKER".
    orig_col: str
        Column name for original values.
    filtered_col: str
        Name of column containing filtered values.
    outlier_col: str
        Name of column containing outlier values.
    lower_dev_col: str
        Name of column containing lower deviation values.
    upper_dev_col: str
        Name of column containing upper deviation values.

    Returns
    -------
    This returns an interactive plot of original values, filtered values, and outlier values constructed using
    IPyWidgets and plotly.
    """

    # Define widgets
    list_idx = widgets.IntSlider(value=1.0, min=1.0, max=len(df_list) - 1, step=1.0, description='List IDX:',
                                 continuous_update=False)
    recalc_outlier = widgets.Checkbox(description='Recalc Outlier?: ', value=False, )
    center_window = widgets.Checkbox(description='Center Window?: ', value=True, )
    window_size = widgets.IntSlider(value=30, min=2, max=120, step=1, description='Window Size:',
                                    continuous_update=False, )
    dev_size = widgets.IntSlider(value=3, min=1, max=12, step=1, description='Deviation Size:',
                                 continuous_update=False, )

    #
    container = widgets.HBox(children=[list_idx])
    container2 = widgets.HBox(children=[recalc_outlier, center_window])
    container3 = widgets.HBox(children=[window_size, dev_size])

    # # Assign an empty figure widget with traces
    trace1 = go.Scatter(x=df_list[0].index, y=df_list[0][orig_col], name='Original', line=dict(color='blue', width=2))
    trace2 = go.Scatter(x=df_list[0].index, y=df_list[0][filtered_col], name='Filtered',
                        marker=dict(size=7, color='green'), mode='markers')
    trace3 = go.Scatter(x=df_list[0].index, y=df_list[0][outlier_col], name='Outliers',
                        marker=dict(size=7, color='red'), mode='markers')

    trace4 = go.Scatter(x=df_list[0].index, y=df_list[0][lower_dev_col], name='Lower Deviation',
                        line=dict(color='orange', width=2, dash='dot'))

    trace5 = go.Scatter(x=df_list[0].index, y=df_list[0][upper_dev_col], name='Upper Deviation',
                        line=dict(color='purple', width=2, dash='dot'))

    # Define FigureWidget that will contain traces
    g = go.FigureWidget(data=[trace1, trace2, trace3, trace4, trace5],
                        layout=go.Layout(title=dict(text="Usage for " + str(df_list[0][key_col].unique()[0])), ))

    # Define Handler Function
    # noinspection PyTypeChecker,PyUnusedLocal
    def response(change):

        if recalc_outlier.value:
            # noinspection PyTypeChecker
            temp_df = df_list[list_idx.value][[key_col, orig_col]]
            new_df = hampel_filter_with_dev_df(temp_df, vals_col=orig_col, time_col=None,
                                               win_size=window_size.value,
                                               num_dev=dev_size.value,
                                               center_win=center_window.value)
            with g.batch_update():
                pass
                g.data[0].x = new_df.index
                g.data[0].y = new_df[orig_col]
                g.data[1].x = new_df.index
                g.data[1].y = new_df[filtered_col]
                g.data[2].x = new_df.index
                g.data[2].y = new_df[outlier_col]
                g.data[3].x = new_df.index
                g.data[3].y = new_df[lower_dev_col]
                g.data[4].x = new_df.index
                g.data[4].y = new_df[upper_dev_col]
                g.layout.title = "Usage for " + str(df_list[list_idx.value][key_col].unique()[0])
                g.layout.xaxis.title = 'Date'
                g.layout.yaxis.title = 'Usage'

        else:
            with g.batch_update():
                g.data[0].x = df_list[list_idx.value].index
                g.data[0].y = df_list[list_idx.value][orig_col]
                g.data[1].x = df_list[list_idx.value].index
                g.data[1].y = df_list[list_idx.value][filtered_col]
                g.data[2].x = df_list[list_idx.value].index
                g.data[2].y = df_list[list_idx.value][outlier_col]

                g.data[3].x = df_list[list_idx.value].index
                g.data[3].y = df_list[list_idx.value][lower_dev_col]
                g.data[4].x = df_list[list_idx.value].index
                g.data[4].y = df_list[list_idx.value][upper_dev_col]

                g.layout.title = "Usage for " + str(df_list[list_idx.value][key_col].unique()[0])
                g.layout.xaxis.title = 'Date'
                g.layout.yaxis.title = 'Usage'

    # Register handler function with widgets
    list_idx.observe(response, names='value')
    recalc_outlier.observe(response, names="value")
    center_window.observe(response, names="value")
    window_size.observe(response, names="value")
    dev_size.observe(response, names="value")

    # return Interactive Plot
    return widgets.VBox([container, container2, container3, g])
