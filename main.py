# rembg kütüphanesinden 'remove' fonksiyonunu içe aktarıyoruz. Bu fonksiyon, arka planı kaldırmak için kullanılacak.
from rembg import remove

# Giriş ve çıkış dosya yollarını belirliyoruz.
input_path = "indir.jpeg"
output_path = "output.png"

# Giriş dosyasını binary ('rb') modda açıyoruz.
with open(input_path, 'rb') as i:
    # Çıkış dosyasını binary ('wb') modda açıyoruz.
    with open(output_path, 'wb') as o:
        # Giriş dosyasının içeriğini okuyoruz.
        input_file = i.read()

        # 'remove' fonksiyonunu kullanarak arka planı kaldırıyoruz.
        output_file = remove(input_file)

        # Çıkış dosyasına arka planı kaldırılmış görüntüyü yazıyoruz.
        o.write(output_file)
