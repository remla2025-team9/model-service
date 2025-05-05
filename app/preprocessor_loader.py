from sentiment_analysis_preprocessing.preprocess import *
from pandas import read_csv

if __name__ == '__main__':
    dataset = read_csv("data/training_data.tsv", delimiter="\t", quoting=3)
    preprocess(dataset['Review'].values.tolist(), save=True)
