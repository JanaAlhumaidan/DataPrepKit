class DataPrepKit:
    import pandas as pd
    def __init__(self, data_path):
        self.data = self._read_data(data_path)
    
    def _read_data(self, data_path):
        if data_path.endswith('.csv'):
            return pd.read_csv(data_path)
        elif data_path.endswith('.xlsx'):
            return pd.read_excel(data_path)
        elif data_path.endswith('.json'):
            return pd.read_json(data_path)
        else:
            raise ValueError("Unsupported file format")

    def summary(self):
        return self.data.describe()

    def handle_missing_values(self, strategy='mean'):
        if strategy == 'drop':
            return self.data.dropna()
        elif strategy == 'mean':
            return self.data.fillna(self.data.mean())
        elif strategy == 'median':
            return self.data.fillna(self.data.median())
        else:
            raise ValueError("Invalid missing value strategy")

    def encode_categorical(self):
        return pd.get_dummies(self.data)
