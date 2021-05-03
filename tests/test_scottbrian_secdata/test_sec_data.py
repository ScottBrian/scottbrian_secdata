"""test_sec_data.py module."""

# from datetime import datetime, timedelta
import pytest
# import sys
# import os
# from pathlib import Path
# import numpy as np
import pandas as pd  # type: ignore
# import string
# import math


# from typing import Any, List, NamedTuple
# from typing_extensions import Final

from scottbrian_secdata.sec_data import SecData, DataSetNotFound

# from scottbrian_utils.diag_msg import diag_msg
from scottbrian_utils.file_catalog import FileCatalog

import logging

logger = logging.getLogger(__name__)


###############################################################################
# TestSecData class
###############################################################################
class TestSecData:
    """TestSecData class."""

    def test_attempt_load_nonexistant_data_sets(self,
                                                sec_data: "SecData"
                                                ) -> None:
        """Test load gets error.

        Args:
            sec_data: pytest fixture instance of SecData (see conftest.py)

        """
        verify_sec_data_initialized(sec_data)

        # we are testing load for missing data sets
        logger.debug("about to attempt load sec data with bad date")
        with pytest.raises(DataSetNotFound):
            sec_data.load_sec_raw_ds(date="1929q1")

        assert sec_data.sub.empty
        assert sec_data.num.empty

        # sec_raw_data_dir = sec_data.ds_catalog.get_path('sec_raw_data_dir')
        # for dirpath, dirnames, files in os.walk(sec_raw_data_dir):
        #     print(f'{dirpath}:{dirnames}:{files}')

    def test_load_data_sets(self,
                            sec_data: "SecData"
                            ) -> None:
        """Test load is successful.

        Args:
            sec_data: pytest fixture instance of SecData (see conftest.py)

        """
        verify_sec_data_initialized(sec_data)

        logger.debug("about to load sec data")
        sec_data.load_sec_raw_ds(date="2020q1")

        assert not sec_data.sub.empty
        assert not sec_data.num.empty


###############################################################################
# connect disconnect verification
###############################################################################
def verify_sec_data_initialized(sec_data: "SecData") -> None:
    """Helper function to verify the sec_data instance is initialized.

    Args:
        sec_data: pytest fixture instance of SecData (see conftest.py)

    """
    assert isinstance(sec_data.ds_catalog, FileCatalog)
    assert isinstance(sec_data.sub, pd.DataFrame)
    assert isinstance(sec_data.num, pd.DataFrame)
    assert len(sec_data.ds_catalog) > 0
    assert sec_data.__repr__() == 'SecData(ds_catalog)'
