import pandas as pd


def process_data():
    data = pd.read_csv("./data/data.csv")

    data = data.dropna(axis=0)
    data = data[data['age'].apply(pd.to_numeric, errors='coerce').notna()].dropna()
    data = data.astype({'name': pd.StringDtype(), 'age': pd.Int16Dtype()})
    data = data[data.apply(lambda x: x['age'] >= 0, axis=1)]
    
    print(f"The mean age of all individuals in the file is {data['age'].mean()}")


if __name__ == "__main__":
    process_data()


