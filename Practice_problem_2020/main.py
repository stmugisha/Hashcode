# M: max. number of pizza slices
# N: num of different pizza types
# S: num of slices in each pizza type (S[n-1] <= M)
import numpy as np


def read(filename: str) -> (int,int,list):
    """Read an input file"""
    with open(filename, 'r') as file:
        M, N = map(int, file.readline().rstrip('\n').split())
        S = [list(map(int, line.rstrip('\n').split())) for line in file]
        S = S[0]
        t = [i for i in range(len(S))]
        S = dict(list(zip(t, S)))
    return (M, N, S)


def orders(d: dict, N: int, M: int) -> list:
    """Computes and return a slice(sub-array) of `d`
    whose elements have a combined sum less than or equal
    to `M`.
    """
    current_sum = d[0]
    #max_sum = 0
    pizza_list = []
    start = 0

    for i in d.keys():
        current_sum += d[i]
        if(current_sum > M):
            current_sum -= d[start]
            start += 1
        else:
            pizza_list.append(i)
    #print(f'Max_sum: {max_sum}')   
    return pizza_list

def write(outputfile: str, typelist: list):
    """Writes the results of `typelist` to a text file.
    Args:
    `outputfile`: The name of the file to write to.

    `typelist`  : A list of pizza types to order.
    """
    with open(outputfile, 'w') as out:
        type_count = len(typelist)
        out.write(''.join([str(type_count), '\n']))
        for t in typelist:
            out.write(''.join([str(t), ' ']))


if __name__=='__main__':
    inputfiles = ['a_example.in','b_small.in','c_medium.in',
                  'd_quite_big.in','e_also_big.in']

    outfiles = ['example.out', 'small.out', 'medium.out',
                'q_big.out', 'big.out']

    for f in range(4):
        M, N, S = read('./in/'+ str(inputfiles[f]))
        print(f'M:{M}\nN:{N}\nS:{S}')
        t_list = orders(S, N, M)
        print(f'Orders: {t_list}')
        write('./out/'+str(outfiles[f]), t_list)