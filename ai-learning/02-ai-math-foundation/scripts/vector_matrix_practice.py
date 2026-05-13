"""第 2 课实践任务 1：向量运算与矩阵乘法（NumPy）。"""
import numpy as np


def main():
    # 一维向量：形状 (3,)，逐元素加法与标量乘法
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 5.0, 6.0])

    print("a =", a, "shape =", a.shape)
    print("b =", b, "shape =", b.shape)
    print("a + b =", a + b)
    print("3 * a =", 3.0 * a)
    # 内积
    print("dot(a, b) =", np.dot(a, b))
    # L2 范数（欧氏长度）
    print("||a|| (L2) =", np.linalg.norm(a))
    print("||b|| (L2) =", np.linalg.norm(b))
    print("euclidean(a, b) =", np.linalg.norm(a - b))

    # (3,2) @ (2,1) -> (3,1)，线性代数里的矩阵乘
    m32 = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    m21 = np.array([[1.0], [2.0]])
    print("m32 shape =", m32.shape)
    print("m21 shape =", m21.shape)
    prod = m32 @ m21
    print("m32 @ m21 =", prod.flatten(), "shape =", prod.shape)


if __name__ == "__main__":
    main()
