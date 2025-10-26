# 🧠 VM Info Collector

Bu Python betiği, **vCenter veya ESXi sunucusuna bağlanarak** ortamda bulunan tüm sanal makinelerin (VM) sistem bilgilerini otomatik olarak listeler.

## 🚀 Özellikler

- SSL doğrulama hatalarını yok sayarak güvenli bağlantı sağlar  
- Tüm sanal makineleri tespit eder  
- Her VM için aşağıdaki bilgileri listeler:
  - Adı  
  - Güç durumu (Power State)  
  - İşletim sistemi (OS)  
  - VMware Tools durumu  
  - IP adresi  
  - Notlar (Annotation)

## 🧩 Gereksinimler

Aşağıdaki Python paketlerinin kurulu olması gerekir:

```bash
pip install pyvmomi
