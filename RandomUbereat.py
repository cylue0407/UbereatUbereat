import random
import string

dishType = ["中式","西式","韓式","日式","泰式","越式"]
chineseDish = ["炒飯","燒臘飯","永和豆漿","麵","滷味","臭豆腐","鐵板燒","粥","串燒/鹽酥雞","餃子","鹹水雞"]
westernDish = ["義大利麵","炸雞","披薩","健康餐","速食"]
koreanDish = ["炸雞","部隊鍋","豆腐鍋","拌飯","飯捲"]
japaneseDish = ["拉麵","丼飯","定食","壽司"]

def randDish(_dishType):
    return {
        "中式":random.choice(chineseDish),
        "西式":random.choice(westernDish),
        "韓式":random.choice(koreanDish),
        "日式":random.choice(japaneseDish),
        "泰式":"No list",
        "越式":"No list"
    }.get(_dishType)

todayType = random.choice(dishType)
todayDish = randDish(todayType)
print("{0},{1}".format(todayType,todayDish))
