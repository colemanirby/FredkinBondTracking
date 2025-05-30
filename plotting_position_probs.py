import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns
from scipy.interpolate import PchipInterpolator
from io import StringIO

def create_bonds_list(sector) -> list[str]:

    bonds = []
    for i in range(0, (2*sector) - 1, 2):
        bond_1 = "u" + (i+1).__str__()
        bond_2 = "u" + (i + 2).__str__()
        bonds.append(bond_1)
        bonds.append(bond_2)
    return bonds

def main():
    N = 128
    min_sector = 1
    max_sector = 2
    max_sector_for_size = ((N/2) - 1).__int__()
    for s in range(min_sector, max_sector_for_size + 1):
        bonds = create_bonds_list(s)
        filename = "Data/N"+N.__str__()+"/data_N"+N.__str__()+"_s"+s.__str__()+".csv"
        df = pd.read_csv(filename)
        all_positions = range(0, N)
        indices_dict = {}
        for bond in bonds:
            index_name = bond + "_index"
            indices_dict[bond] = df[index_name]
        df_positions = pd.DataFrame(indices_dict)

        counts = {col: df_positions[col].value_counts() for col in df_positions.columns}

        counts_df = pd.DataFrame(counts)
        counts_df = counts_df.fillna(0).astype(int)
        counts_df = counts_df.reindex(all_positions, fill_value=0)
        position_probs = counts_df.div(counts_df.sum())

        
        # position_probs.plot(kind = 'bar', width = 1.0, color = colors, align = "center")
        # sns.heatmap(position_probs.T, cmap = "viridis", cbar_kws={'label': 'Probability'})
        color_index = 0
        x_fine = np.linspace(0, (N-1), num = 10000*N)
        x = position_probs.index.to_numpy()
        number_of_colors = len(bonds)
        colors = [plt.cm.turbo(i) for i in np.linspace(0,1,number_of_colors, endpoint=False)]
        for col in position_probs.columns:
            y = position_probs[col].to_numpy()
            f = PchipInterpolator(x, y)
            y_fine = f(x_fine)
            plt.plot(x_fine, y_fine, label = col, color = colors[color_index])
            plt.fill_between(x_fine, y_fine, alpha=0.3, color = colors[color_index])
            color_index+=1
        plt.title("Positional Probabilities")
        plt.xticks(rotation = 45, fontsize = 5)
        plt.xlabel("Index")
        plt.ylabel("Probability")
        ncol = math.ceil(len(bonds)/25)
        plt.legend(ncol = ncol, loc = "center left", fontsize = 'small',  bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plot_name = "Plots/N"+N.__str__()+"/all_probabilities"+"N"+N.__str__()+"_s"+s.__str__()+".jpg"
        plt.savefig(plot_name, dpi = 600)
        plt.close()

if __name__ == "__main__":
    main()