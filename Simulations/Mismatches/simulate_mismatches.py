from spin_chain_mismatches import SpinChain 
import pandas as pd
import time
import os
def main():
    min_N = 250
    max_N = 300
    # N = 64
    number_of_runs = 1000
    min_m = 1
    min_sector = 0

    for N in range(min_N, max_N, 2):    
        max_sector_for_size = (N/2 - 1).__int__()
        for s in range(min_sector, max_sector_for_size):
            max_m = (N/2 - 2 - s).__int__()
            for m in range(min_m, max_m + 1):
                os.makedirs("Data/N"+N.__str__()+"/Mismatches/s"+s.__str__()+"/lifetimes", exist_ok = True)
                os.makedirs("Data/N"+N.__str__()+"/Mismatches/s"+s.__str__()+"/spin_info/", exist_ok = True)
                lifetime_data = {}
                lifetime_data["lifetimes"] = []
                bond_distance_data = {}
                print("s ",s, "m ",m)
                s_bonds = create_bonds_list(False, s)
                m_bonds = create_bonds_list(True, m)
                simulate(number_of_runs, lifetime_data, bond_distance_data, N, m, s, m_bonds, s_bonds)
                print("completed")
                filename = "Data/N"+N.__str__()+"/Mismatches/s"+s.__str__()+"/lifetimes/m"+m.__str__()+"_lifetimes.csv"
                df = pd.DataFrame(lifetime_data)
                df.to_csv(filename)
                filename = "Data/N"+N.__str__()+"/Mismatches/s"+s.__str__()+"/spin_info/m"+m.__str__()+"_spin_info.csv"
                # for key in bond_distance_data:
                    # print(key , " ", len(bond_distance_data[key]))
                df_distances = pd.DataFrame(bond_distance_data)
                df_distances.to_csv(filename)

            # print(bond_distance_data)
        

    # print(lifetime_data)

        





def simulate(number_of_runs, lifetime_data, bond_distance_data, size, m, s, m_bonds, s_bonds):
    all_bonds = m_bonds + s_bonds
    count = 1
    for run in range(0, number_of_runs):

        spin_chain = SpinChain(size, s, m, s_bonds, m_bonds)
        # while not properly_shuffled:
        #     spin_chain = SpinChain(size, s, m, s_bonds, m_bonds)
        #     did_die = False
        #     for shuffle in range(0, size^2):
        #         did_die = spin_chain.evolve()
        #         if(did_die):
        #             break
        #     if not did_die:
        #         properly_shuffled = True 

        is_dead = False
        
        lifetime = 0
        
        while not is_dead:
            is_dead = spin_chain.evolve()
            lifetime+=1
            # if lifetime % (size/8) == 0:
            collect_data(bond_distance_data, spin_chain, all_bonds, s, m)
        lifetime_data["lifetimes"].append(lifetime)
    

def create_bonds_list(isMismatch, count):

    bonds = []
    letter = "m" if isMismatch else "u"
    for i in range(0, 2*count - 1, 2):
        bond_1 = letter + (i+1).__str__()
        bond_2 = letter + (i + 2).__str__()
        bonds.append(bond_1)
        bonds.append(bond_2)
    return bonds

def verify_chain(chain,m_bonds, s_bonds, final_height):
    sum = 0
    for i in range(len(chain)):
        if (i == 0 or i == 1) and chain[i] in m_bonds:
            print(chain)
            raise Exception("Invalid location", i, " populated by bond, ", chain[i])
        elif (i == len(chain)-1 or i == len(chain) - 2) and chain[i] in s_bonds:
            print(chain)
            raise Exception("Invalid location", i, " populated by bond, ", chain[i])
        else:
            bond = chain[i]
            if bond in s_bonds:
                sum+=1
            elif bond in m_bonds:
                numberletter = bond.replace("m", "")
                number = int(numberletter)
                if number % 2 == 0:
                    sum-=1
                else:
                    sum+=1
            else:
                sum+=bond
    if sum != final_height:
        print(chain)
        raise Exception("The count should have been: ", final_height, "but was ", sum)

def collect_data(data: dict[str,list[int]], spin_chain: SpinChain, bonds, sector, mismatch) -> dict[str,list[int]]:
    N = len(spin_chain.chain)
    max_upcant_bond = 2 * sector
    max_mismatch_bond = 2*mismatch
    max_bond_name = ""
    if sector == 0:
        max_bond_name = "m" + max_mismatch_bond.__str__()
    else:
        max_bond_name = "u" + max_upcant_bond.__str__()
    prev_name = ""
    for i in range(N):
        spin = spin_chain.chain[i]
        if spin in bonds:
            index_name = spin + "_index"
            if index_name not in data:
                data[index_name] = [i]
                if spin == "m1":
                    difference_name = "m1-0"
                    data[difference_name] = [i]
                elif spin == max_bond_name:
                    difference_name = spin + "-" + prev_name + "-1"
                    prev_index_key = prev_name + "_index"
                    prev_index = data[prev_index_key][0]
                    difference = i - prev_index - 1
                    data[difference_name] = [difference]
                    difference_name = "N-"+ max_bond_name
                    difference = len(spin_chain.chain) - i - 1
                    data[difference_name] = [difference]
                else:
                    difference_name = spin + "-" + prev_name + "-1"
                    prev_index_key = prev_name + "_index"
                    # print(spin_chain.chain)
                    prev_index = data[prev_index_key][0]
                    difference = i - prev_index - 1
                    data[difference_name] = [difference]
            else:
                data[index_name].append(i)
                if spin == "m1":
                    difference_name = "m1-0"
                    data[difference_name].append(i)
                elif spin == max_bond_name:
                    # print(spin_chain.chain)
                    difference_name = spin+"-"+prev_name+"-1"
                    prev_index_key = prev_name + "_index"
                    last_inserted_index = len(data[prev_index_key]) - 1
                    prev_index = data[prev_index_key][last_inserted_index]
                    difference = i - prev_index - 1
                    data[difference_name].append(difference)
                    difference_name = "N-"+max_bond_name
                    difference = len(spin_chain.chain) - i - 1
                    data[difference_name].append(difference)
                else: 
                    # print(spin_chain.chain)
                    prev_index_key = prev_name + "_index"
                    prev_index_array = data[prev_index_key]
                    prev_index = prev_index_array[len(prev_index_array)-1]
                    difference_name = spin + "-" + prev_name + "-1"
                    difference = i - prev_index - 1
                    data[difference_name].append(difference)
            prev_name = spin


    return data

if __name__ == "__main__":

    main()