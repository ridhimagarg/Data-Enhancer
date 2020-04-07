import os
import wget


def download_model(dir="."):
    """
    Download Tensorflow hub Sentence Encoder model

    Parameters
    ----------
    dir: str
        Directory where the dataset will be stored

    """

    dir = os.path.expanduser(dir)
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Download SQuAD 1.1
    print("Downloading Tensorflow v1.0 model...")

    dir_tfmodel = os.path.join(dir, "TFModel_1.0")
    tfmodel_url = [
        "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json",
        "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json",
    ]

    if not os.path.exists(dir_tfmodel):
        os.makedirs(dir_tfmodel)

    file = tfmodel_url.split("/")[-1]
    if os.path.exists(os.path.join(dir_tfmodel, file)):
        print(file, "already downloaded")
    else:
        wget.download(url=tfmodel_url, out=dir_tfmodel)

    