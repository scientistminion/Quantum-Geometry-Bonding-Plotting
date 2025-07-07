import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Load the updated CSV file
df = pd.read_csv('bonding_data.xlsx - Sheet1.csv')

# Inspect the DataFrame to confirm 'Material Type' column
print(df.head())
print(df.info())

# Extract relevant columns
materials = df['Material Name'].tolist()
conductivity_peak = df['Conductivity Peak'].to_numpy()
sqrtG_over_A = df['sqrt(G)/A'].to_numpy()
material_types = df['Material Type'].tolist()

# Define colors for the material types
# I will define a comprehensive set of colors, ensuring uniqueness for likely material types.
unique_material_types = df['Material Type'].unique()
color_map = plt.cm.get_cmap('tab10', len(unique_material_types)) # Use a colormap to get distinct colors
custom_colors = {m_type: color_map(i) for i, m_type in enumerate(unique_material_types)}

# Assign colors based on the 'Material Type'
colors = [custom_colors.get(m_type, 'grey') for m_type in material_types]

# Plot
plt.figure(figsize=(15, 12)) # Increase figure size for better readability
for i in range(len(materials)):
    plt.scatter(conductivity_peak[i], sqrtG_over_A[i], color=colors[i], marker='x', s=120, linewidths=2.5)
    # Adjust text position slightly if needed to avoid overlap
    plt.text(conductivity_peak[i] + 0.1, sqrtG_over_A[i] + 0.01, materials[i],
             fontsize=9, fontweight='bold', color=colors[i], ha='left', va='bottom')

# Custom legend
legend_elements = [Line2D([0], [0], color=custom_colors[label], label=label, linewidth=3, marker='x')
                   for label in unique_material_types]
plt.legend(handles=legend_elements, title="Material Type", title_fontsize=16, fontsize=12,
           loc='center left', bbox_to_anchor=(1.02, 0.5), borderaxespad=0.)

# Formatting
plt.xlabel('Conductivity Peak (eV)', fontsize=14)
plt.ylabel(r'$\sqrt{G} / A$', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig("sqrtG_over_A_vs_conductivity_peak_from_updated_excel.png", dpi=300)
