import polars as pl

# Login using e.g. `huggingface-cli login` to access this dataset
df = pl.read_parquet('hf://datasets/allenai/WildChat-4.8M/data/train-*.parquet')
