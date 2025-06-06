import pandas as pd
import matplotlib.pyplot as plt
import math
import os

def main():
    N = 128
    sqrtN = math.floor(math.sqrt(N))
    min_sector = 3
    max_sector = 2
    max_sector_for_size = ((N/2) - 1).__int__()
    os.makedirs("Plots/N"+N.__str__()+"/Averages/UpCants/", exist_ok = True)
    
    bond_names = ["u2mu1m1", "u4mu3m1", "u6mu5m1"]
    for bond_name in bond_names:
        spin_sectors = []
        mean_collection = []
        variance_collection = []
        for s in range(min_sector, max_sector_for_size + 1):
            filename = "Data/N"+N.__str__()+"/data_N"+N.__str__()+"_s"+s.__str__()+".csv"
            df = pd.read_csv(filename)
            spin_sectors.append(s)
            df_vals = df[bond_name]
            mean = df_vals.mean()
            variance = df_vals.var()
            mean_collection.append(mean)
            variance_collection.append(variance)
    
        figure_name = "Plots/N"+N.__str__()+"/Averages/UpCants/"+bond_name+"_means.jpg"
        plotting_df = pd.DataFrame({"sectors": spin_sectors, "means": mean_collection, "variances": variance_collection })

        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='s = sqrt(N)')

        plt.scatter(plotting_df["sectors"], plotting_df["means"])
        plt.xlabel('s')
        plt.ylabel('<'+bond_name+'>')
        plt.title('Mean vs S, N = ' + N.__str__())
        plt.legend()
        plt.grid(True)
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()

        figure_name = "Plots/N"+N.__str__()+"/Averages/UpCants/"+bond_name+"_variances.jpg"
        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='s = sqrt(N)')
        plt.scatter(plotting_df["sectors"], plotting_df["variances"])
        plt.xlabel('s')
        plt.ylabel('Var('+bond_name+')')
        plt.title('Variance vs S, N = ' + N.__str__())
        plt.legend()
        plt.grid(True)
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()

    spin_names = ["u1_index", "u2_index", "u3_index", "u4_index", "u5_index", "u6_index"]
    for spin_name in spin_names:
        spin_sectors = []
        mean_collection = []
        variance_collection = []
        for s in range(min_sector, max_sector_for_size + 1):
            filename = "Data/N"+N.__str__()+"/data_N"+N.__str__()+"_s"+s.__str__()+".csv"
            df = pd.read_csv(filename)
            spin_sectors.append(s)
            df = df[spin_name]
            mean = df.mean()
            variance = df.var()
            mean_collection.append(mean)
            variance_collection.append(variance)
        plotting_df = pd.DataFrame({"sectors": spin_sectors, "means": mean_collection, "variances": variance_collection })
        figure_name = "Plots/N"+N.__str__()+"/Averages/UpCants/"+spin_name+"_position_means.jpg"
        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='s = sqrt(N)')

        plt.scatter(plotting_df["sectors"], plotting_df["means"])
        plt.xlabel('s')
        plt.ylabel('<'+spin_name+'>')
        plt.title('Mean Position vs S, N = '+N.__str__())
        plt.legend()
        plt.grid(True)
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()

        plt.axvline(x=sqrtN, color='black', linestyle='--', linewidth=2, label='s = sqrt(N)')
        plt.scatter(plotting_df["sectors"], plotting_df["variances"])
        plt.xlabel('s')
        plt.ylabel('Var('+spin_name+')')
        plt.title('Variance in Position vs S N = '+N.__str__())
        plt.grid(True)
        figure_name = "Plots/N"+N.__str__()+"/Averages/UpCants/"+spin_name+"_position_variances.jpg"
       
        plt.legend()
        plt.savefig(figure_name, dpi = 600)
        # plt.show()
        plt.close()
    

        

if __name__ == "__main__":
    main()