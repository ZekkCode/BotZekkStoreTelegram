from dotenv import load_dotenv
import os
import telebot
import requests

# Memuat file .env
load_dotenv()

# GANTI BAGIAN INI SESUAI PUNYAMU
TOKEN = os.getenv('TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')
QRIS_FILE_ID = os.getenv('QRIS_FILE_ID')

bot = telebot.TeleBot(TOKEN)

# Tambahkan file_id gambar QRIS di sini
QRIS_FILE_ID = "AgACAgUAAxkBAAMuZ_K2oHRohyJclKIpBMqDdtRIFPQAAs3GMRt41JlXw0KkP2hQgXQBAAMCAAN5AAM2BA"  # Ganti dengan file_id gambar QRIS

# Simulasi list produk
produk_list = {
    "followers_1k": {
        "nama": "Followers Instagram 1K",
        "harga": 10000,
        "deskripsi": "1.000 followers real aktif"
    },
    "pulsa_20k": {
        "nama": "Pulsa Telkomsel 20K",
        "harga": 21000,
        "deskripsi": "Pengisian langsung ke nomor"
    }
}
# Tambahkan counter untuk menghitung jumlah pesanan
order_counter = 0
        
user_order = {}

# /start
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Pastikan teks tombol sesuai dengan handler
    markup.row("🛒 LIHAT PRODUK", "HUBUNGI ADMIN", "TENTANG ZEKKSTORE")
    bot.send_message(
        message.chat.id,
        "Selamat datang di *ZekkStore!*\n\n"
        "Klik tombol di bawah untuk melihat produk 👇",
        parse_mode="Markdown",
        reply_markup=markup
    )

# Bantuan
@bot.message_handler(func=lambda msg: msg.text == "HUBUNGI ADMIN")
def bantuan(message):
    bot.send_message(
        message.chat.id,
        "📞 *HUBUNGI ADMIN*\n\n"
        "Untuk bantuan, Anda dapat menghubungi kami melalui:\n"
        "🔹 WhatsApp: wa.me/62881081772005\n"
        "🔹 Telegram: @zekksparow\n"
        "🔹 Instagram: [@zekkstore](https://instagram.com/zekkstore)\n\n"
        "Kami siap membantu Anda!",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda msg: msg.text == "TENTANG ZEKKSTORE")
def show_contact(message):
    bot.send_message(
        message.chat.id,
        "🏪 *Tentang ZekkStore*\n\n"
        "ZekkStore adalah platform terpercaya untuk memenuhi kebutuhan digital Anda. Kami menyediakan:\n"
        "🔹 Followers Instagram, Tiktok, Facebook\n"
        "🔹 Pulsa dan Paket Data dengan Harga Terjangkau\n"
        "🔹 Berbagai Layanan Digital Lainnya\n\n"
        "*Kami berkomitmen untuk memberikan layanan terbaik dan terpercaya kepada pelanggan.*\n"
        "Hubungi kami untuk informasi lebih lanjut!\n"
        "🔹 WhatsApp: [wa.me/62881081772005](https://wa.me/62881081772005)\n"
        "🔹 Telegram: [@zekksparow](https://t.me/zekksparow)\n"
        "🔹 Instagram: [@zekkstore](https://instagram.com/zekkstore)\n"
        "*Kami siap membantu Anda!*",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda msg: msg.text == "🛒 LIHAT PRODUK")
def show_produk(message):
    for kode, data in produk_list.items():
        text = (
            f"📦 *{data['nama']}*\n"
            f"📝 {data['deskripsi']}\n"
            f"💸 Harga: Rp{data['harga']}"
        )
        markup = telebot.types.InlineKeyboardMarkup()
        tombol_beli = telebot.types.InlineKeyboardButton(text="🛍 Beli Sekarang", callback_data=f"beli_{kode}")
        tombol_batal = telebot.types.InlineKeyboardButton(text="❌ Batal", callback_data="batal")
        markup.add(tombol_beli, tombol_batal)

        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# Tangani Tombol Inline
