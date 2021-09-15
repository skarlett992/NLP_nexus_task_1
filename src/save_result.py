import os.path

from src.log import logger


def save_result(result_text, output_file):
    logger.info(
        f'Start save_result., saving result_text({len(result_text)}) into {output_file}'
    )

    if len(result_text) > 0 and not os.path.isfile(output_file):
        with open(output_file, "w") as fd:
            fd.write(result_text)

    logger.info('Finish save_result')
