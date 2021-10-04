import pandas as pd
import orchest

## using pandas read_csv funtion to load csv files
train=pd.read_csv("Data/train.csv")
test=pd.read_csv("Data/test.csv")

## Displying the dataframe of both training and testing
print("Training Data\n")
print(train.head(3))
print("Testing Data\n")
print(test.head(3))

# Output the Vaccine data
print("\nOutputting converted Vaccine data...")
orchest.output((train, test), name="data")
print("Success!")