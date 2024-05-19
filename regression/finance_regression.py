#!/usr/bin/python

"""
     Kode awal untuk proyek mini regresi.
    
     Memuat/memformat versi kumpulan data yang dimodifikasi
     (mengapa dimodifikasi? kami telah menghilangkan beberapa titik masalah
     bahwa kamu akan menemukan diri kamu dalam proyek mini outlier).

     Menggambar sedikit diagram sebar dari data pelatihan/pengujian

     Kamu mengisi kode regresi yang ditunjukkan:

     Author : Hafizh H Asyhari
     usr : hafizhhasyhari
"""

import sys
import pickle
from sklearn.linear_model import LinearRegression
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### daftarkan fitur yang ingin kamu lihat--item pertama di
### daftar akan menjadi fitur "target".
features_list = ["bonus", "salary"]
#features_list = ["bonus", "long_term_incentive"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### pemisahan pelatihan-pengujian diperlukan dalam regresi, sama seperti klasifikasi
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"

