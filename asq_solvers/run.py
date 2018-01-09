#!/usr/bin/env python
import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    level=logging.INFO)

from asq_solvers.commands import main  # pylint: disable=wrong-import-position
# Custom skidls modules for registering models, etc
import asq_solvers.service.predictors
import asq_solvers.data.dataset_readers
import asq_solvers.models
if __name__ == "__main__":
    main(prog="python -m skidls.run")
