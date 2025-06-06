import math

def calculate_excited_states(N, s):
    # print("div", division)
    numerator = 2 * (s + 1)
    k = ((N - 2*(s+1))/2).__int__()
    binomial = math.comb(N, k)
    result = binomial * numerator / N
    return result

# def calculate_mismatch_states(N, s, m):
#     # pure_ground_states = calculate_ground_states(N)
#     # print("ground states: ", pure_ground_states)
#     all_non_mismatch_states = 0
#     # if s == 0:
#     #     all_non_mismatch_states += calculate_excited_states(N,0)
#     # else: 
#     #     for s in range(1, s+1):
#             # all_non_mismatch_states += calculate_excited_states(N,s)
#     N_2 = (N/2).__int__()

#     if m + s >= N_2 - 1:
#         return 0
#     total_number_of_states = calculate_all_states(N, s, m)
#     base_states = 0

#     if m > 0:
#         base_states = calculate_all_states(N, s , m - 1)
    
#     combined_mismatch_states = total_number_of_states - base_states

#     return combined_mismatch_states

# def calculate_all_states(N, s, m):
#     N_2 = (N/2).__int__()
#     i_max = m + 1
#     sum = 0
#     for i in range(i_max + 1):
#         num = 2 * (s + m - i) + 3
#         den = N - 1
#         division = num/den
#         n = N - 1
#         k = N_2 - (s + m + 2) + i
#         binomial = math.comb(n,k)
#         sum += division * binomial
#     return sum

# def calculate_big_time(N,s,m):
#     numerator = 2 * (s + 1) + m
#     # N_2 = (N/2).__int__()
#     sum = 0
#     for i in range(100):
#         n_1 = N + m - (2 * i)
#         k_1 = N - 2*(s + 1) - i
#         n_2 = 1 + m - i
#         if n_2 == 0:
#             print("n_2 = 0")
#             print("n_1 = ", n_1)
#         k_2 = i
#         if n_2 > 0:
#             print("n_1 = ", n_1)
#             print("n_2 = ", n_2)
#             denominator = N + m - (2*i)
#             division = numerator/denominator
#             binomial_1 = math.comb(n_1, k_1)
#             binomaial_2 = math.comb(n_2, k_2)
#             product =  ((-1)**i)*division * binomial_1 * binomaial_2
#             print("bin 1 = ", binomial_1)
#             print("bin  2 = ", binomaial_2)
#             print("Product ", i + 1, " = ", product)
#             sum += product
#     return sum

# def naive_counting(N,s,m):
#     num = 2*(s + 1) + m
#     den = N - m
#     division = num/den
#     print("div", division)
#     N_2 = (N/2).__int__()
#     n = N - m
#     k = N_2 - s - 1

#     binomial = math.comb(n, k)

#     result = (binomial* num)/den

#     return result

def theorem_3(N, s, m): 
    i_max = m
    N_2 = (N/2).__int__()
    num = 2 * (s + 1) + m
    sum = 0
    for i in range(i_max + 1):
        pm_1 = (-1)**i
        den = N + m - (2 * i)

        n = N + m - (2 * i)

        k = N_2 - (s + 1) - i

        binomial_1 = math.comb(n, k)
        binomial_2 = math.comb(1 + m - i, i)

        result = pm_1 * num / den* binomial_1 * binomial_2

        sum += result
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
    m = 1
    N = 8

    print(theorem_3(N, s, m))
    print(theorem_3(N , s, 0) )

    # for i in range(m + 2):
    #     print(math.comb( 1 + m - i, i))

    # print(theorem_3(N, s, 2))
    # print(theorem_3(N, s, 1))
    # print(theorem_3(N, s, 0))
    # print(calculate_mismatch_states(N, s, m))
    # print(calculate_mismatch_states(N, s, m))
    # print(calculate_excited_states(N, s))
    # print(slow_dyn(N))

if __name__ == "__main__":
    main()