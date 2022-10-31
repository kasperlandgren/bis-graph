import csv
import matplotlib.pyplot as plt
import numpy as np

colors = dict()
colors["DEATHKNIGHT"] = "#C41E3A"
colors["DRUID"] = "#FF7C0A"
colors["HUNTER"] = "#AAD372"
colors["MAGE"] = "#3FC7EB"
colors["PALADIN"] = "#F48CBA"
colors["PRIEST"] = "#FFFFFF"
colors["ROGUE"] = "#FFF468"
colors["SHAMAN"] = "#0070DD"
colors["WARLOCK"] = "#8788EE"
colors["WARRIOR"] = "#C69B6D"


def parse():
    result = dict()
    with open("loot.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        next(spamreader, None)
        for row in spamreader:
            name = row[0][:-len("-Ashbringer")]
            response = row[7]
            clas_s = row[9]
            if name not in result:
                result[name] = [clas_s, 0, 0]

            if response == "Bis" or response == "Giga-bis":
                result[name][1] += 1
            else:
                result[name][2] += 1

    data = []
    label = []
    color = []
    for player in result.keys():
        data.append(result[player][1])
        data.append(result[player][2])
        label.append(player + " Bis")
        label.append(player + " Upg")
        color.append(colors[result[player][0]])
        color.append(colors[result[player][0]])

    x_pos = np.arange(len(label))
    plt.rcParams['figure.figsize'] = [20, 10]
    plt.rcParams['font.size'] = '16'
    plt.bar(x_pos, data, color = color, edgecolor = 'black')
    plt.xticks(x_pos, label, rotation='vertical')
    plt.tight_layout()
    plt.savefig("loot.png")


if __name__ == "__main__":
    parse()