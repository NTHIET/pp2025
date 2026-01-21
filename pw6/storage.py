import pickle
import gzip
import os

files = "data_pickle.gz"
def save(mark_manager):
    with gzip.open(files, "wb") as f:
        pickle.dump(mark_manager, f)
        
def load():
    if not os.path.exists(files):
        return None
    with gzip.open(files, "rb") as f:
        return pickle.load(f)