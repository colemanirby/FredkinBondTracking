import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
    N = 24
    min_sector = 1
    max_sector = 2
    max_sector_for_size = ((N/2) - 1).__int__()
    for s in range(min_sector, max_sector_for_size + 1):
        bonds = create_bonds_list(s)
        filename = "data_N"+N.__str__()+"_s"+s.__str__()+".csv"
        df = pd.read_csv(filename)
        all_positions = range(0, N)
        indices_dict = {}
        for bond in bonds:
            index_name = bond + "_index"
            indices_dict[index_name] = df[index_name]
        df_positions = pd.DataFrame(indices_dict)

        counts = {col: df[col].value_counts() for col in df_positions.columns}

        counts_df = pd.DataFrame(counts)
        counts_df = counts_df.fillna(0).astype(int)
        counts_df = counts_df.reindex(all_positions, fill_value=0)
        position_probs = counts_df.div(counts_df.sum())

        number_of_bonds = len(bonds)

        colors = [plt.cm.hsv(i/number_of_bonds) for i in range(number_of_bonds)]

        position_probs.plot(kind = 'bar', width = 1.0, color = colors)
        plt.title("Positional Probabilities")
        plt.xticks(rotation = 45, fontsize = 5)
        plt.xlabel("Index")
        plt.ylabel("Probability")
        plt.legend(fontsize = 'small',  bbox_to_anchor=(1, 1))
        plt.tight_layout()
        plot_name = "all_probabilities"+"N"+N.__str__()+"_s"+s.__str__()+".jpg"
        plt.savefig(plot_name, dpi = 600)
        plt.close()

if __name__ == "__main__":
    main()