"""import json ifadesi, Python'da JSON (JavaScript Object Notation) verilerini okumak (parse etmek) ve yazmak (serialize etmek) için
kullanılan yerleşik (built-in) bir modülü programına dahil eder. 


person = {"name":"Ali", "languages":["python","C#"]}
result = person["name"]
result = person["languages"],
result = person["languages"][0]
print(result)  bu kısım dict yazımı örneği aşşağı json

dict yapısını json modulunu cevirmek için string yapıya çevirmek lazım yani "" eklemek yerleri başına sonuna
'{"name":"Ali", "languages":["python","C#"]}' gibi böyle olunca sult = person["name"] bunlar çalışmaz. Yani jsonu dict cevirmek lazım


import json

person_str = '{"name":"Ali", "languages":["python","C#"]}'
result = json.loads(person_str)
result = result["name"]  #bu sefer ali çıkaacaktır çünkü dict çevirdik
print(result) 

with open("melih.json") as f: #("melih.json", "w") bu şekil yazma ekleme yapılabilir 
    data = json.load(f)
    print(data)    #json dosya okuma

json.dumps(melih_dict) #dict i jsona(strye) çevirme"""

#json.dumps(obj)  python formatındakini json formatına çevirir json.dump(obj, file) bir dosyaya yazaar buda 
#json.loads(json_string) jsonu python(dict) çevirir  
#json.load(file) dosyadaki json veririsini python çevirir 
import json

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age
        }

    @staticmethod
    def from_dict(data):
        return User(data["name"], data["email"], data["age"])


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.users = [User.from_dict(user_dict) for user_dict in data]

    def print_users(self):
        for user in self.users:
            print(f"{user.name} | {user.email} | {user.age}")


# Kullanım
repo = UserRepository()
repo.add_user(User("Ahmet", "ahmet@example.com", 25))
repo.add_user(User("Ayşe", "ayse@example.com", 30))

repo.save_to_file("users.json")

print("✅ Dosyaya kaydedildi.")

# Yeni repository oluşturup dosyadan okuyalım
new_repo = UserRepository()
new_repo.load_from_file("users.json")

print("\n📄 Dosyadan okunan kullanıcılar:")
new_repo.print_users()


#çok çok önemli bir not pythondan çıkarken json tabanlı çıkması lazım pythonda işlememk için dict yapısı laazım 

#json.loads()   # string → dict
#json.dumps()   # dict → string