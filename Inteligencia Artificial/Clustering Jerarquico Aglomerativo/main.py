import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clear_column(column):
    new_column = []
    for value in column:
        new_column.append(value.replace(' ', ''))
    return new_column


def clear_data(data):
    data.columns = clear_column(data.columns)
    data[['']] = clear_column(data[''])
    data = data.set_index('')
    for i in range(len(data)):
        data.iat[i, i] = np.nan
    return data


def getMinIndexes(data):
    minimus = data.idxmin(skipna=True).dropna()
    for i, row in enumerate(minimus):
        minimus[i] = [data[minimus.index[i]][row], row, minimus.index[i]]
    return min(minimus)


def minna(a, b):
    if pd.notna(a):
        return min(a, b)
    return b


def maxna(a, b):
    if pd.notna(a):
        return max(a, b)
    return b


def meanna(a, b):
    if pd.notna(a):
        return (a + b) / 2.0
    return b

def add_row_and_column_to_data(data, column1, column2, function, label):
    new_column = (data.apply(lambda row: function(row[column1], row[column2]), axis=1))
    new_row = (data.apply(lambda row: function(row[column1], row[column2]), axis=0))
    new_row.name = label
    data = data.append(new_row, ignore_index=False)
    del (data[column1])
    del (data[column2])
    data[label] = new_column
    return  data.drop([column1, column2])


def cluster(data, function):
    levels = []
    if len(data.columns) > 1:
        minimun = getMinIndexes(data)
        label_minimun = minimun[1] + minimun[2]
        levels.append(minimun)
        data = add_row_and_column_to_data(data, minimun[1], minimun[2], function, label_minimun)
        #print(levels)
        #print(data)
        new_level, data = cluster(data, function)
        levels = levels + new_level

    return levels, data


def single_linkage(data):
    return cluster(data, minna)

def complete_linkage(data):
    return cluster(data, maxna)

def mean_linkage(data):
    return cluster(data, meanna)

def draw_dendogram(levels, axes, title):
    bottom_level = {}
    for level in levels:
        bottom_level[level[1]] = 0
        bottom_level[level[2]] = 0
    label_levels = {}
    for level in levels:
        a = level[1]
        b = level[2]
        ai = 0
        bi = 0
        if not a in label_levels:
            ai = len(label_levels) + 1
            label_levels[a] = ai
        else:
            ai = label_levels[a]
        if not b in label_levels:
            bi = len(label_levels) + 1
            label_levels[b] = bi
        else:
            bi = label_levels[b]
        label_levels[a + b] = (ai + bi) / 2
    label_levels_1 = []
    for level in label_levels.keys():
        label_levels_1.append([label_levels[level], level])
    label_levels_1 = sorted(label_levels_1)
    for level in label_levels_1:
        axes.plot([level[1]], [0])
    fig = plt.Figure()
    for level in levels:
        axes.set_title(title)
        axes.plot([level[1]], [0], 'b')
        axes.plot([level[1] + level[2]], [0], 'b')
        axes.plot([level[2]], [0], 'b')
        axes.plot([level[1], level[2]], [level[0]] * 2, 'b')
        axes.plot([level[1], level[1]], [bottom_level[level[1]], level[0]], 'b')
        axes.plot([level[2], level[2]], [bottom_level[level[2]], level[0]], 'b')
        axes.plot([level[1] + level[2]] * 2, [level[0]] * 2, 'b')
        axes.plot([level[1], level[1] + level[2]], [level[0]] * 2, 'b')
        axes.set(ylim=(0, 3))
        bottom_level[level[1] + level[2]] = level[0]




def main(file):
    data = pd.read_csv(file, sep='\t')
    data = clear_data(data)
    print(data)
    fig, ax = plt.subplots(1, 3, constrained_layout=True)
    levels, data1 = single_linkage(data)
    draw_dendogram(levels, ax[0], 'Single Linkage')

    levels, data2 = complete_linkage(data)
    draw_dendogram(levels, ax[1], 'Complete Linkage')

    levels, data3 = mean_linkage(data)
    draw_dendogram(levels, ax[2], 'Mean Linkage')
    plt.show()

if __name__ == '__main__':
    main('cluster.txt')
