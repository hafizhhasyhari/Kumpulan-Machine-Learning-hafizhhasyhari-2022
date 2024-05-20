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

### Regresi Anda mengarah ke sini!
### Harap beri nama reg, sehingga kode plot di bawah mengambilnya dan
### memplotnya dengan benar. Jangan lupa ubah test_color di atas dari "b" menjadi
### "r" untuk membedakan titik latihan dengan titik tes.
reg = LinearRegression()
reg.fit(feature_train, target_train)
print("Slope: ", reg.coef_)
print("Interception : ", reg.intercept_)
print("Score on Training set: ", reg.score(feature_train, target_train))
print("Score on Test set: ", reg.score(feature_test, target_test))

### menggambar diagram sebar, dengan titik pelatihan dan 
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 


### label untuk legenda
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")

### gambar garis regresi, setelah dikodekan mencoba:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass

reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b")
print("Slope Outlier: ", reg.coef_)

plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
