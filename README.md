# script 

### Revdk3-r3.sh
**ReVdK3-r3.sh - "You input a wireless interface that doesn't exist!"  Hatasının Çözümü !**
wireless kartını monitör moda aldığınızda wlan0mon olarak isimlendirilecektir. Bu script önceki sürümlerde(bt, kali 1.x) kullanılan mon1, mon2 vs. gibi isimler referans alınarak kodlandı bu nedenle kali 2.x sürümlerinde wlan0mon gibi isimlendirme yapıldığından yukarıdaki hatayı verecektir.
Bu script wlan0mon için tekrar düzenlenilmiştir sorunsuzca kullanabilirsiniz.  

### xor.py
Xor mantıksal operatörü kullanılarak yapılan şifrelemeyi binary seviyede görebilmek için yazdığım ufak bir tooldur.  

### newsBot.py
Birkaç haber sitesindeki manşet haberleri çekip listeyen bir bot. Haber detayları için ise google'ın shorting url api sini kullandım. Geliştirilmeye müsait duruyor.


### merge.py
Youtube veya başka video paylaşım sitelerinde indirilen DASH(ses veya görüntüsü eksik olan dosya) türündeki ses ve görüntülerinin birleştirilmesi için yazılmış küçük bir scripttir. İndirilen görüntü/ses'e ait diğer parçası olan görüntü/ses aynı klasöre atılıp bu script çalıştırılır ise görüntünün ses dosyasını sorunsuz bir şekilde birleştirecektir.
**Not:**Scriptin çalışması için ffmpeg'in yüklü olması gerekmektedir.
