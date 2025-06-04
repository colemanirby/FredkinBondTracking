import pandas as pd
import matplotlib.pyplot as plt
import os

def create_bonds_list(isMismatch, count):

    bonds = []
    letter = "m" if isMismatch else "u"
    for i in range(0, 2*count - 1, 2):
        bond_1 = letter + (i+1).__str__()
        bond_2 = letter + (i + 2).__str__()
        bonds.append(bond_1)
        bonds.append(bond_2)
    return bonds

def main():
    N = 64
    s = 2
    m = 1
    # os.makedirs("Plots/N"+N.__str__()+"/inter_bond_distances/s"+s.__str__()+"/", exist_ok = True)
    mismatch_bonds = create_bonds_list(True, m)
    up_cant_bonds = create_bonds_list(False, s)
    all_bonds = mismatch_bonds + up_cant_bonds
    filename = "m1_s2_bond_distances.csv"
    df = pd.read_csv(filename)
    distances_dict = {}
    final_bond_name: str
    if s == 0:
        final_bond_name = "m4"
    else:
        final_bond_name = "u"+ len(up_cant_bonds).__str__()
    prev_name = ""
    for bond in all_bonds:
        if bond == "m1":
            index_name = "m1-0"
            distances_dict[index_name] = df[index_name]
        elif bond == final_bond_name:
            index_name = "N-"+final_bond_name
            distances_dict[index_name] = df[index_name]
            index_name = final_bond_name + "-" + prev_name + "-1"
            distances_dict[index_name] = df[index_name]
        else:
            index_name = bond + "-" + prev_name + "-1"
            distances_dict[index_name] = df[index_name]
        prev_name = bond
    distances_df = pd.DataFrame(distances_dict)
    for col in distances_df.columns:
        # bond_distance_name = col.replace("m", " - ")
        bond_distance_name = "Inter Bond Distance " + col
        if col == "m1-0":
            bond_distance_name = "m1 Distance from Left Edge"
        elif col == "N-"+final_bond_name:
            bond_distance_name = final_bond_name + " Distance from Right Edge"
        
        plot_name = "Plots/Mismatches/inter_bond_distances_s2_m2_"+col+".jpg"
        distance_to_plot = distances_df[col]
        distance_to_plot.hist(bins=N)
        plt.title(bond_distance_name)
        plt.xticks(rotation = 45, fontsize = 5)
        plt.xlabel("Distance")
        plt.ylabel("Frequency")
        plt.yscale("log")
        plt.tight_layout()
        plt.savefig(plot_name, dpi = 600)
        plt.close()

        

if __name__ == "__main__":
    main()