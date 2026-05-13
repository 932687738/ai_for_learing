"""第 2 课实践任务 4：不调用 sklearn，手写梯度下降拟合 y ≈ w*x + b。"""
import numpy as np


def main():
    # 固定随机种子，每次运行得到同一组伪数据
    rng = np.random.default_rng(42)
    n = 100
    # 在 [-2, 2] 上均匀采样 x，再加小噪声，真实关系约为 y = 2*x + 1
    x = rng.uniform(-2.0, 2.0, size=n)
    noise = rng.normal(0.0, 0.1, size=n)
    y_true_w, y_true_b = 2.0, 1.0
    y = y_true_w * x + y_true_b + noise

    # 从零点起步，用梯度下降学 w、b
    w, b = 0.0, 0.0
    lr = 0.05
    epochs = 1000

    for _ in range(epochs):
        pred = w * x + b
        err = pred - y
        # MSE = mean(err^2)；对 w、b 求导后得到 batch 梯度（与教材推导一致）
        grad_w = 2.0 * np.mean(err * x)
        grad_b = 2.0 * np.mean(err)
        w -= lr * grad_w
        b -= lr * grad_b

    pred_final = w * x + b
    mse_final = np.mean((pred_final - y) ** 2)
    print("final w =", round(w, 6), "final b =", round(b, 6))
    print("final MSE =", round(mse_final, 6))
    print("(target roughly w=2, b=1)")


if __name__ == "__main__":
    main()
