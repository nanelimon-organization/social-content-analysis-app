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

