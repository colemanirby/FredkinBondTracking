import pandas as pd
import matplotlib.pyplot as plt
import os

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
        os.makedirs("Plots/N"+N.__str__()+"/inter_bond_distances/New/s"+s.__str__()+"/", exist_ok = True)
        bonds = create_bonds_list(s)
        filename = "Data/N"+N.__str__()+"/data_N"+N.__str__()+"_s"+s.__str__()+".csv"
        df = pd.read_csv(filename)
        distances_dict = {}
        number_of_bonds = len(bonds)
        final_bond_name = "u"+number_of_bonds.__str__()
        prev_name = ""
        for bond in bonds:
            if bond == "u1":
                index_name = "u1m0"
                distances_dict[index_name] = df[index_name]
            elif bond == final_bond_name:
                index_name = "Nm"+final_bond_name
                distances_dict[index_name] = df[index_name]
                index_name = final_bond_name + "m" + prev_name + "m1"
                distances_dict[index_name] = df[index_name]
            else:
                index_name = bond + "m" + prev_name + "m1"
                distances_dict[index_name] = df[index_name]

            prev_name = bond
        distances_df = pd.DataFrame(distances_dict)
        for col in distances_df.columns:
            bond_distance_name = col.replace("m", " - ")
            bond_distance_name = "Inter Bond Distance " + bond_distance_name
            if col == "u1m0":
                bond_distance_name = "u1 Distance from Left Edge"
            elif col == "Nm"+final_bond_name:
                bond_distance_name = final_bond_name + " Distance from Right Edge"
            
            plot_name = "Plots/N"+N.__str__()+"/inter_bond_distances/New/s"+s.__str__()+"/inter_bond_distances_N" + N.__str__() + "_s"+s.__str__()+"_"+col+".jpg"
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