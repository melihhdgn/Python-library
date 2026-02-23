#bu aslında çok güzel mesela bir uygulama yaptın ordada sana dövüz kurları,bitcoin fiyatları
#lazım sen gidip bir ExchangeRate-API gibi uyglardan bunları çekiyorsunyeni bir şey ayarlamıyorsun :D
#ama paralı çok trafikli uygulamalardan ücretsizler genelde test 1500 tane taelep felan bunuda anahtarla anlıyorlar



import requests  #bir sayffanın html kodlarına erişmek 
import json
result = requests.get("https:// melih.ffsda") #sayfanın htlm ulaşşır
result = result.text # o sayfadaki ne varsa yazdırır

result = json.loads(result) #eğerosayfa json şeklinde ise her bir parçaya ulaşmak için dick yaptık

for i in result:
    print(i["tittle"])  #sadece title bilgilerni söyler 

for i in result:
    if i["userID"] == 1:    #user ıd 1 olan ve sadece title olanları yazdırır gibi 
        print(i["tittle"])    

