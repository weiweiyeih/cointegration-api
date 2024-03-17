from fastapi import FastAPI
import boto3
# from decouple import config
import os
# import statsmodels.api as sm
# import pandas as pd
# import numpy as np
from mangum import Mangum

WINDOW = 21

db = boto3.resource(
    'dynamodb',
    # aws_access_key_id = config('AWS_ACCESS_KEY_ID_COINT'),
    # aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY_COINT'),
    # region_name = config('AWS_REGION_NAME_COINT'),
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID_COINT'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY_COINT'),
    region_name = os.environ.get('AWS_REGION_NAME_COINT')
    ) 
table = db.Table('Cointegration') 

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def root():
    return {
        "message": "Thank you for using our API! This API is used to get the cointegrated pairs and latest z-score of pairs based on their hourly close prices on dYdX V3. More exchanges platforms will be included soon. It is essential for a pair trading strategy. Typically, you LONG a cointegrated pair when the z-score is below the pre-defined threshold and SHORT the pair when the z-score is above the pre-defined threshold. The z-score is calculated using the rolling window of 21 hours and the past 400 hours close prices. The data is updated hourly.",
        "endpoints": {
            "/dydxV3/cointegrated-pairs": "Get the cointegration pairs for dydxV3.",
        }
            }


@app.get("/dydxV3/cointegrated-pairs")
def dydxV3_cointegration_pairs():
    response = table.get_item(
    Key={
        'item_name': 'dydxV3_cointegrated_pairs'
    }
)
    return response['Item']

'''
@app.get("/dydxV3/z-score")
def get_z_score(ticker_1: str, ticker_2: str):
    # GET item dydxV3_prices
    dydxV3_prices = table.get_item(
        Key={
            'item_name': 'dydxV3_prices'
        }
    )
    series_1 = []
    series_2 = []
    for dict in dydxV3_prices['Item']['close_prices']:
        if ticker_1 in dict.keys():
            series_1 = dict[ticker_1]
        if ticker_2 in dict.keys():
            series_2 = dict[ticker_2]

    # Handle the case when the ticker is not found
    if series_1 == [] or series_2 == []:
        return {
            'error': 'Ticker not found. Please make sure the tickers are available on dydxV3 and symbols are correct, e.g. "BTC-USD".'
        }
    
    series_1 = np.array(series_1).astype(float) # To fix error: "(np.float)" -> "(float)"
    series_2 = np.array(series_2).astype(float)
    model = sm.OLS(series_1, series_2).fit()
    hedge_ratio = model.params[0]
    spread = series_1 - (hedge_ratio * series_2)

    # Calculate z-score
    spread_series = pd.Series(spread)
    mean = spread_series.rolling(center=False, window=WINDOW).mean()
    std = spread_series.rolling(center=False, window=WINDOW).std()
    x = spread_series.rolling(center=False, window=1).mean()
    zscore = (x - mean) / std
    
    # get the last z-score
    return {
        'ticker_1': ticker_1,
        'ticker_2': ticker_2,
        'latest_zscore': zscore.to_list()[-1],
        'updated_at': dydxV3_prices['Item']['latest_datetime']
        }
'''

# uvicorn main:app --reload