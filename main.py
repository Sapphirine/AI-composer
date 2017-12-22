import urllib
import zipfile
import datacleanandmodel
import rnn

# collect the data
#url = "http://www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
#urllib.urlretrieve(url, "dataset.zip")

zip = zipfile.ZipFile(r'dataset.zip')  
zip.extractall('data')  

# build the model
datacleanandmodel.create_model()

# train the model
rnn.train_model()
