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
        
    # i_counts = df["i_indices"].value_counts()
    # j_counts = df["j_indices"].value_counts()
    # k_counts = df["k_indices"].value_counts()
    # l_counts = df["l_indices"].value_counts()
    # # m_counts = df["m_indices"].value_counts()
    # # n_counts = df["n_indices"].value_counts()

    # i_counts_filled = i_counts.reindex(all_positions, fill_value=0)
    # j_counts_filled = j_counts.reindex(all_positions, fill_value=0)
    # k_counts_filled = k_counts.reindex(all_positions, fill_value=0)
    # l_counts_filled = l_counts.reindex(all_positions, fill_value=0)
    # # m_counts_filled = m_counts.reindex(all_positions, fill_value=0)
    # # n_counts_filled = n_counts.reindex(all_positions, fill_value=0)

    # i_position_probabilities = i_counts_filled/i_counts_filled.sum()
    # i_position_probabilities.plot(kind='bar')
    # # plt.show(block = True)
    # plt.title("P(i) at specific index N = ")
    # plt.xticks(rotation = 45, fontsize = 5)
    # plt.xlabel("index")
    # plt.ylabel("P(i)")
    # plt.tight_layout()
    # plt.savefig("i_position_dist.jpg", dpi = 600)
    # plt.close()
    # j_position_probabilities = j_counts_filled/j_counts_filled.sum()
    # j_position_probabilities.plot(kind='bar')
    # plt.xticks(rotation = 45, fontsize = 5)
    # # plt.show(block = True)
    # plt.title("P(j) at specific index")
    # plt.xlabel("index")
    # plt.ylabel("P(j)")
    # plt.savefig("j_position_dist.jpg", dpi = 600)
    # plt.close()
    # k_position_probabilities = k_counts_filled/k_counts_filled.sum()
    # k_position_probabilities.plot(kind='bar')
    # plt.xticks(rotation = 45, fontsize = 5)
    # plt.title("P(k) at specific index")
    # plt.xlabel("index")
    # plt.ylabel("P(k)")
    # plt.savefig("k_position_dist.jpg", dpi = 600)
    # plt.close()
    # # plt.show(block = True)
    # l_position_probabilities = l_counts_filled/l_counts_filled.sum()
    # l_position_probabilities.plot(kind='bar')
    # plt.xticks(rotation = 45, fontsize = 5)
    # # plt.show()
    # plt.title("P(l) at specific index")
    # plt.xlabel("index")
    # plt.ylabel("P(l)")
    # plt.savefig("l_position_dist.jpg", dpi = 600)
    # plt.close()

    # # m_position_probabilities = m_counts_filled/m_counts_filled.sum()
    # # m_position_probabilities.plot(kind = 'bar')
    # # plt.xticks(rotation = 45, fontsize = 5)
    # # # plt.show()
    # # plt.title("P(m) at specific index")
    # # plt.xlabel("index")
    # # plt.ylabel("P(m)")
    # # plt.savefig("m_position_dist.jpg", dpi = 600)
    # # plt.close()

    # # n_position_probabilities = n_counts_filled/n_counts_filled.sum()
    # # n_position_probabilities.plot(kind = "bar")
    # # plt.xticks(rotation = 45, fontsize = 5)
    # # # plt.show()
    # # plt.title("P(n) at specific index")
    # # plt.xlabel("index")
    # # plt.ylabel("P(n)")
    # # plt.savefig("n_position_dist.jpg", dpi = 600)
    # # plt.close()

    # jmim1 = df["jmim1"]
    # jmim1.hist(bins = N, edgecolor = "black")
    # plt.title("Distribution of Distances (1k runs)")
    # plt.xlabel("j-i-1")
    # plt.ylabel("Frequency")
    # plt.grid(True)
    # # plt.show()
    # plt.savefig("ji_distance.jpg", dpi = 600)
    # plt.close()

    # # Nmj = df["Nmj"]
    # # Nmj.hist(bins = N, edgecolor = "black")
    # # plt.title("Distribution of Distances (1k runs)")
    # # plt.xlabel("N - j")
    # # plt.ylabel("Frequency")
    # # plt.grid(True)
    # # plt.savefig("Nj_distances.jpg", dpi = 600)
    # # plt.close()

    # kmjm1 = df["kmjm1"]
    # kmjm1.hist(bins = N, edgecolor = "black")
    # plt.title("Distribution of Distances (10k runs)")
    # plt.xlabel("k-j-1")
    # plt.ylabel("Frequency")
    # plt.grid(True)
    # # plt.show()
    # plt.savefig("kj_distance.jpg", dpi = 600)
    # plt.close()

    # lmkm1 = df["lmkm1"]
    # lmkm1.hist(bins = N, edgecolor = "black")
    # plt.title("Distribution of Distances (10k runs)")
    # plt.xlabel("l-k-1")
    # plt.ylabel("Frequency")
    # plt.grid(True)
    # # plt.show()
    # plt.savefig("lk_distance.jpg", dpi = 600)
    # plt.close()

    # # Nml = df["Nml_list"]
    # # Nml.hist(bins = N, edgecolor = "black")
    # # plt.title("Distribtuion of Distances from right edge")
    # # plt.xlabel("N-l")
    # # plt.ylabel("Frequency")
    # # plt.grid(True)
    # # plt.savefig("Nl_distance.jpg", dpi = 600)
    # # plt.close()

    # # mmlm1 = df["mmlm1"]
    # # mmlm1.hist(bins = 128, edgecolor = "black")
    # # plt.title("Distribution of Distances (10k runs)")
    # # plt.xlabel("m-l-1")
    # # plt.ylabel("Frequency")
    # # plt.grid(True)
    # # # plt.show()
    # # plt.savefig("ml_distance.jpg", dpi = 600)
    # # plt.close()

    # # nmmm1 = df["nmmm1"]
    # # nmmm1.hist(bins = 128, edgecolor = "black")
    # # plt.title("Distribution of Distances (10k runs)")
    # # plt.xlabel("n-m-1")
    # # plt.ylabel("Frequency")
    # # plt.grid(True)
    # # # plt.show()
    # # plt.savefig("nm_distance.jpg", dpi = 600)
    # # plt.close()

    # # Nmn = df["Nmn"]
    # # Nmn.hist(bins = 128, edgecolor = "black")
    # # plt.title("Distribution of Distances (10k runs)")
    # # plt.xlabel("N - m")
    # # plt.ylabel("Frequency")
    # # plt.grid(True)
    # # # plt.show()
    # # plt.savefig("Nn_distance.jpg", dpi = 600)
    # # plt.close()

    # # i_position_probabilities.plot(kind='bar')
    # # j_position_probabilities.plot(kind='bar')
    # # k_position_probabilities.plot(kind='bar')
    # # l_position_probabilities.plot(kind='bar')

    # # df_probs = pd.DataFrame({"i": i_position_probabilities, "j": j_position_probabilities, "k": k_position_probabilities, "l": l_position_probabilities, "m": m_position_probabilities, "n": n_position_probabilities})
    # df_probs = pd.DataFrame({"i": i_position_probabilities, "j": j_position_probabilities, "k": k_position_probabilities, "l": l_position_probabilities})
    # # df_probs = pd.DataFrame({"i": i_position_probabilities, "j": j_position_probabilities})

    # df_probs.plot(kind = 'bar', width = 1.0)
    # plt.title("Positional Probabilities")
    # plt.xticks(rotation = 45, fontsize = 5)
    # plt.xlabel("Index")
    # plt.ylabel("Probability")
    # plt.legend()
    # # plt.tight_layout()

    # plt.savefig("all_probabilities.jpg", dpi = 600)
    # plt.close()

    # df_spread = pd.DataFrame({"i": df["i_indices"], "ji": df["jmim1"], "kj": df["kmjm1"], "lk": df["lmkm1"], "Nk": k})

    # df_spread.plot.hist(bins = 100, edgecolor = "black")
    # # i.hist(bins = 100)
    # # jmim1.hist(bins = 100)
    # # kmjm1.hist(bins = 100)
    # # lmkm1.hist(bins = 100)
    # # k.hist(bins = 100)

    # plt.legend()

    # plt.show()




    # print(i_counts)
    # print(i_position_probabilities)

if __name__ == "__main__":
    main()