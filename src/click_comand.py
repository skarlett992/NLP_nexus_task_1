import click

from src.get_text import get_text
from src.log import set_log_level
from src.save_result import save_result


@click.command()
@click.option('--input', type=click.Path(exists=True), help="input file")
@click.option('--output',
              type=click.Path(exists=False, dir_okay=True),
              help="output text file")
@click.option('--verbose',
              type=click.BOOL,
              default=False,
              help="verbose mode ( output detailed logs )",
              required=False)
def get_params(input, output, verbose):
    click.echo(f'input: {input}, output: {output}, verbose: {verbose}')
    set_log_level(verbose)
    result_text = get_text([input])
    save_result(result_text, output)
