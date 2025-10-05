from bs4 import BeautifulSoup

# html4 = """<div>div1</div>
# <div>div2</div>
# <div>div3</div>
# <div>div4</div>
# <div>div5</div>
# <div>div6</div>
# <div>div7</div>
# <div>div8</div>
# <div>div9</div>
# <div>div10</div>"""

# 1. Inisialisasi BeautifulSoup
soup = BeautifulSoup(html4, 'html.parser')

# 2. Mencari semua tag <div> dan menyimpannya ke dalam list
all_divs = soup.find_all('div')

print("--- Hasil Output ---")

# Mengakses div ke-2 (Indeks 1)
print(all_divs[1])

# Mengakses div ke-4 (Indeks 3)
print(all_divs[3])

# Mengakses div ke-6 (Indeks 5)
print(all_divs[5])

# Mengakses div ke-8 (Indeks 7)
print(all_divs[7])

# Mengakses div ke-10 (Indeks 9)
print(all_divs[9])

for index, div in enumerate(soup.findAll("div)")):
    if (index + 1) % 2 == 0:  # Cek apakah indeks ganjil (karena indeks mulai dari 0)
        print(div)
