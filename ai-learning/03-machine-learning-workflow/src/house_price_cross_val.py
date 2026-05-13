"""
第 3 课：教材第十七节「交叉验证」最小示例。

对「StandardScaler + LinearRegression」组成的 Pipeline 在整表上做 K 折交叉验证，
评分使用负 MAE（sklearn 约定：误差类指标用 neg_ 前缀，数值越大越好）。

数据：../data/houses_ml.csv。在项目根 ai-learning/03-machine-learning-workflow/ 下执行：
  python src/house_price_cross_val.py

严谨工程上应先留出**最终测试集**，仅对剩余训练数据做 CV（见教材 17.4）；本脚本为
与教材代码块一致、使用全表 X/y 演示 API（样本仅 20 条，折上分数波动大，仅供学习流程）。
"""
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_file = project_root / "data" / "houses_ml.csv"

    df = pd.read_csv(data_file)
    feature_columns = ["area", "rooms", "age", "distance_to_subway"]
    X = df[feature_columns]
    y = df["price"]

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression()),
    ])

    # neg_mean_absolute_error：返回负 MAE，取负后还原为 MAE（与教材一致）
    scores = cross_val_score(
        pipeline,
        X,
        y,
        cv=5,
        scoring="neg_mean_absolute_error",
    )

    mae_scores = -scores
    print("each fold MAE:", mae_scores)
    print("mean MAE:", round(float(mae_scores.mean()), 4))


if __name__ == "__main__":
    main()
