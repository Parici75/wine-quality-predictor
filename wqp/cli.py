import click

import wqp.workflow as wf
from wqp import __version__


@click.group(name="wqp", help="A command line tool to train a wine quality predictor")
@click.version_option(__version__)
def wqp():
    pass


@wqp.group(name="jobs", help="Set of commands to launch training or evaluation jobs")
def jobs():
    pass


@jobs.command(name="train", help="Executes the wine predictor training workflow")
@click.option("--data-path", "-d", help="The path were training data can be found")
def train(data_path: str):
    wf.model_training_workflow(data_path=data_path)
