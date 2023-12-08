import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Plot test accuracies from multiple CSV files.")
parser.add_argument('csv_files', nargs='+', help='Paths to CSV files')
args = parser.parse_args()

# Create a figure with specified size
fig, ax = plt.subplots(figsize=(4, 2.5), layout="constrained")

# Loop through each CSV file
for csv_file in args.csv_files:
    data = pd.read_csv(csv_file)
    print(data['Test Accuracy'])
    ax.plot(data['Epoch'], data['Test Accuracy'], marker='o', label=f"{csv_file.replace('.csv','')}")

# After plotting the test accuracies and before saving the figure
ax.axhline(y=53, color='r', linestyle='-', label='Baseline (53%)')
# Adding labels and legend
ax.set_xlabel('Epoch')
ax.set_ylabel('Test Accuracy (%)')
ax.set_ylim(35, 60)
ax.legend()


# Save plot to a PDF file
plt.savefig('test_accuracy.pdf', format='pdf')

# Close the figure
plt.close(fig)

