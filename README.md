# Oyun Karakteri Motoru (Game Character Engine) - EBLG443 Dönem Projesi

## 1. Proje Tanımı
Bu proje, bir rol yapma oyunundaki (RPG) karakter yaratımı, dinamik saldırı stratejileri, zırh/büyü güçlendirmeleri ve durum bildirim mekanizmalarını Nesne Yönelimli Tasarım Kalıpları (GoF) kullanarak çözen modüler bir oyun motorudur.

## 2. Kullanılan Tasarım Kalıpları
- **Yaratımsal (Creational):** Factory Method (Karakter üretimi)
- **Yapısal (Structural):** Decorator (Karaktere dinamik zırh/büyü aurası ekleme)
- **Davranışsal (Behavioral):** Strategy (Silah ve saldırı davranışı değişimi)
- **Davranışsal (Behavioral):** Observer (Can ve durum güncellemelerini UI/Log bileşenlerine bildirme)

## 3. Kurulum ve Çalıştırma
Gereksinim: Python 3.10+
```bash
python src/main.py