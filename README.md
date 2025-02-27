# AI SQL QUERY GENERATOR
## Deskripsi Proyek
Proyek ini memungkinkan AI untuk mengubah pertanyaan pengguna menjadi SQL query dan memberikan jawaban berdasarkan hasil dari database Titanic. Dengan menggunakan model bahasa besar dan database MySQL, AI dapat menjawab pertanyaan berdasarkan data yang ada di dalam tabel passengers.

## Fitur Utama
- **Konversi Pertanyaan ke SQL**: AI mengubah pertanyaan dalam bahasa alami menjadi SQL query.
- **Eksekusi Query ke Database**: Query dijalankan di database MySQL.
- **Jawaban AI Berdasarkan Data**: AI menjawab berdasarkan hasil query yang dieksekusi.
- **Dukungan Streaming**: Jawaban diberikan secara real-time.

## Instalasi
1. **Clone Repository**
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```
2. **Buat Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows
```
3. **Instal Dependensi**
```bash
pip install -r requirements.txt
```
4. **Buat File .env dan isi dengan kredensial database MySQL Anda:**
```bash
USER="your_username"
PASSWORD="your_password"
HOST="your_host"
DATABASE="your_database"
BASE_URL="your_openai_base_url"
API_KEY="your_api_key"
MODEL="your_model_name"
```
5. **Jalankan Program**
```bash
python ai_sql_chatbot.py
```

## Penggunaan
- **Pastikan database Titanic dengan tabel passengers sudah tersedia.**
- **Jalankan program dan masukkan pertanyaan terkait data di dalam database.**
- **AI akan menghasilkan SQL query, menjalankan query tersebut, dan memberikan jawaban berdasarkan hasilnya.**

## Struktur Kode
```
|-- ai_sql_chatbot.py  # Kode utama aplikasi SQL AI
|-- requirements.txt  # Daftar dependensi
|-- README.md  # Dokumentasi proyek
|-- .env  # File konfigurasi kredensial database
```

## Pengembang
**Nama:** Abulkhair Rizvan Yahya  
**Email:** [aburnyh.yahya@gmail.com](mailto:aburnyh.yahya@gmail.com)  
**LinkedIn:** [linkedin.com/in/arizvanyahya](https://linkedin.com/in/arizvanyahya)  
