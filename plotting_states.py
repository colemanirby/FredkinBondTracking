import math 
import pandas as pd
import matplotlib.pyplot as plt

def calculate_states(N, s):
    division = (2 * (s + 1)/N).__int__()
    # print("div", division)
    numerator = 2 * (s + 1)
    k = ((N - 2*(s+1))/2).__int__()
    # print("k", k)
    # print("N", N)
    binomial = math.comb(N, k)
    result = binomial * numerator / N

    return result



def main():

    N = 6
    s = 0

    print(calculate_states(N, s))
    print(calculate_states(N+2, s))

    # N = 6

    # s_min = 1
    # s_max =(N/2 - 1).__int__()

    # count = []
    # index = []
    # for s in range(s_min, s_max + 1):
    #     index.append(s)
    #     count.append(calculate_states(N, s))

    # df = pd.DataFrame(data = count, index = index)
    # df.plot(kind = "bar")

    # plt.title("Number of states as a function of s, N = 64")
    # plt.ylabel("f(64, s)")
    # plt.xlabel("s")
    
    # # plt.savefig("nos_N64.jpg", dpi = 600)
    # plt.show()

    # N_max = 64

    # s = 1

    # states = []
    # chain_size = []

    # N_min = 2*(s+1)

    # for N in range(N_min, N_max + 1, 2):
    #     chain_size.append(N)
    #     states.append(math.log10(calculate_states(N, s)))

    # chain_size.reverse()
    # states.reverse()
    
    # df = pd.DataFrame(data = states, index = chain_size)
    # df.plot(kind = "bar")
    # plt.title("Number of states as a function of N, s = 1")
    # plt.ylabel("log10(f(N, 1))")
    # plt.xlabel("N")
    
    # # plt.savefig("nos_s1.jpg", dpi = 600)
    # plt.show()
        


if __name__ == "__main__":
    main()