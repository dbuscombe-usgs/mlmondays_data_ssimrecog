
import os, zipfile
import tensorflow as tf

os.mkdir('data')
os.mkdir('data/tamucc')

folder = './data'
file = 'tamucc_subset_12class.zip'

url = "https://github.com/dbuscombe-usgs/mlmondays_data_ssimrecog/releases/download/0.1.0/"+file
filename = os.path.join(os.getcwd(), file)
print("Downloading %s ... " % (filename))
tf.keras.utils.get_file(filename, url)
print("Unzipping to %s ... " % (folder))
with zipfile.ZipFile(file, "r") as z_fp:
    z_fp.extractall("./"+folder)

try:
    os.remove(files_to_download)
except:
    pass
