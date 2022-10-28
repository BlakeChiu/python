from sklearn.metrics import accuracy_score
import numpy as np

def purity_score(y_true,y_pred):
    y_voted_labels = np.zeros(y_true.shape)

    labels = np.unique(y_true)
    ordered_labels = np.arange(labels.shape[0])
    for k in range(labels.shape[0]):
        y_true[y_true==labels[k]] = ordered_labels[k]

    labels = np.unique(y_true)

    bins = np.concatenate((labels, [np.max(labels)+1]), axis=0)

    for cluster in np.unique(y_pred):
        hist, _ = np.histogram(y_true[y_pred==cluster], bins=bins)

        winner = np.argmax(hist)
        y_voted_labels[y_pred==cluster] = winner

    return accuracy_score(y_true, y_voted_labels)

y_true=np.array([0,0,0,1,1,1,2])
y_pre=np.array([1,1,1,2,2,2,2])

print("純度為:",purity_score(y_true,y_pre)) #12/14