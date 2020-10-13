from demo.utils import deduplicate_data
import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal

RAW_TESTDATA = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 2, 3]]),
                   columns=['a', 'b', 'c'])

CLEAN_TESTDATA = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

def test_deduplicate_data():
    assert_frame_equal(deduplicate_data(RAW_TESTDATA), CLEAN_TESTDATA)