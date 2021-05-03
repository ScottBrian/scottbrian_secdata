"""scottbrian_algo1 sec_data.

========
sec_data
========

sec_data obtains fundamental data from the sec download txt files.

Use cases:

1) get a specific quarterly value for a specific company
2) get a specific annual value for a specific company
3) get a specific quarterly ratio for a specific company
4) get a specific annual ratio for a specific company
5) get a specific quarterly value for all companies
6) get a specific annual value for all companies
7) get a specific quarterly ratio for all companies
8) get a specific annual ratio for all companies

"""

import pandas as pd  # type: ignore
# import numpy as np
# import matplotlib.pyplot as plt
# import os
# from collections import Counter
# from datetime import timedelta,datetime
# from calendar import monthrange
# import plotly.express as px

# from pathlib import Path

from typing import Type, TYPE_CHECKING

# from plotly.subplots import make_subplots
# import plotly.graph_objects as go

from scottbrian_utils.file_catalog import FileCatalog
# from scottbrian_utils.flower_box import print_flower_box_msg

import logging

########################################################################
# logging
########################################################################
logging.basicConfig(filename='SecData.log',
                    filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s '
                           '%(levelname)s '
                           '%(filename)s:'
                           '%(funcName)s:'
                           '%(lineno)d '
                           '%(message)s')

logger = logging.getLogger(__name__)

########################################################################
# pandas options
########################################################################
pd.set_option('mode.chained_assignment', 'raise')
pd.set_option('display.max_columns', 15)


########################################################################
# Exceptions
########################################################################
class SecDataError(Exception):
    """Base class for exceptions in this module."""
    pass


class DataSetNotFound(SecDataError):
    """SecData attempt to load files that do not exist."""
    pass


class SecData:
    """SEC Data handler."""
    def __init__(self, ds_catalog: FileCatalog):
        """Instantiate the SecData.

        Args:
            ds_catalog: contain the paths for data sets

        :Example: instantiate SecData and print it

        >>> from scottbrian_secdata.sec_data import SecData
        >>> from scottbrian_utils.file_catalog import FileCatalog
        >>> from pathlib import Path
        >>> ds_catalog = FileCatalog({'sub': Path('t_datasets/sub.txt'),
        ...                           'num': Path('t_datasets/num.txt')})
        >>> sec_data = SecData(ds_catalog)
        >>> print(sec_data)
        SecData(ds_catalog)

        """
        self.ds_catalog = ds_catalog
        self.sub = pd.DataFrame()
        self.num = pd.DataFrame()

    ###########################################################################
    # __repr__
    ###########################################################################
    def __repr__(self) -> str:
        """Return a representation of the class.

        Returns:
            The representation as how the class is instantiated

        :Example: instantiate AlgoApp and print it

        >>> from scottbrian_secdata.sec_data import SecData
        >>> from scottbrian_utils.file_catalog import FileCatalog
        >>> from pathlib import Path
        >>> ds_catalog = FileCatalog({'sub': Path('t_datasets/sub.txt'),
        ...                           'num': Path('t_datasets/num.txt')})
        >>> sec_data = SecData(ds_catalog)
        >>> print(sec_data)
        SecData(ds_catalog)

        """
        if TYPE_CHECKING:
            __class__: Type[SecData]
        classname = self.__class__.__name__
        parms = 'ds_catalog'

        return f'{classname}({parms})'

    def load_sec_raw_ds(self, date: str) -> None:
        """Load sec raw data sets for given date.

        Args:
            date: identifies the sec raw files to load (e.g., '2020q1')

        Raises:
            DataSetNotFound: the raw data sets were not found

        """
        #######################################################################
        # if raw data set exists, load it and reset the index
        #######################################################################
        sec_raw_data_dir = self.ds_catalog.get_path('sec_raw_data_dir')
        logger.info(f'path: {sec_raw_data_dir}')

        sub_path = sec_raw_data_dir / date / 'sub.txt'
        if not sub_path.exists():
            raise DataSetNotFound(f'{sub_path} not found')
        else:
            self.sub = pd.read_csv(sub_path,
                                   sep='\t',
                                   dtype={'cik': str, 'name': 'string'})

        num_path = sec_raw_data_dir / date / 'num.txt'
        if not num_path.exists():
            raise DataSetNotFound(f'{num_path} not found')
        else:
            self.num = pd.read_csv(num_path,
                                   sep='\t',
                                   dtype={'cik': str, 'name': 'string'})

    def split_sub(self) -> None:
        """Split the sub data set into 10-K and 10-Q data frames."""
        pass

    def split_num(self) -> None:
        """Split the num data set into 10-K and 10-Q data frames."""
        pass
