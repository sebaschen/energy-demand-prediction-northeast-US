# Forecasting Daily Energy Consumption in the Northeastern US

This project focuses on the forecasting of daily energy consumption in the northeastern US using time-series analysis and machine learning techniques. The goal is to accurately predict the consumption pattern of energy per day based on existing data, enabling efficient energy allocation and ensuring a stable electricity supply for businesses and households.

## Abstract

The project aims to utilize machine learning methods to predict the daily energy consumption pattern in the northeastern US. By collecting seven years of energy consumption data (2012-2018) from PJME and evaluating it with autoregressive and recurrent neural network (RNN) models, the project explores the effectiveness of different algorithms. The study shows that while autoregressive models can provide reliable predictions with feature engineering, RNN models with LSTM structure yield more accurate results.

## Introduction

The project aims to develop machine learning models capable of accurately predicting the energy consumption per day based on a dataset collected from open sources. The predicted consumption values can then be used to optimize energy allocation through the smart grid, ensuring a steady supply and preventing potential blackouts. The project also provides an opportunity to explore time series prediction in machine learning, bridging the gap between data engineering and machine learning applications.

## Dataset

The project utilizes the PJME dataset, which contains daily energy consumption data in the northeastern US. The dataset, obtained from Kaggle, includes columns such as daily consumption. The goal is to determine the correlation between previous energy consumption data and the energy consumption at a given time, considering the temporal patterns and their impact on consumption.

## Methods

The project employs various techniques, including feature engineering, time-series analysis, and machine learning models, to forecast daily energy consumption. The feature engineering process involves leveraging the PJME production dataset and extracting meaningful information such as the quarter, month, year, and day of the year to gain insights into consumption trends. The dataset is divided into a training set (2012-2018) and a testing set (2018).(This Dataset is from Kaggle)

For modeling, two primary approaches are explored: an autoregressive model and an RNN model with LSTM structure. The autoregressive model considers previous consumption values as lag and utilizes linear regression to make predictions. On the other hand, the RNN model employs a deep learning architecture with LSTM units to overcome the gradient vanishing problem commonly faced by deep RNN networks.

## Results

The project's results demonstrate the effectiveness of the different models in predicting daily energy consumption. The autoregressive model with feature engineering yields reliable predictions, while the RNN model with LSTM structure achieves higher accuracy. The MAPE metric is used to evaluate the models, and the RNN model outperforms the autoregressive model, with a lower MAPE score.

## Conclusion

The project successfully addresses the problem of forecasting daily energy consumption in the northeastern US using time-series analysis and machine learning techniques. The developed models provide accurate predictions, enabling efficient energy allocation and contributing to a stable electricity supply. The findings highlight the potential of using machine learning methods to forecast energy consumption and guide decision-making in the energy sector.

---

*Note: The README structure provided above is a general guideline. Feel free to modify it based on the specific details and findings of your project.*

## Contributors

- [Li-Pu Chen](https://github.com/sebaschen/)
: Responsible for data preprocessing, feature engineering, and training autoregressive models to predict electricity consumption. Evaluated model performance using MAPE and MSE metrics.

- [Ziyan Liu](https://github.com/billyyliu/): Handled data preprocessing and trained LSTM models for electricity consumption prediction. Evaluated model performance using MSE metric and visualized predictions.

- [Kaiwen Hu](https://github.com/kevin00hu): Conducted data analysis, performed autocorrelation checks, and trained autoregressive models for electricity consumption prediction. Evaluated model performance using MAPE and MSE metrics and visualized predictions.
