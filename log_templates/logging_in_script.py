import logging
import example_lib

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def main():

    logger.info("begin script.")
    example_lib.do_something()
    logger.info("end script.")


if __name__ == "__main__":
    main()
