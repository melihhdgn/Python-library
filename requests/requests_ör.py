import requests
import json
#https://www.exchangerate-api.com/ bu satfadan apikey url yi aldık 
api_key = "069308526f15df61c2a65082"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/" #hangi döviz turunden çeviri var ise sonuna eklenir sonucta ekledik

bozulan_doviz = input("Bozulan döviz türü: ") #USD, EURO
alınan_döviz = input("Alınan döviz türü:") #TRY
miktar = float(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz:"))
sonuc = requests.get(api_url + bozulan_doviz) 
result = json.loads(sonuc.text) #response yani yanıtı text çevirirr texti ise altta jsona çeviririz

print("1 {0} = {1} {2}".format(bozulan_doviz,result["conversion_rates"][alınan_döviz], alınan_döviz)) #format yöntemi unutma 
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,result["conversion_rates"][alınan_döviz]*miktar,alınan_döviz))

#doviz uygulaması 