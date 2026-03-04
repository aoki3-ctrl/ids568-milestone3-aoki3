from sklearn.datasets import load_iris
import pandas as pd

def preprocess():

    X, y = load_iris(return_X_y=True)

    df = pd.DataFrame(X)
    df["target"] = y

    df.to_csv("processed_data.csv", index=False)

    print("Data preprocessing complete")

if __name__ == "__main__":
    preprocess()