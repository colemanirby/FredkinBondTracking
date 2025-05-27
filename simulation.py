from classes import SpinChain, Metrics
import pandas as pd

def main():
    number_of_runs = 1000
    metrics = Metrics()
    min_sector = 1
    max_sector = 2
    size = 64
    max_sector_for_size = ((size/2) - 1).__int__()
    # print(bonds)
    for current_sector in range(min_sector, max_sector_for_size + 1):
        data = {}
        bonds = create_bonds_list(current_sector)
        simulate(number_of_runs, data, current_sector, size, bonds)
        filename = "data_N"+size.__str__()+"_s"+current_sector.__str__()+".csv"
        df = pd.DataFrame(data)
        df.to_csv(filename)
    # print(data)

    # print(df)

    # df = create_data_frame(data)

    # df = pd.DataFrame({"i_indices": metrics.i_positions, "j_indices": metrics.j_positions,"jmim1": metrics.jmim1_list, "Nmj": metrics.Nmj_list})
    # df = pd.DataFrame({"i_indices": metrics.i_positions, "j_indices": metrics.j_positions, "k_indices": metrics.k_positions, "l_indices":metrics.l_positions, "jmim1": metrics.jmim1_list, "kmjm1": metrics.kmjm1_list, "lmkm1": metrics.lmkm1_list})
    # df = pd.DataFrame({"i_indices": metrics.i_positions, "j_indices": metrics.j_positions, "k_indices": metrics.k_positions, "l_indices":metrics.l_positions, "m_indices": metrics.m_positions, "n_indices": metrics.n_positions, "jmim1": metrics.jmim1_list, "kmjm1": metrics.kmjm1_list, "lmkm1": metrics.lmkm1_list, "mmlm1": metrics.mmlm1_list, "nmmm1": metrics.nmmm1_list, "Nmn": metrics.Nmn_list})
    
def simulate(number_of_runs, data, sector, size, bonds):
    
    for _ in range(number_of_runs):
        spin_chain = SpinChain(size, sector, bonds)
        is_dead = False
        while not is_dead:
           data = collect_data(data, spin_chain, bonds, sector)
           is_dead = spin_chain.evolve()
        print("completed ", _)       
        

def create_bonds_list(sector) -> list[str]:

    bonds = []
    for i in range(0, (2*sector) - 1, 2):
        bond_1 = "u" + (i+1).__str__()
        bond_2 = "u" + (i + 2).__str__()
        bonds.append(bond_1)
        bonds.append(bond_2)
    return bonds

def verify_chain(spin_chain: SpinChain):
    chain = spin_chain.chain
    sum = 0
    for spin in chain:
        if spin == "i" or spin == "j" or spin == "k" or spin == "l" or spin == 1:
            sum += 1
        else:
            sum -= 1
    if sum != 4:
        raise Exception("sum didnt equal 4 it was actually ", sum)

def collect_data(data: dict[str,list[int]], spin_chain: SpinChain, bonds, sector) -> dict[str,list[int]]:
    N = len(spin_chain.chain)
    max_bond = 2 * sector
    max_bond_name = "u" + max_bond.__str__()
    prev_name = ""
    for i in range(N):
        spin = spin_chain.chain[i]
        if spin in bonds:
            index_name = spin + "_index"
            if index_name not in data:
                data[index_name] = [i]
                if spin == "u1":
                    difference_name = "u1m0"
                    data[difference_name] = [i]
                elif spin == max_bond_name:
                    difference_name = spin+"m"+prev_name+"m1"
                    prev_index_key = prev_name + "_index"
                    prev_index = data[prev_index_key][0]
                    difference = i - prev_index - 1
                    data[difference_name] = [difference]

                    difference_name = "Nm"+max_bond_name
                    difference = len(spin_chain.chain) - i - 1
                    data[difference_name] = [difference]
                else:
                    difference_name = spin+"m"+prev_name+"m1"
                    prev_index_key = prev_name + "_index"
                    prev_index = data[prev_index_key][0]
                    difference = i - prev_index - 1
                    data[difference_name] = [difference]
            else:
                data[index_name].append(i)
                if spin == "u1":
                    difference_name = "u1m0"
                    data[difference_name].append(i)
                elif spin == max_bond_name:
                    difference_name = spin+"m"+prev_name+"m1"
                    prev_index_key = prev_name + "_index"
                    prev_index = data[prev_index_key][0]
                    difference = i - prev_index - 1
                    data[difference_name].append(difference)
                
                    difference_name = "Nm"+max_bond_name
                    difference = len(spin_chain.chain) - i - 1
                    data[difference_name].append(difference)
                else: 
                    prev_index_key = prev_name + "_index"
                    prev_index_array = data[prev_index_key]
                    prev_index = prev_index_array[len(prev_index_array)-1]
                    difference_name = spin + "m" + prev_name + "m1"
                    difference = i - prev_index
                    data[difference_name].append(difference)

            prev_name = spin

    return data


    #     if spin == "i":
    #         i_index = i
    #         metrics.i_positions.append(i_index)
    #     elif spin == "j":
    #         j_index = i
    #         metrics.j_positions.append(j_index)

    #     elif spin == "k":
    #         k_index = i
    #         metrics.k_positions.append(k_index)

    #     elif spin == "l":
    #         l_index = i
    #         metrics.l_positions.append(l_index)

    #     # elif spin == "m":
    #     #     m_index = i
    #     #     metrics.m_positions.append(m_index)
    #     # elif spin == "n":
    #     #     n_index = i
    #     #     metrics.n_positions.append(n_index)

    # jmim1 = j_index - i_index - 1
    # # Nmj = N - 1 - j_index
    # kmjm1 = k_index - j_index - 1
    # lmkm1 = l_index - k_index - 1
    # Nml = N - 1 - l_index
    # # mmlm1 = m_index - l_index - 1
    # # nmmm1 = n_index - m_index - 1
    # # Nn = N - 1 - n_index

    # metrics.jmim1_list.append(jmim1)
    # # metrics.Nmj_list.append(Nmj)
    # metrics.kmjm1_list.append(kmjm1)
    # metrics.lmkm1_list.append(lmkm1)
    # metrics.Nml_list.append(Nml)
    # metrics.mmlm1_list.append(mmlm1)
    # metrics.nmmm1_list.append(nmmm1)
    # metrics.Nmn_list.append(Nn)

if __name__ == "__main__":
    main()
