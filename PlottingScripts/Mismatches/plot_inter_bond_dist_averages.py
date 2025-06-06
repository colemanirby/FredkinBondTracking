import pandas as pd
import matplotlib.pyplot as plt
import math
import os

def main():
    N = 64
    sqrtN = math.floor(math.sqrt(N))
    s = 1
    # max_sector_for_size = ((N/2) - 1).__int__()
    bond_names = ["m2-m1-1", "u2-u1-1"]

    os.makedirs("Plots/N"+N.__str__()+"/Averages/Mismatches/s"+s.__str__(), exist_ok = True)
    
    for bond_name in bond_names:
        mismatches = []
        mean_collection = []
        variance_collection = []
        min_m = 1
        max_m = (N/2 - 2 - s).__int__()
        # filename = "Data/N"+N.__str__()+"/Mismatches/s"+s.__str__()+"/spin_info/m"+m.__str__()+"_spin_info.csv"
        for m in range(min_m, max_m + 1):
            filename = "Data/N"+N.__str__()+"/Mismatches/s"+s.__str__()+"/spin_info/m"+m.__str__()+"_spin_info.csv"
            df = pd.read_csv(filename)
            mismatches.append(m)
            df = df[bond_name]
            mean = df.mean()
            variance = df.var()
            mean_collection.append(mean)
            variance_collection.append(variance)
    
        figure_name = "Plots/N"+N.__str__()+"/Averages/Mismatches/s"+s.__str__()+"/"+bond_name+"_means.jpg"
        plotting_df = pd.DataFrame({"sectors": mismatches, "means": mean_collection, "variances": variance_collection })

        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='s = sqrt(N)')

        plt.scatter(plotting_df["sectors"], plotting_df["means"])
        plt.xlabel('m')
        plt.ylabel('<'+bond_name+'>')
        plt.title('Mean vs m, N = ' + N.__str__() + 's = ' + s.__str__())
        plt.legend()
        plt.grid(True)
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()

        figure_name = "Plots/N"+N.__str__()+"/Averages/Mismatches/s"+s.__str__()+"/"+bond_name+"_variances.jpg"
        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='m = sqrt(N)')
        plt.scatter(plotting_df["sectors"], plotting_df["variances"])
        plt.xlabel('m')
        plt.ylabel('Var('+bond_name+')')
        plt.title('Variance vs m, N = ' + N.__str__() + 's = ' + s.__str__())
        plt.legend()
        plt.grid(True)
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()

    spin_names = ["m1_index", "m2_index", "u1_index", "u2_index"]
    for spin_name in spin_names:
        mismatches = []
        mean_collection = []
        variance_collection = []
        for m in range(min_m, max_m + 1):
            filename = "Data/N"+N.__str__()+"/Mismatches/s"+s.__str__()+"/spin_info/m"+m.__str__()+"_spin_info.csv"
            df = pd.read_csv(filename)
            mismatches.append(m)
            df = df[spin_name]
            mean = df.mean()
            variance = df.var()
            mean_collection.append(mean)
            variance_collection.append(variance)
        figure_name = "Plots/N"+N.__str__()+"/Averages/Mismatches/s"+s.__str__()+"/"+spin_name+"_position_means.jpg"

        plotting_df = pd.DataFrame({"sectors": mismatches, "means": mean_collection, "variances": variance_collection })
        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='s = sqrt(N)')

        plt.scatter(plotting_df["sectors"], plotting_df["means"])
        plt.xlabel('m')
        plt.ylabel('<'+spin_name+'>')
        plt.title('Mean Position vs m, N = '+N.__str__() + 's = ' + s.__str__())
        plt.legend()
        plt.grid(True)
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()

        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='s = sqrt(N)')
        plt.scatter(plotting_df["sectors"], plotting_df["variances"])
        plt.xlabel('m')
        plt.ylabel('Var('+spin_name+')')
        plt.title('Variance in Position vs m N = '+N.__str__() + 's = ' + s.__str__())
        plt.grid(True)
        figure_name = "Plots/N"+N.__str__()+"/Averages/Mismatches/s"+s.__str__()+"/"+spin_name+"_position_variances.jpg"
       
        plt.legend()
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()
    

        

if __name__ == "__main__":
    main()