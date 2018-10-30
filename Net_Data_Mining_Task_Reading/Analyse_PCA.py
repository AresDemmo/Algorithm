from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

def PCAImage(d, num_components):
    w, h, c = d.shape
    new_P = np.zeros((w, num_components, 3))
    new_Q = np.zeros((num_components, h, 3))
    new_img = d.copy()
    for i in range(c):
        pca = PCA(n_components=num_components)
        P = pca.fit_transform(d[:, :, i])
        Q = pca.components_
        new_P[:, :, i] = P
        new_Q[:, :, i] = Q
        new_img[:, :, i] = np.clip(np.matmul(P, Q), 0, 255)
    return new_img

def main():
    img = misc.imread(r'Net_Data_Mining_Task_Reading\image\ucas.jpg')
    img = np.array(img, dtype=np.float64) / 255
    plt.subplot(2, 3, 1)
    plt.imshow(img)
    plt.title("Origin Image")

    for i in range(20, 70, 10):
        plt.subplot(2, 3, i / 10)
        plt.imshow(PCAImage(img, i))
        plt.title("r = " + str(i))
    plt.savefig('Net_Data_Mining_Task_Reading\\image\\Analyse_PCA.png')
    


if __name__ == '__main__':
    main()