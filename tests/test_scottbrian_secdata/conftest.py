"""conftest.py module for testing."""

# from datetime import datetime, timedelta, timezone
# import string
# import time
# import os
import pytest
# import pandas as pd  # type: ignore
from typing import Any

import shutil

from scottbrian_secdata.sec_data import SecData
from scottbrian_utils.file_catalog import FileCatalog
# from scottbrian_utils.diag_msg import diag_msg

# import queue
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# proj_dir = Path.cwd().resolve().parents[1]  # back two directories

# test_cat = \
#     FileCatalog({'symbols': Path(proj_dir / 't_datasets/symbols.csv'),
#                  'mock_contract_descs':
#                      Path(proj_dir / 't_datasets/mock_contract_descs.csv')
#                  })


###############################################################################
# sec_app
###############################################################################
@pytest.fixture(scope='function')
def sec_data(tmp_path: Any) -> "SecData":
    """Instantiate and return a SecData for testing.

    Args:
        tmp_path: pytest fixture for providing a temporary path

    Returns:
        An instance of SecData
    """
    ###########################################################################
    # create temp directories for testing
    ###########################################################################
    sec_raw_data_dir = tmp_path / "sec_raw_data"
    sec_raw_data_dir.mkdir()

    sec_df_data_dir = tmp_path / "sec_df_data"
    sec_df_data_dir.mkdir()

    ###########################################################################
    # copy sec data to temp directories
    ###########################################################################
    src_dir = Path('/home/Tiger/sec_data/')

    for qtr_dir in ['2018q2', '2020q1']:
        dst_dir = sec_raw_data_dir / qtr_dir
        dst_dir.mkdir()
        for file_name in ['sub.txt', 'num.txt']:
            src = src_dir / qtr_dir / file_name
            shutil.copy2(src, dst_dir)

    # for dirpath, dirnames, files in os.walk(sec_raw_data_dir):
    #     print(f'{dirpath}:{dirnames}:{files}')

    ds_catalog = FileCatalog({'sec_raw_data_dir': sec_raw_data_dir,
                              'sec_df_data_dir': sec_df_data_dir
                              })

    sec_data = SecData(ds_catalog)
    return sec_data
