import random, time

class SpinChain:

    chain: list[any]
    up_cant_bonds: dict[int, any]
    mismatch_bonds: dict[int, any]
    all_bonds: dict[int, any]

    def __init__(self, length: int, sector, mismatches, up_cant_bonds, mismatch_bonds):
        random.seed(time.time())
        self.chain = [0]*length
        self.spin_sector = sector
        self.up_cant_bonds = up_cant_bonds
        self.mismatch_bonds = mismatch_bonds
        self.all_bonds = up_cant_bonds + mismatch_bonds
        self.create_chain(length, sector, mismatches)
        

    def create_chain(self, length, sector, mismatches):
        self.chain[0] = 1
        self.chain[length-1] = -1

        mismatch_sites = self.choose_excited_sites(length - 2 - 2*sector, mismatches, 2)
        m_offset = mismatch_sites[len(mismatch_sites) - 1] + 1
        excited_sites = self.choose_excited_sites(length - m_offset, sector, m_offset)
        ##populate excited sites

        bond_index = 0
        if(sector > 0 ):
            for i in excited_sites:
                self.chain[i] = self.up_cant_bonds[bond_index]
                bond_index += 1
                # print("fosho no way")

        # print("Chain after u: ", self.chain.copy())
        mismatch_index = 0
        for j in mismatch_sites:
            self.chain[j] = self.mismatch_bonds[mismatch_index]
            mismatch_index+=1
            # print("aint no way")
        ##fill in Dyck words
        # print("Chain after m: ", self.chain.copy())
        self.populate_left_side(mismatch_sites[0])

        index = 1
        while index < len(mismatch_sites):
            left_bound_index = mismatch_sites[index - 1]
            right_bound_index = mismatch_sites[index]
            segment_length = right_bound_index - left_bound_index - 1
            self.generate_arbitrary_dyck_words(left_bound_index + 1, right_bound_index, segment_length)
            # print("STUCK :000000000")
            index +=1
        if sector == 0:
            last_bond_position = mismatch_sites[len(mismatch_sites) - 1]
            segment_length = length - last_bond_position - 1
            self.generate_arbitrary_dyck_words(last_bond_position + 1, length, segment_length)
        else:
            last_mismatch_site_position = mismatch_sites[len(mismatch_sites) - 1]
            segment_length = excited_sites[0] - last_mismatch_site_position - 1
            self.generate_arbitrary_dyck_words(last_mismatch_site_position+1, excited_sites[0], segment_length)
            index = 1
            while index < len(excited_sites):
                left_bound_index = excited_sites[index - 1]
                right_bound_index = excited_sites[index]
                segment_length = right_bound_index - left_bound_index - 1
                self.generate_arbitrary_dyck_words(left_bound_index + 1, right_bound_index, segment_length)
                index +=1
            last_bond_position = excited_sites[len(excited_sites) - 1]
            segment_length = length - last_bond_position - 1
            self.generate_arbitrary_dyck_words(last_bond_position + 1, length, segment_length)

    def populate_left_side(self, first_excited_bond_position):
        
        if first_excited_bond_position == 0:
            return
        elif first_excited_bond_position == 2:
            self.chain[1] = -1
            return
        self.generate_arbitrary_dyck_words(0, first_excited_bond_position, first_excited_bond_position)

    def generate_arbitrary_dyck_words(self, left_bound, right_bound, length):
        current_index = 1
        height = 1
        if length == 0:
            return
        elif length == 2:
            self.chain[left_bound] = 1
            self.chain[right_bound - 1] = -1
            return
        else:
            self.chain[left_bound] = 1
            self.chain[right_bound - 1] = -1

            for i in range(left_bound + 1, right_bound):
                num = random.uniform(0,1)
                numerator = (height + 2) * (length - current_index - height)
                denominator = 2 * (height + 1) * (length - current_index)

                prob_up = numerator/denominator

                if num <= prob_up :
                    self.chain[i] = 1
                    height += 1
                else:
                    self.chain[i] = -1
                    height -= 1
                current_index += 1

    def choose_excited_sites(self, N: int, s, offset) -> list[int]:
        m_o = m_e = 0

        i = 0

        sites = []
        
        while m_e != s or m_o != s:
            number = random.uniform(0,1)
            if i % 2 == 0:
                prob = 2*(s - m_e)/(N - 2 - i)
                if number <= prob:
                    sites.append(i + offset)
                    i += 1
                    m_e += 1
                else:
                    i = i+2
            else:
                prob = 2*(s - m_o)/(N - 1 - i)
                if number <= prob:
                    sites.append(i + offset)
                    i += 1
                    m_o += 1
                else:
                    i += 2
        return sites

    def evolve(self) -> bool:
        N = len(self.chain) - 1
        left_index = random.randint(0, N - 2)
        middle_index = left_index + 1
        right_index = middle_index + 1

        left_spin = self.chain[left_index]
        middle_spin = self.chain[middle_index]
        right_spin = self.chain[right_index]
        left_spin_value = self.determine_spin(left_spin)
        middle_spin_value = self.determine_spin(middle_spin)
        right_spin_value = self.determine_spin(right_spin)    

        is_chain_dead = False

        if left_spin in self.all_bonds or middle_spin in self.all_bonds or right_spin in self.all_bonds:
            is_chain_dead = self.dyck_swap(left_spin_value, middle_spin_value, right_spin_value, left_spin, middle_spin, right_spin, left_index, middle_index, right_index, N)
        else:
           self.direct_swap(left_spin_value, middle_spin_value, right_spin_value, left_index, middle_index, right_index, N)

        
        return is_chain_dead
    
    def dyck_swap(self, left_spin_value, middle_spin_value, right_spin_value, left_spin, middle_spin, right_spin, left_index, middle_index, right_index, N):
        is_chain_dead = False

        if left_spin in self.all_bonds:
            if middle_spin_value == 1 and right_spin_value == -1:
                if right_index == N:
                    is_chain_dead = True
                else:
                    # print("left spin was detected swapping", left_spin, middle_spin, right_spin)
                    self.chain[right_index] = left_spin
                    self.chain[middle_index] = right_spin
                    self.chain[left_index] = middle_spin
        elif right_spin in self.all_bonds:
            if left_spin_value == 1 and middle_spin_value == -1:
                if left_index == 0:
                    is_chain_dead = True
                else: 
                    # print("right spin was detected swapping", left_spin, middle_spin, right_spin)
                    self.chain[right_index] = middle_spin
                    self.chain[middle_index] = left_spin
                    self.chain[left_index] = right_spin
        return is_chain_dead

        

    def direct_swap(self, left_spin_value, middle_spin_value, right_spin_value, left_index, middle_index, right_index, N):
        if left_spin_value == 1:
            if middle_spin_value == 1 and right_spin_value == -1:
                if right_index == N:
                    raise Exception("Chain was killed in invalid way!!! Right Side")
                else:
                    self.chain[middle_index] = right_spin_value
                    self.chain[right_index] = middle_spin_value
            elif middle_spin_value == -1 and right_spin_value == 1:
                self.chain[middle_index] = right_spin_value
                self.chain[right_index] = middle_spin_value
            elif middle_spin_value == -1 and right_spin_value == -1 and left_index == 0:
                raise Exception("Chain was killed in invalid way!!! Left Side.")
            elif middle_spin_value == -1 and right_spin_value == -1:
                self.chain[middle_index] = left_spin_value
                self.chain[left_index] = middle_spin_value
        else:
            if middle_spin_value == 1 and right_spin_value == -1:
                self.chain[middle_index] = left_spin_value
                self.chain[left_index] = middle_spin_value

    def determine_spin(self, spin):
        spin_value = spin
        if spin in self.up_cant_bonds:
            spin_value =  1
        elif spin in self.mismatch_bonds:
            number = int(spin.replace("m",""))
            if number <= len(self.mismatch_bonds)/2:
                spin_value = -1
            else:
                spin_value = 1
        return spin_value