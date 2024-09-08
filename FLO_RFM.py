###############################################################
# GÖREVLER
###############################################################
import datetime as dt
import pandas as pd
pd.set_option('display.max_columns',None)
#pd.set_option('display.max_rows',None)
pd.set_option('display.float_format',lambda x:'%.3f'%x)
# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama

           # 1. flo_data_20K.csv verisini okuyunuz.
df_=pd.read_csv("flo_data_20k.csv")
df=df_.copy()
           # 2. Veri setinde
                     # a. İlk 10 gözlem,
df.head(10)
                     # b. Değişken isimleri,
df.columns
                     # c. Betimsel istatistik,
df.describe().T
                     # d. Boş değer,
df.isnull().sum()

                     # e. Değişken tipleri, incelemesi yapınız.
df.dtypes
df.dtypes.value_counts()
           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
df["order_num_total"]=df["order_num_total_ever_online"]+df["order_num_total_ever_offline"]
df["customer_value_total"]=df["customer_value_total_ever_offline"]+df["customer_value_total_ever_online"]
df["total_price"]=df["customer_value_total"]*df["order_num_total"]
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
date_columns = ['first_order_date', 'last_order_date', 'last_order_date_online', 'last_order_date_offline']
df[date_columns]=df[date_columns].apply(pd.to_datetime)
df.dtypes
           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
df.groupby("order_channel").agg(total_customers=('master_id', 'nunique'),  # Eşsiz müşteri sayısı
    avg_order_num=('order_num_total', 'mean'),  # Ortalama sipariş sayısı
    avg_spending=('customer_value_total', 'mean')).reset_index()  # Ortalama harcama
           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
