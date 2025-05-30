import math

def calculate_excited_states(N, s):
    # print("div", division)
    numerator = 2 * (s + 1)
    k = ((N - 2*(s+1))/2).__int__()
    binomial = math.comb(N, k)
    result = binomial * numerator / N
    return result

def calculate_mismatch_states(N, s, m):
    # pure_ground_states = calculate_ground_states(N)
    # print("ground states: ", pure_ground_states)
    all_non_mismatch_states = 0
    # if s == 0:
    #     all_non_mismatch_states += calculate_excited_states(N,0)
    # else: 
    #     for s in range(1, s+1):
            # all_non_mismatch_states += calculate_excited_states(N,s)
    total_number_of_states = calculate_all_states(N, s, m)
    base_states = 0

    if m > 0:
        base_states = calculate_all_states(N, s , m - 1)
    
    combined_mismatch_states = total_number_of_states - base_states

    return combined_mismatch_states

def calculate_all_states(N, s, m):
    N_2 = (N/2).__int__()
    i_max = m + 1
    sum = 0
    for i in range(i_max + 1):
        num = 2 * (s + m - i) + 3
        den = N - 1
        division = num/den
        n = N - 1
        k = N_2 - (s + m + 2) + i
        binomial = math.comb(n,k)
        sum += division * binomial
    return sum


def slow_dyn(N):
    num = 5
    N_2 = (N/2).__int__()
    den = N_2 + 2

    binomial = math.comb(N - 2, N_2 - 3)
    result = (num/den)*binomial
    return result


def main():
    s = 0
    m = 0
    N = 8
    # print(calculate_mismatch_states(N, s, m))
    print(calculate_mismatch_states(N, s, m))
    # print(calculate_excited_states(N, s))
    # print(slow_dyn(N))

if __name__ == "__main__":
    main()