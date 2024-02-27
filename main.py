import time
import numpy as np

if __name__ == '__main__':
    max = int(1e8)
    print(f'max={max:e}')

    t_start = time.time()
    tab = [i for i in range(max)]
    t_stop = time.time()
    print(f'Generation time | loop:{t_stop - t_start}')

    t_start = time.time()
    tab = [i + 10 for i in tab]
    t_stop = time.time()
    print(f'Loop+10:{t_stop - t_start}')

    t_start = time.time()
    tab_np = np.arange(max)
    t_stop = time.time()
    print(f'\nGeneration time | numpy:{t_stop - t_start}')

    t_start = time.time()
    tab_np = tab_np + 10
    t_stop = time.time()
    print(f'Numpy+10:{t_stop - t_start}')
