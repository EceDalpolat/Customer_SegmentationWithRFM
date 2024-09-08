# Customer_SegmentationWithRFM
#RFM Analizi Projesi
Bu proje, müşterilerin satın alma davranışlarını analiz etmek ve segmentlere ayırmak amacıyla RFM (Recency, Frequency, Monetary) analizini kullanır. RFM analizi, işletmelerin müşterilerini daha iyi tanımalarına ve daha etkili pazarlama stratejileri geliştirmelerine yardımcı olan güçlü bir tekniktir.

#Proje İçeriği
Bu projede, aşağıdaki adımlar izlenerek müşteri segmentasyonu gerçekleştirilmiştir:

1. Veri Hazırlığı
Müşteri alışveriş verileri birleştirilerek toplam alışveriş sayısı ve toplam harcama tutarı hesaplandı.
Online ve offline alışveriş verileri birleştirildi.
Son alışveriş tarihi ile analiz tarihi arasında geçen süre hesaplandı.
2. RFM Metriklerinin Hesaplanması
Müşterilerin son alışveriş tarihine göre Recency (Yakınlık), toplam alışveriş sayısına göre Frequency (Sıklık) ve toplam harcama tutarına göre Monetary (Parasal Değer) metrikleri oluşturuldu.
3. RFM Skorlarının Oluşturulması
Recency, Frequency ve Monetary değerleri kullanılarak her bir müşteri için 1 ile 5 arasında değişen skorlar belirlendi.
Bu skorlar birleştirilerek her müşteri için bir RFM Skoru oluşturuldu.
4. Müşteri Segmentasyonunun Oluşturulması
RFM skorlarına göre müşteriler belirli segmentlere ayrıldı. Bu segmentler arasında "Şampiyonlar", "Sadık Müşteriler", "Risk Altındakiler" gibi gruplar yer alır.
5. Sonuçların Analizi
Her bir segmentin Recency, Frequency ve Monetary ortalamaları analiz edildi.
Segmentlere göre müşterilerin davranışları ve işletmeye sağladıkları katkılar değerlendirildi.
#Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız olacak:
pandas
numpy
datetime

