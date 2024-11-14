import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from hmmlearn import hmm


# Step 1: Load data from CSV
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Step 2: Preprocess Data - Calculate log returns of 'Close' prices
def calculate_log_returns(df):
    df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))
    df = df.dropna()  # Remove the first row with NaN
    return df

# Step 3: Normalize/Standardize Data
def normalize_data(data, method="standardize"):
    data = data.values.reshape(-1, 1)  # Reshape for sklearn scaler
    if method == "minmax":
        scaler = MinMaxScaler(feature_range=(0, 1))
    elif method == "standardize":
        scaler = StandardScaler()
    else:
        raise ValueError("Invalid method specified. Use 'minmax' or 'standardize'.")
    normalized_data = scaler.fit_transform(data)
    return normalized_data, scaler

# Step 4: Train an HMM Model
def train_hmm_model(normalized_data, n_components=6):
    np.random.seed(42)  # Set a fixed random seed
    model = hmm.GaussianHMM(n_components=n_components, covariance_type="full", n_iter=100)
    model.fit(normalized_data)
    return model

# Main workflow
if __name__ == "__main__":
    # Load data
    file_path = "data_pipeline/data/BTCUSDT_historical_data_1h.csv"  # Update with your file path
    df = load_data(file_path)

    # Calculate log returns
    df = calculate_log_returns(df)

    # Normalize or standardize data
    normalized_data, scaler = normalize_data(df['log_return'], method="standardize")  # You can use "minmax" or "standardize"

    # Train HMM
    model = train_hmm_model(normalized_data)

    # 1. Transition Matrix
    print("Transition Matrix (State to State Transition Probabilities):")
    print(model.transmat_)

    # 2. Means of each Hidden State (Gaussian mean for each state)
    print("\nMeans of each hidden state:")
    print(model.means_)

    # 3. Covariances of each Hidden State (Gaussian variance for each state)
    print("\nCovariances of each hidden state:")
    print(model.covars_)

    # 4. Predicted Hidden States (State sequence for each data point)
    hidden_states = model.predict(normalized_data)
    print("\nPredicted Hidden States (Regimes):")
    print(hidden_states[:10])  # Display the first 10 hidden states

    # Optionally, add the predicted hidden states to the DataFrame
    df['hidden_states'] = hidden_states

    # Display the DataFrame with hidden states
    print("\nData with Hidden States:")
    print(df.head())


# TODO: log results