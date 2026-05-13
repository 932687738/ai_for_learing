"""
第 1 课脚本：pandas 读 CSV、简单聚合与柱状图。

数据：上一级目录 ../data/students.csv（相对本脚本）。
"""
from pathlib import Path

# 若遇 matplotlib 后端报错（常见于部分 IDE 环境），可先尝试指定 TkAgg（见注释）
# 碰到 AttributeError 与 FigureCanvasAgg 之类提示时再放开下行
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd


def main():
    # 定位到与本课 data 目录：scripts 的上级的 data
    data_path = Path(__file__).resolve().parent.parent / "data" / "students.csv"
    df = pd.read_csv(data_path)

    # 三门课按行求平均分，axis=1 表示沿列聚合到每一行
    df["average_score"] = df[["math", "english", "programming"]].mean(axis=1)

    print("Data preview:")
    print(df.head())
    print("\nStats:")
    print(df.describe())

    # 筛选平均分高于 85 的记录
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
