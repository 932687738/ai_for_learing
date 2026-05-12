from pathlib import Path

# 碰到AttributeError: module 'backend_interagg' has no attribute 'FigureCanvas'. Did you mean: 'FigureCanvasAgg'?
# 把下面这行放开
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd


def main():
    data_path = Path(__file__).resolve().parent.parent / "data" / "students.csv"
    df = pd.read_csv(data_path)

    df["average_score"] = df[["math", "english", "programming"]].mean(axis=1)

    print("Data preview:")
    print(df.head())
    print("\nStats:")
    print(df.describe())

    top_students = df[df["average_score"] > 85]
    print("\nTop students:")
    print(top_students[["name", "average_score"]])

    plt.figure(figsize=(8, 4))
    plt.bar(df["name"], df["average_score"])
    plt.title("Average Score by Student")
    plt.xlabel("Name")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
