from functools import partial
from lambda_helper import lambda_handler
from src.mock_module_one import mock_module_one
from src.module_one import module_one


main_handler = partial(lambda_handler, module_one)
mock_handler = partial(lambda_handler, mock_module_one)
