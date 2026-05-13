"""

第 2 课：广播 (broadcasting) 小实验。



演示 (3, 1) + (1, 3) -> (3, 3)，并用双重循环逐项核对 NumPy 结果。

第二段：(4, 3) + (3,) 为每一行加上同一偏置向量。

"""

import numpy as np





def main():

    # 形状 (3,1) 与 (1,3) 相加时 numpy 会自动「铺开」成 (3,3)

    col = np.array([[1.0], [2.0], [3.0]])

    row = np.array([[10.0, 20.0, 30.0]])



    print("col shape:", col.shape)

    print("row shape:", row.shape)



    out = col + row

    print("col + row shape:", out.shape)

    print("col + row =\n", out)



    # 逐元素手算应与 out[i,j] 一致

    print("\n逐项手算核对: out[i,j] 应等于 col[i,0] + row[0,j]")

    for i in range(3):

        for j in range(3):

            expected = col[i, 0] + row[0, j]

            got = out[i, j]

            ok = np.isclose(got, expected)

            print(f"  ({i},{j}): {col[i,0]:.1f} + {row[0,j]:.1f} = {expected:.1f}, np={got:.1f}, ok={ok}")



    # (4, 3) 矩阵每行加上长度为 3 的一维向量 bias（按最后一个轴对齐广播）

    print("\n对比: (4, 3) + (3,) 给每行加同一偏置向量")

    X = np.array([[1, 0, 2], [0, 1, 1], [2, 2, 0], [1, 1, 1]], float)

    bias = np.array([1.0, 0.0, -1.0])

    print("X + bias shape:", (X + bias).shape)





if __name__ == "__main__":

    main()

