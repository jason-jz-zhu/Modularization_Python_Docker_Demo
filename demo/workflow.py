from functools import partial
import time
from datetime import date
import os
import configparser
from typing import Dict, List


import pandas as pd

from demo.pipeline import Pipeline
from demo.logger import get_log
from demo.utils import get_data, deduplicate_data, generate_metric

LOG = get_log(__name__)

pipeline = Pipeline()

@pipeline.task()
def get_raw_data(path: str) -> pd.DataFrame:
    raw_df = get_data(path)
    return raw_df

@pipeline.task(depends_on=get_raw_data)
def clean_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    dedup_df = deduplicate_data(raw_df)
    return dedup_df

@pipeline.task(depends_on=clean_data)
def get_metric(dedup_df: pd.DataFrame) -> pd.DataFrame:
    metric_df = generate_metric(dedup_df)
    return metric_df

@pipeline.task(depends_on=get_metric)
def save_metric(metric_df: pd.DataFrame) -> None:
    metric_df.to_csv('/demo/data/output.csv')


def demo_workflow():
    start = time.time()

    LOG.info("get data path from config: begin")
    config = configparser.ConfigParser()
    config.read('/demo/config/demo.cfg')
    path = config['project_info']['data_path']
    # path = '/demo/data/demo.csv'
    # print(path)
    LOG.info("get data path from config: end")
    
    pipeline.run(path)
    end = time.time()
    LOG.info('Whole process take {} ms'.format((end - start) * 1000.0))

    
