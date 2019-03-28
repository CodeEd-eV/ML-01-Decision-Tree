from sklearn.model_selection import train_test_split
import tools.extract as ex
import os

def split(filename):
    return train_test_split(ex.load_file(filename), test_size=0.2)

def write_split(train, test, DIR):
    train.to_csv( os.path.join(DIR, "train.csv"), sep=",", encoding="utf-8", index=False) 
    test.to_csv( os.path.join(DIR, "test.csv"), sep=",", encoding="utf-8", index=False) 
    
if __name__ == "__main__" :
    train, test = split("data/adult/data.csv")
    write_split(train, test, "data/adult")
