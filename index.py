python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    # Load the Excel file
    return pd.read_excel(file_path)

def preprocess_data(data):
    # Convert year and quarter to a single datetime for better visualization
    data['Period'] = data['Year'].astype(str) + 'Q' + data['Quarter'].astype(str)
    return data

def plot_gender_distribution(data):
    sns.set_theme(style="whitegrid")
    gender_data = data.groupby(['Period', 'Type']).sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Period', y='Count', hue='Type', data=gender_data)
    plt.title("Beneficiaries Gender Distribution per Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Number of Beneficiaries")
    plt.legend(title="Gender")
    plt.show()

def main():
    file_path = 'path_to_your_file.xlsx'  # Path to your dataset
    raw_data = load_data(file_path)
    processed_data = preprocess_data(raw_data)
    plot_gender_distribution(processed_data)

if __name__ == "__main__":
    main()
