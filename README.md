# Sosyal İçerik Analizi Uygulaması

Bu, bir konu (hashtag) hakkındaki sosyal medya tartışmalarını anında görüntüleyen ve bu tartışmaların çeşitli kategorilerde hakaret içerip içermediğini belirleyen ve eğer içeriyorsa, metnin hangi kelimelerinin o hakaret kategorisinde değerlendirildiğini gösteren bir uygulamadır.

## Kullanılan Teknolojiler

Ana teknolojiler:

- [PostgreSQL](https://www.postgresql.org/) - RDBMS veritabanı
- [Python](https://docs.python.org/3.10/) - Python sürümü: 3.10 
- [SQLAlchemy](https://docs.sqlalchemy.org/) - SQLAlchemy sürümü: 2.0
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Bootstrap sürümü: 5.0


## Gereksinimler

### Ortam

Lütfen Python sürümünüzü `3.10` olarak ayarlayın:

```bash
python --version
```

- Virtualenv kurulumu:
```bash
pip install virtualenv
```
- Virtualenv oluşturma:
```bash
virtualenv venv
```
- Virtualenv'i aktif hale getirme:
```bash
source venv/bin/activate
```
- Kütüphanelerin kurulumu:
```bash
pip install -r requirements.txt
```

### Konfigürasyon

`.env` dosyanızı oluşturun.
```bash
cd <project-directory>

touch .env dosyasına ortam değişkenleri ekleyin.
```
- Add environment variables into `.env` file
```bash
* HASHTAG=#hashtag
* DATABASE=postgresql
* HOST=localhost
* USERNAME=postgres
* PASSWORD=postgres
* PORT=5432
```

## Uygulamayı Çalıştırma

```bash
python app.py
```


![WhatsApp Image 2023-04-05 at 11 45 28 PM](https://user-images.githubusercontent.com/78956836/230224757-d6bf76fc-7297-478f-af2a-6b4b1d504363.jpeg)



Uygulama, Teknofest 2023 Doğal Dil İşleme yarışması kapsamında geliştirilen, Türkçe metinler üzerinde derinlemesine analizler gerçekleştirmenize olanak tanıyan, kullanıcı dostu ve güçlü bir sosyal medya analitikleri platformudur. 

Uygulama, popüler sosyal medya platformu Twitter üzerinden belirli bir hashtag ile ilişkilendirilmiş tweet'leri toplama, analiz etme ve anlık gösterim yeteneklerine sahiptir. Bu sayede, kullanıcılar sosyal medya trendlerini, kullanıcı davranışlarını ve içerik türlerini daha iyi anlayabilir ve etkili stratejiler geliştirebilirler.

Uygulama için planlanan başlıca analitik modüller şunlardır:

İstenmeyen İçerik Analizi: Bu modül, kötü anlam taşıyan veya saldırgan içerikleri tespit ederek, sosyal medya yöneticilerine iletişim stratejilerini optimize etme imkanı sağlar. Kullanılan model, beş farklı kategoriye ayrıştırarak Türkçe metinleri sınıflandırmak için eğitilmiştir. Bu kategoriler INSULT (HAKARET), OTHER (DİĞER), PROFANITY (KÜFÜR), RACIST (IRKÇI) ve SEXIST (CİNSİYETÇİ) olarak tanımlanmıştır. Modelin performansı, precision, recall ve F1-score gibi metrikler kullanılarak değerlendirilmiştir.

" is_offensive " fonksiyonu sayesinde, anlık olarak etiketlenmiş içeriklerin hangi kategoriye ait olduğunu belirler ve beş farklı etiket sunar. Bu modülde, gelişmiş doğal dil işleme teknikleri ve BERT tabanlı modeller kullanılır.

Rakip Analizi: Kullanıcılar için rakip markaların ve kişilerin sosyal medya performansını ve etkileşimlerini analiz eder. Bu sayede, sektördeki duruşlarını güçlendirmelerine destek olur. Rakip analizi, gelişmiş metrikler ve sosyal medya analitiği araçları kullanarak gerçekleştirilir.

Kullanıcı Duruş Analizi: Kullanıcıların sosyal medyadaki etkileşimlerini ve duyarlılıklarını değerlendirir. Bu analizlerle, daha hedef odaklı iletişim stratejileri geliştirmelerine katkıda bulunur. Duruş analizi için duygu analizi ve metin sınıflandırma algoritmaları kullanılır.

Takip Analizi: Kullanıcıların takip ettikleri kişiler ve etiketlerin analizini gerçekleştirir. Bu sayede, sosyal medya ağlarını genişletmelerine ve etkileşimlerini artırmalarına yardımcı olur. Takip analizi, kullanıcı etkileşimi ve sosyal ağ analitiği yöntemleri kullanarak gerçekleştirilir.

Yarışma süresinin kısıtlı olması nedeniyle, bu modüllerin tamamlanması henüz gerçekleştirilememiştir. Ancak, projenin hedefleri doğrultusunda geliştirme süreci devam etmektedir. Proje süresince Python programlama dili, TensorFlow ve PyTorch kütüphaneleri kullanılmaktadır. Ayrıca, analizlerin görselleştirilmesi için Matplotlib ve Seaborn gibi popüler kütüphanelerden faydalanılmıştır.

Uygulama, BERT tabanlı dönüşüm modelleri kullanarak Türkçe metinlerin analizini sağlar ve doğru, güvenilir analizler elde etmek için en güncel ve etkili doğal dil işleme tekniklerine dayalı algoritmalar kullanır. Sunduğumuz tasarım kapsamında İstenmeyen İçerik Analizi bölümü gerçekleştirilmiştir. Ek olarak, Rakip Analizi, Kullanıcı Duruş Analizi ve Takip Analizi gibi çeşitli analitik modüller yer almaktadır. Hedefimiz, bu alanların altında kapsamlı ve güvenilir analizler sağlamak amacıyla BERT tabanlı modellerin yeniden oluşturulması, eğitilmesi ve uygun mikro hizmetlerin geliştirilmesidir.

