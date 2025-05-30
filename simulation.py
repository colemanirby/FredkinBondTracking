from spin_chain import SpinChain
import pandas as pd

def main():
    number_of_runs = 100
    min_sector = 1
    max_sector = 2
    size = 128
    max_sector_for_size = ((size/2) - 1).__int__()
    for current_sector in range(min_sector, max_sector_for_size + 1):
        data = {}
        bonds = create_bonds_list(current_sector)
        simulate(number_of_runs, data, current_sector, size, bonds)
        filename = "Data/N"+size.__str__()+"/data_N"+size.__str__()+"_s"+current_sector.__str__()+".csv"
        df = pd.DataFrame(data)
        df.to_csv(filename)
    
def simulate(number_of_runs, data, sector, size, bonds):
    
    for _ in range(number_of_runs):
        spin_chain = SpinChain(size, sector, bonds)
        is_dead = False
        evolve_count = 0
        while not is_dead:
           if evolve_count % (size/8) == 0:
                data = collect_data(data, spin_chain, bonds, sector)
           is_dead = spin_chain.evolve()
           evolve_count += 1
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
                    last_inserted_index = len(data[prev_index_key]) - 1
                    prev_index = data[prev_index_key][last_inserted_index]
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

if __name__ == "__main__":
    main()
