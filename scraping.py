import requests
from bs4 import BeautifulSoup

# URL halaman web yang akan di-scrape
url = 'https://www.smkn7garut.sch.id'

# Menambahkan header User-Agent agar permintaan tampak berasal dari browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Mengirim permintaan GET ke URL
response = requests.get(url, headers=headers)

# Memastikan permintaan berhasil (status code 200)
if response.status_code == 200:
    # Mengambil konten halaman
    page_content = response.content
    
    # Mem-parsing konten HTML dengan BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Cek struktur halaman yang diambil
    print(soup.prettify())  # untuk debugging, bisa dilihat struktur HTML
    
    # Menemukan semua elemen yang berisi judul artikel
    articles = soup.find_all('a', class_='post-title')  # pastikan class sesuai
    
    # Menampilkan judul artikel
    for article in articles:
        title = article.get_text()
        print(title)
else:
    print(f"Permintaan gagal dengan status code {response.status_code}")
