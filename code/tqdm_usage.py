from tqdm import tqdm
from time import sleep

a = range(100)
a = tqdm(a)
for i in a:
    sleep(0.01)