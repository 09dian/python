import requests
from bs4 import BeautifulSoup

# URL halaman web yang akan di-scrape
url = 'https://www.smkn7garut.sch.id'

# Mengirim permintaan GET ke URL
response = requests.get(url)

# Memastikan permintaan berhasil (status code 200)
if response.status_code == 200:
    # Mengambil konten halaman
    page_content = response.content
    
    # Mem-parsing konten HTML dengan BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Menemukan semua elemen yang berisi judul artikel
    articles = soup.find_all('a', class_='post-title')
    
    # Menampilkan judul artikel
    for article in articles:
        title = article.get_text()
        print(title)
else:
    print(f"Permintaan gagal dengan status code {response.status_code}")
