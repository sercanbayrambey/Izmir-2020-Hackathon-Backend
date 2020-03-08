# Izmir 2020 Hackathon Backend APIs





## Built With
* [Python](https://www.python.org/) 
* [Flask](https://palletsprojects.com/p/flask/) - The web framework used



## Authors

* **Sercan Bayrambey** - [Github](https://github.com/sercanbayrambeyy)
* **Gökay Meriç Şişik** - [Github](https://github.com/tassattir)


## Servisler
`Path: /apis/`
`Method: POST`

 - **Duration**<br>
 -*İki istasyon arasında geçen süreyi verir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| st1  |  Başlangıç istasyonu id |
| st2  |  Bitiş istasyonu id  |

------------


 - **GetBAstation**<br>
	-*Bir istasyondan bir önceki ve bir sonraki istasyonu verir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| stno  |  İstasyon id  |
------------


 - **StationData**<br>
	-*O istasyonla ilgili tüm verileri verir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| stno  |  İstasyon id  |
------------


 - **TotalPassengers**<br>
	-*Belirtilen saat aralığında o istasyondaki toplam yolcuları verir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| stno  |  İstasyon id  |
| time  |  Saat (HH)  |
| time2 (optional)  |  Saat (HH)  |
------------


 - **GetNStations**<br>
	-*Verilen enlem ve boylama göre en yakın 3 istasyonu verir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| origin  |  Enlem boylam (e,b)  |
------------

 - **compareTrans**<br>
	-*Başlangıç ve bitiş noktasına göre metro ile mi araba ile mi daha kısada varılacağını gösterir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| origin  |  Başlangıç noktası için enlem boylam (e,b)  |
| destination  |  Bitiş noktası için enlem boylam (e,b)  |
------------

 - **DData**<br>
	-*Bir noktadan bir noktaya giderken yürüyerek ve arabayla kaç dakika süreceğini verir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| origin  |  Başlangıç noktası için enlem boylam (e,b)  |
| destination  |  Bitiş noktası için enlem boylam (e,b)  |
| mode  |  Yürüme veya sürme modu (walking,driving)  |
------------

 - **GetStationLocation**<br>
	-*Verilen istasyonun enlem ve boylamını verir.*

| Parametre  |  Açıklama |
| ------------ | ------------ |
| stno  |  İstasyon id  |

