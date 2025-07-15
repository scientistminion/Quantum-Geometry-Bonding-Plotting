import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Load the updated CSV file
df = pd.read_csv('bonding_data.xlsx - Sheet1.csv')

# Define the exact column names for x and y axes
x_column_name = '∫ σ(ω) dω'
y_column_name = 'sqrt(G)/A with bound'

# Explicitly convert columns to numeric, coercing errors
df[x_column_name] = pd.to_numeric(df[x_column_name], errors='coerce')
df[y_column_name] = pd.to_numeric(df[y_column_name], errors='coerce')

# Drop rows where critical plotting data is NaN in the specified columns
df.dropna(subset=[x_column_name, y_column_name, 'Material Type', 'Material Name'], inplace=True)

# Extract relevant columns AFTER cleaning
materials = df['Material Name'].tolist()
x_axis_data = df[x_column_name].to_numpy()
y_axis_data = df[y_column_name].to_numpy()
material_types = df['Material Type'].tolist()

# Define colors for the material types
unique_material_types = df['Material Type'].unique()
color_map = plt.cm.get_cmap('tab10', len(unique_material_types))
custom_colors = {m_type: color_map(i) for i, m_type in enumerate(unique_material_types)}

# Assign colors based on the 'Material Type'
colors = [custom_colors.get(m_type, 'grey') for m_type in material_types]

# Plot
plt.figure(figsize=(15, 12))
for i in range(len(materials)):
    plt.scatter(x_axis_data[i], y_axis_data[i], color=colors[i], marker='x', s=120, linewidths=2.5)
    plt.text(x_axis_data[i] + 0.01, y_axis_data[i] + 0.01, materials[i],
             fontsize=12, fontweight='bold', color=colors[i], ha='left', va='bottom')

# Custom legend
legend_elements = [Line2D([0], [0], color=custom_colors[label], label=label, linewidth=3, marker='x')
                   for label in unique_material_types]
plt.legend(handles=legend_elements, title="Material Type", title_fontsize=16, fontsize=12,
           loc='center left', bbox_to_anchor=(1.02, 0.5), borderaxespad=0.)

# Formatting
plt.xlabel(r'$\int \sigma(\omega) d\omega$', fontsize=14)
plt.ylabel(r'$\sqrt{G} / A$ with bound electrons', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig("sqrtG_over_A_with_bound_electrons_vs_sigma_omega_domega.png", dpi=300)
