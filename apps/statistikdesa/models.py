from django.db import models
from django.conf import settings

# Create your models here.
class KartuKeluarga(models.Model):
    no_kk = models.CharField(max_length=16, primary_key=True)
    nama_kk = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    rt = models.IntegerField()
    rw = models.IntegerField()
    kelurahan = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    kode_pos = models.IntegerField()
    provinsi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kk





class Penduduk(models.Model):
    nik = models.CharField(max_length=16, primary_key=True)
    no_kk = models.ForeignKey(KartuKeluarga,on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=30)
    tempat_lahir = models.CharField(max_length=100)
    tgl_lahir = models.DateField(auto_now= False, auto_now_add=False)
    golongan_darah = models.CharField(max_length=20, null=True)
    Agama = models.CharField(max_length=100)
    status_perkawinan = models.CharField(max_length=100)
    hubungan_keluarga = models.CharField(max_length=100)
    pendidikan = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    kewarganegaraan = models.CharField(max_length=50)



    def __str__(self):
        return self.nama
    


    