top10_customer_value=df[["master_id","customer_value_total"]].sort_values(by="customer_value_total",ascending=False).head(10)
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
top10_order_value = df[["master_id", "order_num_total"]].sort_values(by="order_num_total",
                                                                             ascending=False).head(10)
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def data_preparation(df):
    """
        Bu fonksiyon, müşteri verisini alarak gerekli ön hazırlıkları yapar ve
        veriyi analiz için hazır hale getirir.

        Args:
            df (pd.DataFrame): Müşteri verisinin olduğu DataFrame

        Returns:
            pd.DataFrame: Hazırlık işlemleri tamamlanmış DataFrame
        """
    import pandas as pd

    # 1. Değişkenlerin adlarını ve ilk gözlemleri yazdır.
    print("İlk 10 gözlem:")
    print(df.head(10))

    print("\nDeğişken İsimleri:")
    print(df.columns)

    print("\nBetimsel İstatistikler:")
    print(df.describe().T)

    print("\nBoş Değer Sayısı:")
    print(df.isnull().sum())

    print("\nDeğişken Tipleri:")
    print(df.dtypes)

    # 2. Toplam alışveriş sayısı ve harcama için yeni değişkenler oluştur.
    df["order_num_total"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
    df["customer_value_total"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
    df["total_price"] = df["customer_value_total"] * df["order_num_total"]
    # 3. Tarih ifade eden değişkenlerin tipini date'e çevir.
    date_columns = ['first_order_date', 'last_order_date', 'last_order_date_online', 'last_order_date_offline']
    df[date_columns] = df[date_columns].apply(pd.to_datetime)

    # 4. Alışveriş kanallarındaki müşteri sayısının, ortalama sipariş sayısının ve ortalama harcamaların dağılımı.
    channel_stats = df.groupby("order_channel").agg(
        total_customers=('master_id', 'nunique'),  # Eşsiz müşteri sayısı
        avg_order_num=('order_num_total', 'mean'),  # Ortalama sipariş sayısı
        avg_spending=('customer_value_total', 'mean')  # Ortalama harcama
    ).reset_index()

    print("\nAlışveriş Kanallarına Göre Dağılım:")
    print(channel_stats)

    # 5. En fazla kazancı getiren ilk 10 müşteriyi sıralama.
    top10_customer_value = df[["master_id", "customer_value_total"]].sort_values(by="customer_value_total",
                                                                                 ascending=False).head(10)
    print("\nEn Fazla Kazanç Getiren İlk 10 Müşteri:")
    print(top10_customer_value)

    # 6. En fazla siparişi veren ilk 10 müşteriyi sıralama.
    top10_order_value = df[["master_id", "order_num_total"]].sort_values(by="order_num_total", ascending=False).head(10)
    print("\nEn Fazla Sipariş Veren İlk 10 Müşteri:")
    print(top10_order_value)

    return df
df=df_.copy()
df = data_preparation(df)


# GÖREV 2: RFM Metriklerinin Hesaplanması

df.head(10)
df["last_order_date"].max()
today_date=dt.datetime(2021,6,1)
type(today_date)

rfm=df.groupby('master_id').agg({'last_order_date':lambda last_order_date:(today_date-last_order_date.max()).days,
                                 'customer_value_total':lambda customer_value_total:customer_value_total,
                                 'total_price':lambda total_price:total_price.sum()})
rfm.head(10)
rfm.columns=["recency","frequency","monetary"]
rfm.describe().T
rfm=rfm[rfm["monetary"]>0]
rfm.shape
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması

rfm["recency_score"]=pd.qcut(rfm["recency"],5,labels=[5,4,3,2,1])
rfm["monetary_score"]=pd.qcut(rfm["monetary"],5,labels=[1,2,3,4,5])
rfm["frequecny_score"]=pd.qcut(rfm["frequency"].rank(method="first"),5,labels=[1,2,3,4,5])
rfm.head()
rfm["RFM_SCORE"]=(rfm["recency_score"].astype(str)+
                  rfm["frequecny_score"].astype(str))
rfm.describe().T
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
#REGEX
seg_map={
    r'[1-2][1-2]':'hibernating',
    r'[1-2][3-4]':'at-risk',
    r'[1-2]5':'cant_loose',
    r'3[1-2]':'about_to_sleep',
    r'33':'need_attention',
    r'[3-4][4-5]':'loyal_customer',
    r'41':'promising',
    r'51':'neew_customer',
    r'[4-5][2-3]':'potential_loyalist',
    r'5[4-5]':'champions',
}

rfm["segment"]=rfm["RFM_SCORE"].replace(seg_map,regex=True)
rfm.head()
# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
rfm[["segment","recency","frequency","monetary"]].groupby("segment").agg(["mean","count"])
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşter8ileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
df.head()
target_customers_case1 = df[
    (df['segment'].isin([['champions', 'loyal_customers']])) &
    (df['monetary'] > 250) &
    (df['interested_in_categories_12'].str.contains('KADIN'))]
target_case1_ids = target_customers_case1['master_id']
target_case1_ids.to_csv("yeni_marka_hedef_musteri_id.csv", index=False)
                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.
target_customers_case2 = df[
    (df['segment'].isin(['cant_loose', 'hibernating', 'new_customers'])) &
    (df['interested_in_categories_12'].str.contains('ERKEK|COCUK'))
]
target_case2_ids = target_customers_case2['master_id']
target_case2_ids.to_csv("indirim_hedef_musteri_ids.csv", index=False)

rfm.to_csv("rfm.csv")
# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

def createe_rfm(dataframe, csv=False):
    #Veriyi hazırlama
    df["order_num_total"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
    df["customer_value_total"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
    df["total_price"] = df["customer_value_total"] * df["order_num_total"]
    date_columns = ['first_order_date', 'last_order_date', 'last_order_date_online', 'last_order_date_offline']
    ##rfm skorları
    df[date_columns] = df[date_columns].apply(pd.to_datetime)
    df["last_order_date"].max()
    today_date = dt.datetime(2021, 6, 1)
    type(today_date)
    rfm = df.groupby('master_id').agg(
        {'last_order_date': lambda last_order_date: (today_date - last_order_date.max()).days,
         'customer_value_total': lambda customer_value_total: customer_value_total,
         'total_price': lambda total_price: total_price.sum()})
    rfm.head(10)
    rfm.columns = ["recency", "frequency", "monetary"]
    rfm.describe().T
    rfm = rfm[rfm["monetary"] > 0]
    ##segmentler
    rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
    rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])
    rfm["frequecny_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm.head()
    rfm["RFM_SCORE"] = (rfm["recency_score"].astype(str) +
                        rfm["frequecny_score"].astype(str))
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at-risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customer',
        r'41': 'promising',
        r'51': 'neew_customer',
        r'[4-5][2-3]': 'potential_loyalist',
        r'5[4-5]': 'champions',
    }

    rfm["segment"] = rfm["RFM_SCORE"].replace(seg_map, regex=True)
    ##rfm=rfm["recency", "frequency", "monetary","segment"]
    rfm.index=rfm.index.astype(int)
    if csv:
        rfm.to_csv("rfm.csv")
    return rfm

df=df_.copy()
rfm_new=createe_rfm(df,csv=True)
rfm_new.head()