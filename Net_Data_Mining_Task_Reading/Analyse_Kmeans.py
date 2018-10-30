from sklearn.cluster import MiniBatchKMeans as Kmeans
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

def KmeansImage(d, num_components):
    w, h, c = d.shape
    new_img = d.copy()
    new_img = new_img.reshape(w * h, 3)
    model = Kmeans(n_clusters=num_components)
    model.fit(new_img)
    predict = model.predict(new_img)
    new_color = model.cluster_centers_[predict]
    new_img = new_color.reshape(d.shape)
    return new_img

def main():
    img = misc.imread(r'Net_Data_Mining_Task_Reading\image\ucas.jpg')
    img = np.array(img, dtype=np.float64) / 255
    plt.subplot(2, 3, 1)
    plt.imshow(img)
    plt.title("Origin Image")
    for i in range(2, 7, 1):
        plt.subplot(2, 3, i)
        plt.imshow(KmeansImage(img, i))
        plt.title("cluster = " + str(i))
    plt.savefig('Net_Data_Mining_Task_Reading\\image\\Analyse_Kmeans.png')
    


if __name__ == '__main__':
    main()