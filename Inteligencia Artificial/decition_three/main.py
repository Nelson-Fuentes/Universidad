import pprint
import math
import pandas as pd


def main(file):
    data = pd.read_csv(file,  index_col=0)
    print(data)
    columns = data.columns.drop('Clase')
    return build_node(data, columns)


def build_node(data, columns):
    entropy_data = entropy(data)
    dictionary = {}
    earnings = pd.DataFrame(columns=('Column', 'Earning'))
    entropies = {}
    for column in columns:
        earn_result = earning(data, column, entropy_data)
        earn = earn_result[0]
        entropies[column] = earn_result[1]
        earnings.loc[len(earnings)] = [column, earn]
    earnings = earnings.set_index('Column')
    major = earnings[['Earning']].idxmax().to_list()[0]
    node = entropies[major]
    columns = columns.drop(major)
    for value in node:
        new_data = data.loc[data[major] == value]
        if node[value] == 0:
            node[value] = new_data['Clase'].mode()[0]
        else:

            node[value] = build_node(new_data, columns)
    dictionary[major] = node
    return dictionary


def earning(data, column, entropy_current):
    earn = entropy_current
    unique_values = data[column].unique()
    entropies = {}
    for value in unique_values:
        data_value = data.loc[data[column] == value]
        entropy_value = entropy(data_value)
        entropies[value] = entropy_value
        earn = earn - len(data_value) / len(data) * entropy_value
    return earn, entropies


def entropy(data):
    size = len(data)
    positive = len(data.loc[data['Clase'] == '+'])
    negative = len(data.loc[data['Clase'] == '-'])
    if positive > 0:
        positive = (positive / size) * math.log2(positive / size)
    else:
        positive = 0
    if negative > 0:
        negative = negative / size * math.log2(negative / size)
    else:
        negative = 0
    return - positive - negative


if __name__ == '__main__':
    file = 'data.csv'
    three = main(file)
    print("\nÁRBOL RESULTADO\n")
    pprint.pprint(three, width=1)
