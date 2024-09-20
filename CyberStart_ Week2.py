import math

# 1. Adım: Noktaları Tanımla
# Burada 5 tane noktamız var, her biri (x, y) olarak tanımlanıyor.
points = [(1, 2), (4, 6), (5, 8), (9, 2), (3, 7)]  

# 2. Adım: Öklid Mesafesi Hesaplayan Fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1  
    x2, y2 = point2  
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 3. Adım: Tüm Mesafeleri Hesapla
distances = [] 
for i in range(len(points)):  
    for j in range(i + 1, len(points)):  
        distance = euclideanDistance(points[i], points[j])  # İki nokta arasındaki mesafeyi hesaplıyoruz
        distances.append(distance)  # Hesaplanan mesafeyi listeye ekliyoruz

# 4. Adım: Minimum Mesafeyi Bul
min_distance = min(distances)  # 'distances' listesindeki en küçük mesafeyi buluyoruz
print(f"Minimum Öklid mesafesi: {min_distance}")  # Sonucu yazdırıyoruz
