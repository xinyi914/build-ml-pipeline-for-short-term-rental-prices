#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################
    logger.info("Downloading raw data from W&B")
    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()

    df = pd.read_csv(artifact_path)

    logger.info("Dropping outliers")
    idx = df['price'].between(args.min_price,args.max_price)
    df = df[idx].copy()

    # logger.info("Dropping null values")
    # df = df.dropna()

    logger.info("Saving cleaned dataset to W&B")
    df.to_csv("clean_sample.csv",index=False)
    artifact = wandb.Artifact(
        args.output_artifact,
        type = args.output_type,
        description=args.output_description
    )
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str, ## INSERT TYPE HERE: str, float or int,
        help="Name of the input artifact", ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type= str, ## INSERT TYPE HERE: str, float or int,
        help="Name of the output_artifact", ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str, ## INSERT TYPE HERE: str, float or int,
        help="Type of the output artifact", ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str, ## INSERT TYPE HERE: str, float or int,
        help="Description of the output artifact", ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float, ## INSERT TYPE HERE: str, float or int,
        help="lower bound of outlier of the price", ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float, ## INSERT TYPE HERE: str, float or int,
        help="upper bound of outlier of the price", ## INSERT DESCRIPTION HERE,
        required=True
    )


    args = parser.parse_args()

    go(args)
