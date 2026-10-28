# Yol Haritası

**Hedef:** Simülasyonda senaryo tabanlı AMR test düzeneği (scenario testbed).
Bir ayar dosyasından simülasyon ortamı üretilir, robot çalıştırılır, sonuç CI'da otomatik ölçülür.

Durumlar: Planlandı / Üzerinde çalışılıyor / Tamamlandı.
Kural: Bir adım, doğrulaması gerçekten geçmeden "Tamamlandı" yazılmaz.

## Şimdiye kadar (Tamamlandı)

- ROS 2 Humble + Gazebo Classic + TurtleBot3 simülasyonu kendi bilgisayarda çalışıyor
- Docker: image/container farkı, Dockerfile, `docker build` / `docker run`, temizlik komutları
- GitHub reposu, `.gitignore`, GitHub Actions CI (`docker build` + `colcon build`)
- CI'ın boş klasörü derlediğini (`0 packages`) log'dan fark etme ve `COPY src` ile düzeltme (`1 package`)
- C++ için: paket oluşturma (16), minimal node (20), CMake hatalarını okuma

## Proje 1: Simülasyonda mobil robot

Kurs dersleri sadece C++ olanlar. Python derslerini atlıyoruz.

| Adım | İş | Kurs dersi | CI/CD ve Docker kazanımı | Durum |
|------|----|-----------|--------------------------|-------|
| 1 | OOP biçiminde C++ node (`class MyNode : public rclcpp::Node`), kodu bakmadan yeniden yaz | 21 | - | Üzerinde çalışılıyor |
| 2 | Robotu `/cmd_vel` ile ileri süren C++ publisher (R1) | 38 | - | Planlandı |
| 3 | `/scan` veya `/odom` okuyan C++ subscriber | 39 | - | Planlandı |
| 4 | TF ağacı ve RViz (R2). Kurs dışı, birlikte, görsel olarak | - | - | Planlandı |
| 5 | Kodu kurs klasöründen repodaki `src/` altına taşı (`ament_cmake` C++ paketi) | - | Dockerfile'a gerekirse `build-essential`, CI iki paketi derler | Planlandı |
| 6 | Lint/test: `colcon test` adımını CI'a ekle (R4). İlk seferde kırmızı vermesi beklenen adım | - | CI'da test adımı, log okuma | Planlandı |
| 7 | Launch dosyası ve parametre: tek komutla her şey başlasın, hız parametreden gelsin | 76, 78, 80 (parametre); 87, 89, 90, 91, 92 (launch) | - | Planlandı |
| 8 | README ve 30-60 sn ekran videosu | - | README'ye CI rozeti | Planlandı |

Atlanacak dersler: 45, 46, 79, 81-84, 88, 93, 94 ve Bölüm 6, 7, 10 (şimdilik).

## Proje 2: Kendi yol planlayıcın ve Nav2

| İş | Not | CI/CD ve Docker kazanımı |
|----|-----|--------------------------|
| Izgara haritada A* planlayıcıyı C++ ile yaz | Yolu adım adım görselleştir | gtest ile birim testleri, `colcon test` CI'da |
| Nav2 ile aynı haritada karşılaştır | "Benimki neden farklı?" sorusu | - |
| Hedefe ulaşma ölçümü | Başardı mı, ne kadar sürdü | Docker katman önbelleği (build süresi) |
| Küçük deneme: simülasyon görsel pencere olmadan (headless) CI'da çalışır mı? | Proje 3 için risk kontrolü | Headless deneme |

Kurs: gerektiğinde Bölüm 6 (Service) ve Bölüm 7 (özel mesajlar). Alt başlıklarına bakıp seçeriz.

## Proje 3: Senaryo üretici ve otomatik test

| İş | CI/CD ve Docker kazanımı |
|----|--------------------------|
| `senaryo.yaml` oku, Gazebo dünyası üret | Üretilen dosyalar için test |
| Robotu çalıştır, sonucu ölç | Sonuç raporunu CI çıktısı (artifact) olarak yükle |
| Birden çok senaryoyu CI'da otomatik koştur | `docker compose`, image'ı GHCR'ye yayınla (CD) |
| Isteğe bağlı: çoklu robot | - |

## Dürüstlük notları

- CV'de yalnızca doğrulaması geçmiş olanı yaz, planlananı "yaptım" diye yazma.
- Simülasyonda çalışmak CV'de "simülasyonda" diye belirtilir.
- İlan şartları (örneğin Almanca) başvurmadan önce canlı ilanlardan kontrol edilir.
