import os
import shutil
from pathlib import Path
import nltk
import tensorflow as tf

def main():
    print("Getting NLTK Models")
    nltk_dir = Path.cwd()/"models"
    assert nltk_dir.exists()
    os.environ["NLTK_DATA"] = str(nltk_dir)
    nltk.download('stopwords', quiet=True)
    nltk.download('vader_lexicon', quiet=True)

    print("Getting IMDB Texts")
    texts_dir= Path.cwd()/"texts"
    assert texts_dir.exists()
    dataset_dir = texts_dir / 'aclImdb'
    train_dir = dataset_dir / 'train'
    url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
    text_dataset = tf.keras.utils.get_file("aclImdb_v1", url, untar=True, cache_dir=texts_dir, cache_subdir='')
    shutil.rmtree(train_dir/'unsup')

if __name__ == "__main__":
    main()
