"""
第 3 课：教材第十八节「保存模型」示意。

1）用与 house_price_pipeline 相同数据训练 Pipeline；
2）将整条 Pipeline（含 StandardScaler）用 joblib 写入 ../models/；
3）重新 load 后对新一行特征做 predict，校验与内存中 pipeline 一致。

运行（工作目录为 ai-learning/03-machine-learning-workflow）：
  python src/house_price_save_load.py

产物目录 ../models/ 已在仓库 .gitignore 中忽略；依赖见根目录 README.md（joblib 常随 scikit-learn 环境已有）。
"""
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_file = project_root / "data" / "houses_ml.csv"
    model_dir = project_root / "models"
    model_file = model_dir / "house_price_pipeline.joblib"

    df = pd.read_csv(data_file)
    feature_columns = ["area", "rooms", "age", "distance_to_subway"]
    X = df[feature_columns]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression()),
    ])
    pipeline.fit(X_train, y_train)

    model_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, model_file)
    print("saved:", model_file)

    loaded = joblib.load(model_file)
    new_house = pd.DataFrame([
        {
            "area": 118,
            "rooms": 3,
            "age": 6,
            "distance_to_subway": 1.6,
        }
    ])
    p0 = float(pipeline.predict(new_house)[0])
    p1 = float(loaded.predict(new_house)[0])
    print("predict in-memory:", round(p0, 4))
    print("predict after load: ", round(p1, 4))
    print("match:", abs(p0 - p1) < 1e-6)

    y_pred = loaded.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print("loaded model test MAE:", round(mae, 4))


if __name__ == "__main__":
    main()
