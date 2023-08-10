import logging
import os
import rollbar

rollbar.init(
    os.environ.get("ROLLBAR_ACCESS_TOKEN"),
    environment=os.environ["ROLLBAR_ACCESS_TOKEN"]
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(function, event, _):
    logging.info("Lambda called")
    logging.info(f"Raw lambda event: {event}")
    try:
        return "hello world"
    except Exception as e:
        rollbar.report_exc_info()
        logging.exception("Main event loop exception occurred")
        raise e
