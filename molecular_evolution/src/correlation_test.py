#!/usr/bin/env python3

import argparse
import sys
import pandas as pd
from scipy.stats import pearsonr, spearmanr
import statsmodels.api as sm

def ols_fit(data, predictor: str, response: str):
    '''
    Fits and print a Ordinary Least Squares model to the data.
    Data must be provided as a .csv file and specify the two
    variables that need to be modeled.
    '''
    # Data input
    df = pd.read_csv(data)
    # Variables definition
    x = df[predictor]
    X = sm.add_constant(x)  # Constant column needed for Statsmodels
    y = df[response]
    # Define and fit the model
    model = sm.OLS(y, X)
    model = model.fit()
    r_pearson = pearsonr(x, y)
    r_spearman = spearmanr(x, y)
    print(model.summary())
    print(f'''
              R^2                   {model.rsquared},
              Pearson Correlation   {r_pearson[0]},
              Spearman Correlation  {r_spearman[0]}''')

def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="Data file in .csvs format")
    parser.add_argument("predictor",
                        help="Name of the independent variable")
    parser.add_argument("response",
                        help="Name of the dependent variable")
    args = parser.parse_args()
    data = args.data
    predictor = args.predictor
    response = args.response
    return data, predictor, response

def main():
    data, predictor, response = arguments_parser()
    with open('conservation_correlation.log', 'w') as fh:
        sys.stdout = fh
        ols_fit(data, predictor, response)

if __name__ == "__main__":
    main()
