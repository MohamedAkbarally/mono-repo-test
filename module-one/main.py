from functools import partial
from lambda_helper import lambda_handler
from src.mock_module_one import mock_main_function
from src.module_one import main_function


main_handler = partial(lambda_handler, main_function)
mock_handler = partial(lambda_handler, mock_main_function)
