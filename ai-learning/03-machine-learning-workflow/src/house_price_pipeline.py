"""
第 3 课：教材「使用 Pipeline 改造房价预测」。

在 house_price_linear_regression.py 基础上，用 StandardScaler + LinearRegression 组成 Pipeline，
保证训练与预测时对特征使用同一套缩放（见第十五节）。

数据：../data/houses_ml.csv。在项目根 ai-learning/03-machine-learning-workflow/ 下执行：
  python src/house_price_pipeline.py
依赖：pandas、scikit-learn（见仓库根目录 README.md）。
"""
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def evaluate(y_true, y_pred) -> None:
    """打印与教材一致的回归指标（测试集上 y 与预测值对比）。"""
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse ** 0.5
    r2 = r2_score(y_true, y_pred)

    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2: {r2:.4f}")


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_file = project_root / "data" / "houses_ml.csv"

    df = pd.read_csv(data_file)

    feature_columns = ["area", "rooms", "age", "distance_to_subway"]
    target_column = "price"

    X = df[feature_columns]
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    # 步骤名 "scaler" / "model" 在 GridSearchCV 里会用作 model__xxx 前缀
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression()),
    ])

    # fit：先仅在 X_train 上拟合 scaler，再用缩放后的 X_train 训练线性回归
    pipeline.fit(X_train, y_train)

    # predict：对 X_test / 新样本先 transform 再线性预测，避免忘做标准化
    y_pred = pipeline.predict(X_test)

    print("Test set metrics:")
    evaluate(y_test, y_pred)
    print()

    # 单行新房特征：列名与顺序须与训练时 feature_columns 一致
    new_house = pd.DataFrame([
        {
            "area": 118,
            "rooms": 3,
            "age": 6,
            "distance_to_subway": 1.6,
        }
    ])

    predicted_price = pipeline.predict(new_house)
    print(f"Predicted price for new house: {predicted_price[0]:.2f}")


if __name__ == "__main__":
    main()
