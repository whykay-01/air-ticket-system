import os

from matplotlib import pyplot as plt


def draw_barchart(sql_data, title, xlabel, ylabel, filename, color, name):
    total_amount = []
    labels = []
    for row in sql_data:
        labels.append(row[0])
        total_amount.append(row[1])

    # Create a vertical bar chart
    with plt.ion():
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(labels, total_amount, color=color)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.set_xticklabels(labels)

        # Display the exact value of each bar
        for i, v in enumerate(total_amount):
            ax.text(i, v / 2, "{:.0f}".format(v), ha="center", fontsize=12)

    filename = name + ".png"

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    fig.savefig(file_path)
    plt.close(fig)

    return filename