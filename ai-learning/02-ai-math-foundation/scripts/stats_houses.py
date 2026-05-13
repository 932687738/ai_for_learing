"""第 2 课实践任务 3：房价 CSV 描述统计；有 matplotlib 则画直方图。"""
from pathlib import Path

import pandas as pd

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def main():
    csv_path = Path(__file__).resolve().parent.parent / "data" / "houses.csv"
    df = pd.read_csv(csv_path)
    prices = df["price"]

    # 一维序列上直接调 pandas 的统计函数
    print("mean(price) =", prices.mean())
    print("var(price) =", prices.var())
    print("std(price) =", prices.std())
    idx_max = int(prices.idxmax())
    idx_min = int(prices.idxmin())
    print("max price row:", df.loc[idx_max].to_dict())
    print("min price row:", df.loc[idx_min].to_dict())

    if plt is None:
        print(
            "skip histogram: matplotlib not installed. "
            "Run: pip install matplotlib"
        )
        return

    plt.figure(figsize=(6, 4))
    plt.hist(prices, bins=5, edgecolor="black")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.title("Price Distribution")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
