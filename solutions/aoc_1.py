import numpy as np

def one(df):
    df = df.apply(lambda x: x.sort_values().values)
    df['diff'] = abs(df['A'] - df['B'])
    return(sum(df['diff']))


def two(df):
    s = 0
    for n in df['A']:
        c = (df['B'] == n).sum()
        s += (n * c)
    return s