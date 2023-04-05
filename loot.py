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
    with open("loot.csv", newline='', encoding="latin1") as csvfile:
        spamreader = csv.reader(csvfile, quotechar='|')
        next(spamreader, None)
        for row in spamreader:
            name = row[0][:-len("-Mograine")].replace('"', "")
            response = row[7]
            clas_s = row[9]
            print(name)
            if name not in result:
                result[name] = [clas_s, 0, 0]

            if response == "Bis" or response == "Giga-bis":
                result[name][1] += 1
            else:
                result[name][2] += 1

    bis = []
    upg = []
    labels = []
    color = []
    for player in result.keys():
        bis.append(result[player][1])
        upg.append(result[player][2])
        labels.append(player)
        color.append(colors[result[player][0]])

    x_pos = np.arange(len(labels))
    width = 0.35
    plt.rcParams["figure.figsize"] = [20, 10]
    plt.rcParams["font.size"] = 16

    fig, ax = plt.subplots()
    upg_rects = ax.bar(x_pos + width/2, upg, width, color=color, edgecolor="black", alpha=0.72)
    bis_rects = ax.bar(x_pos - width/2, bis, width, color=color, edgecolor="black", linewidth=1.4)

    ax.set_ylabel("Antal items (ej off spec)")
    ax.set_xticks(x_pos, labels, rotation='vertical')

    fig.tight_layout()

    plt.savefig("loot.png")


if __name__ == "__main__":
    parse()