@bot.callback_query_handler(func=lambda call: call.data.startswith("beli_") or call.data == "batal")
def handle_callback(call):
    chat_id = call.message.chat.id

    if call.data.startswith("beli_"):
        kode = call.data.replace("beli_", "")
        if kode in produk_list:
            user_order[chat_id] = {"produk": kode}
            bot.send_message(chat_id, f"📝 Masukkan nomor tujuan untuk *{produk_list[kode]['nama']}*:", parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "❌ Produk tidak ditemukan.")

    elif call.data == "batal":
        if chat_id in user_order:
            user_order.pop(chat_id)
        bot.send_message(chat_id, "🚫 Pemesanan dibatalkan. Ketik /start untuk kembali ke menu.")

# Input nomor tujuan
@bot.message_handler(func=lambda msg: msg.chat.id in user_order and 'nomor' not in user_order[msg.chat.id])
def input_nomor(msg):
    # Debugging: Log input yang diterima
    print(f"Pesan diterima dari {msg.chat.id}: {msg.text}")

    # Validasi input nomor tujuan
    if not msg.text.isdigit() or len(msg.text) < 8:  # Contoh validasi: hanya angka dan minimal 8 digit
        bot.send_message(msg.chat.id, "❌ Nomor tujuan tidak valid. Silakan masukkan nomor yang benar.")
        return

    # Simpan nomor tujuan ke user_order
    user_order[msg.chat.id]['nomor'] = msg.text
    kode = user_order[msg.chat.id]['produk']
    data = produk_list[kode]

    # Debugging: Log data yang disimpan
    print(f"Data user_order untuk {msg.chat.id}: {user_order[msg.chat.id]}")

    summary = (
        f"📦 *{data['nama']}*\n"
        f"📞 Tujuan: {msg.text}\n"
        f"💰 Harga: Rp{data['harga']}\n\n"
        "Silakan transfer ke:\n"
        "🔰 *QRIS / DANA / GOPAY: [Lihat gambar QR di bawah]*\n\n"
        "📌 Setelah transfer, kirim *bukti transfer berupa foto*, lalu *salin ulang pesan ini untuk verifikasi!*"
    )

    user_order[msg.chat.id]['summary'] = summary

    # Kirim gambar QRIS
    bot.send_photo(msg.chat.id, QRIS_FILE_ID, caption=summary, parse_mode="Markdown")
    print(f"Gambar QRIS dikirim ke {msg.chat.id}")

# Terima bukti transfer (foto)
@bot.message_handler(content_types=['photo'])
def bukti_transfer(msg):
    bot.send_message(msg.chat.id, "📩 Bukti transfer diterima! Sekarang, *kirim ulang pesan terakhir dari bot* yang berisi detail order kamu.", parse_mode="Markdown")

# Verifikasi pesan invoice
@bot.message_handler(func=lambda msg: msg.chat.id in user_order and 'summary' in user_order[msg.chat.id])
def cek_summary(msg):
    expected = user_order[msg.chat.id]['summary']
    if msg.text.strip() == expected.strip():
        bot.send_message(msg.chat.id, "✅ Verifikasi cocok. Pesanan Anda sedang diproses...")

        username = msg.from_user.username or "(tanpa username)"
        kirim_ke_admin(username, user_order[msg.chat.id], msg.photo[-1].file_id)
        user_order.pop(msg.chat.id)
    else:
        bot.send_message(msg.chat.id, "❌ Pesan tidak cocok. Silakan salin ulang invoice yang benar.")

# Kirim notifikasi ke admin dengan gambar invoice
def kirim_ke_admin(username, order, photo_file_id):
    global order_counter
    order_counter += 1  # Tambahkan 1 setiap ada pesanan baru

    kode = order['produk']
    data = produk_list[kode]
    nomor = order['nomor']

    # Pesan teks untuk admin
    text = (
        f"📥 *PESANAN BARU #{order_counter}! DARI BOT*\n\n"  # Tambahkan nomor pesanan
        f"👤 User: @{username}\n"
        f"📦 Produk: {data['nama']}\n"
        f"📞 Tujuan: {nomor}\n"
        f"💰 Harga: Rp{data['harga']}\n\n"
        "📸 Bukti transfer terlampir di bawah!"
    )

    # Kirim pesan teks ke admin
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': ADMIN_CHAT_ID, 'text': text, 'parse_mode': 'Markdown'})

    # Kirim gambar (bukti transfer/invoice) ke admin
    url_photo = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    requests.post(url_photo, data={'chat_id': ADMIN_CHAT_ID, 'photo': photo_file_id})

# Run bot
print("Bot is running...")
bot.infinity_polling()



