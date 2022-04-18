print ("Hesap makinesine hoş geldiniz:\n\n")
print ("Toplama işlemi için 1 düğmesine\n\nÇıkarma işlemi için 2 düğmesine\n\nÇarpma işlemi için 3 düğmesine\n\nBölme işlemi için 4 düğmesine basınız")
a = int(input("\n\nİşlem seçiniz:"))
if a == 1:
  b = int(input("Rakam giriniz:"))
  c = int(input("Rakam giriniz:"))
  print ("Cevap:" , b + c)
elif a == 2:
  b = int(input("Rakam giriniz:"))
  c = int(input("Rakam giriniz:"))
  print ("Cevap:" , b - c)
elif a == 3:
  b = int(input("Rakam giriniz:"))
  c = int(input("Rakam giriniz:"))
  print ("Cevap:" ,b * c)
elif a == 4:
  b = int(input("Rakam giriniz:"))
  c = int(input("Rakam giriniz:"))
  print ("Cevap:" ,b / c)
else:
  print ("HATA!, Yalnış işlem lütfen\nsadece 1, 2, 3, 4 düğmelerinden\nbirini seçiniz")