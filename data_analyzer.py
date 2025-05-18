import pandas as pd
import plotly.express as px

class SmartDataExplorer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)  # Load data
    
    def analyze(self):  # ⚠️ Method name must match (no typos)
        stats = {
            "missing_values": self.df.isnull().sum().to_dict(),
            "data_types": self.df.dtypes.to_dict()
        }
        return stats
    
    def plot(self, column):
        if self.df[column].nunique() > 10:
            return px.histogram(self.df, x=column)  # Histogram for numbers
        else:
            return px.bar(self.df[column].value_counts())  # Bar chart for categories