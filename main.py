import requests


class SuperHero:
    URL = "https://superheroapi.com/api/2619421814940190"

    def __init__(self, name):
        self.name = name
        search_by_name_url = self.URL + "/search/" + self.name
        self.info = requests.get(search_by_name_url)

    def get_intelligence(self):
        return int(self.info.json()['results'][0]['powerstats']['intelligence'])


def get_smartest_hero(heroes_list):
    if heroes_list:
        heroes_dict = {}
        smartest = heroes_list[0]
        for hero in heroes_list:
            heroes_dict[hero] = SuperHero(hero).get_intelligence()
            if heroes_dict[hero] >= heroes_dict[smartest]:
                smartest = hero
        return smartest
    else:
        return 'No heroes in list'


if __name__ == "__main__":
    heroes = ['Hulk', 'Captain America', 'Thanos']
    print('Smartest hero is:', get_smartest_hero(heroes))
