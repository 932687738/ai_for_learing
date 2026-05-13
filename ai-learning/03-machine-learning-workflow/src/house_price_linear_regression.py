"""
第 3 课：教材「房价预测最小示例」闭环脚本。

流程：读 CSV -> 取特征 X / 标签 y -> 划分 train / test -> LinearRegression 训练
-> 在测试集上 predict -> 算 MAE/MSE/RMSE/R2 -> 打印逐条误差。

数据：与本目录上一级的 data/houses_ml.csv 配套；运行前在项目根
ai-learning/03-machine-learning-workflow/ 下执行：
  python src/house_price_linear_regression.py
依赖见仓库根目录 README.md（pandas、scikit-learn 等）。
"""
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def main() -> None:
    # parents[1] = 同时含有 data/ 与 src/ 的目录（本课项目根）
    project_root = Path(__file__).resolve().parents[1]
    data_file = project_root / "data" / "houses_ml.csv"

    # 整表读入；数值列在此示例中已是数字类型
    df = pd.read_csv(data_file)

    # 特征列：模型「看得见」的输入；勿把 price 混进特征
    feature_columns = ["area", "rooms", "age", "distance_to_subway"]
    target_column = "price"

    X = df[feature_columns]
    y = df[target_column]

    # 80% 训练、20% 测试；random_state 固定划分便于复现实验结果
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = LinearRegression()
    # 仅用训练集的 (X, y) 更新模型内部权重与截距
    model.fit(X_train, y_train)

    # 测试集只做 predict，不向模型泄露 y_true
    y_pred = model.predict(X_test)

    # 离线把预测与真实标签对比得到指标；单位与教材一致（此处与 CSV 数值同量级）
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, y_pred)

    # coef_[i] 与 feature_columns[i] 一一对应，便于检查符号是否合理
    print("Model coefficients:")
    for name, coef in zip(feature_columns, model.coef_):
        print(f"{name}: {coef:.4f}")
    print(f"intercept: {model.intercept_:.4f}")
    print()

    print("Evaluation:")
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2: {r2:.4f}")
    print()

    # error > 0 表示预测偏高，< 0 表示预测偏低（与教材写法一致）
    result = X_test.copy()
    result["actual_price"] = y_test
    result["predicted_price"] = y_pred
    result["error"] = result["predicted_price"] - result["actual_price"]

    print("Prediction details:")
    print(result)


if __name__ == "__main__":
    main()
