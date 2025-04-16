# BotZekkStoreTelegram

**BotZekkStoreTelegram** adalah bot Telegram yang dirancang untuk memudahkan pengguna dalam berinteraksi dengan layanan digital store melalui Telegram. Bot ini memungkinkan pengguna untuk membeli produk digital dengan mudah dan aman, langsung melalui aplikasi Telegram.

## 🚀 Fitur Utama
- **Pengelolaan Produk**: Menampilkan berbagai produk digital seperti followers Instagram, pulsa, dan banyak lagi.
- **Pembelian Mudah**: Pengguna dapat membeli produk langsung melalui percakapan di Telegram tanpa kerumitan.
- **Keamanan API Key**: Semua API key dan informasi sensitif disimpan dengan aman menggunakan file `.env` untuk menghindari kebocoran data.

## 🛠️ Instalasi

1. **Clone Repository**:
   Untuk mengunduh project ini ke komputer Anda, jalankan perintah berikut di terminal atau command prompt:
   ```bash
   git clone https://github.com/ZekkCode/BotZekkStoreTelegram.git
2. Instalasi Dependencies: Pastikan Anda sudah memiliki Python dan pip terinstal. Untuk menginstal semua dependensi yang diperlukan, jalankan perintah berikut:

'''pip install -r requirements.txt'''

3. Konfigurasi File .env: Buat file .env di direktori utama proyek dan tambahkan variabel berikut:

file env
'''TOKEN=your_telegram_bot_token'''
'''ADMIN_CHAT_ID=your_admin_chat_id'''
'''QRIS_FILE_ID=your_qris_file_id'''

Pastikan untuk mengganti nilai-nilai tersebut dengan data yang sesuai.

🔑 Menjaga Kerahasiaan API Key
Untuk menjaga keamanan API key dan informasi sensitif lainnya, gunakan file .env yang tidak akan di-upload ke GitHub. Anda dapat memanfaatkan pustaka python-dotenv untuk memuat variabel dari file .env ke dalam aplikasi Python Anda tanpa mengekspose data sensitif.

Langkah-langkah untuk menjaga keamanan API key:

Simpan API key dalam file .env yang tidak terpublikasi.

Gunakan pustaka python-dotenv untuk mengakses variabel dari file .env dalam kode Python Anda.

Pastikan file .env terdaftar dalam file .gitignore agar tidak ter-commit ke GitHub.

🖥️ Penggunaan
Setelah konfigurasi selesai, jalankan bot Telegram dengan perintah berikut:

bash
Salin
Edit
python main_bot.py
🌐 Media Sosial & Kontak
Untuk pembaruan lebih lanjut, pertanyaan, atau sekedar berinteraksi, berikut adalah akun media sosial saya:

Instagram: @Zekkymp

Github: @ZekkCode

LinkedIn: Zakaria Mujur Prasetyo

🤝 Contributing
Jika Anda ingin berkontribusi pada proyek ini, silakan buka issue atau buat pull request di repository ini. Kami akan sangat senang untuk menerima kontribusi Anda!

Dikembangkan oleh ZekkCode.
