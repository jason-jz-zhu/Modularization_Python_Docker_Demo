import sys
import pandas as pd

from demo.logger import get_log

LOG = get_log(__name__)

def get_data(path: str) -> pd.DataFrame:
    """Read data.

    Given a data path, return the dataframe.

    Args:
        path: data path

    Returns:
        The raw dataframe is returned.
    """
    try:
        raw_df = pd.read_csv(path)
        LOG.info(f"data: retrieved [{raw_df.shape[0]}] records")
    except Exception as error:
        LOG.exception(f"data: source data could not be loaded. {error}")
        sys.exit(1)

    if raw_df.shape[0] == 0:
        LOG.exception(f"data: source data empty.")
        sys.exit(1)

    return raw_df

def deduplicate_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Deduplicate data.

    Given a dataframe, return the dedup dataframe.

    Args:
        path: dataframe

    Returns:
        The dedup dataframe is returned.
    """
    try:
        dedup_df = raw_df.drop_duplicates()
        LOG.info(f"data: deduplicate [{len(raw_df) - len(dedup_df)}] records")
    except Exception as error:
        LOG.exception(f"data: deduplicate could not be completed. {error}")
        sys.exit(1)
    return dedup_df

def generate_metric(dedup_df: pd.DataFrame) -> pd.DataFrame:
    """Generate metric.

    Given a dataframe, return the metric dataframe.

    Args:
        path: dataframe

    Returns:
        The metric dataframe is returned.
    """
    try:
        dedup_us_df = dedup_df[dedup_df['Country_Region'] == 'US']
        cleaned_df = dedup_us_df.copy()
        cleaned_df['month'] = pd.DatetimeIndex(cleaned_df['Date']).month
        cleaned_df['year'] = pd.DatetimeIndex(cleaned_df['Date']).year
        metric_df = cleaned_df.groupby(['Province_State', 'year', 'month'])["ConfirmedCases"].sum()
        LOG.info(f"data: generate_metric [{metric_df.shape[0]}] records")
    except Exception as error:
        LOG.exception(f"data: generate_metric could not be completed. {error}")
    return metric_df


def print_demo(s: str):
    print(s)