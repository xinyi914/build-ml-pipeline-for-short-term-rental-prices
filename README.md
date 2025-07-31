# Build an ML Pipeline for Short-Term Rental Prices in NYC
You are working for a property management company renting rooms and properties for short periods of 
time on various rental platforms. You need to estimate the typical price for a given property based 
on the price of similar properties. Your company receives new data in bulk every week. The model needs 
to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

In this project you will build such a pipeline.

# Github repository
https://github.com/xinyi914/build-ml-pipeline-for-short-term-rental-prices.git

the latest version is 1.2.1
# W&B link
https://wandb.ai/xinyimao914-georgia-institute-of-technology/nyc_airbnb?nw=nwuserxinyimao914


# To run thte whole pipeline using sample2.csv
```
mlflow run https://github.com/xinyi914/build-ml-pipeline-for-short-term-rental-prices.git -v 1.2.1 -P hydra_options="etl.sample='sample2.csv'"
```

# Environment
I am using mlflow==2.21.0, hydra-core=1.3.2 which is updated in environment.yml.
The environment can be created by
```
conda env create -f environment.yml
conda activate nyc_airbnb_dev
```

## License

[License](LICENSE.txt)
