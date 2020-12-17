class Entity(object):  # -> класс сущность
    def __init__(self, name: str, category: str, planet: str, character: str):
        self._name = name
        self._category = category
        self._planet = planet  # -> планета вида
        self._character = character

    def __str__(self):  # -> переопределение строкового метода
        return f'Знакомтесь с {self._name}. Это {self._category} родом с планеты {self._planet}. ' \
               f'Характер {self._character}.'

    def get_name(self):
        return self._name

    def get_planet(self):  # -> получение названия планеты
        return self._planet

    def get_character(self):
        return self._character


class Flying(Entity):
    def __init__(self, name: str, category: str, planet: str, character: str, wings: str, flight_altitude: int):
        super().__init__(name, category, planet, character)
        self._wings = wings
        self._flight_altitude = flight_altitude

    def __str__(self):
        return f'{super().__str__()}\n  {self._name.capitalize()} имеет {self._wings}, за счёт чего летает и способен' \
               f' подниматься на высоту до {self._flight_altitude}м.'

    def get_wings(self):
        return self._wings

    def get_flight_altitude(self):
        return self._flight_altitude


class PlantLike(Entity):
    def __init__(self, name: str, category: str, planet: str, character: str, cover: str, sustainability: str,
                 special_skill: str):
        super().__init__(name, category, planet, character)
        self._cover = cover
        self._sustainability = sustainability
        self._special_skill = special_skill

    def __str__(self):
        return f'   {super().__str__()}\n   Снаружи его покрывает {self._cover}, поэтому он {self._sustainability} ' \
               f'к влияниям извне.\n   Особые умения: {self._special_skill}.'

    def get_cover(self):
        return self._cover

    def get_sustainability(self):
        return self._sustainability

    def get_special_skill(self):
        return self._special_skill

    def set_special_skill(self, new_special_skill):
        self._special_skill = new_special_skill
        return self._special_skill


class Aquatic(Entity):
    def __init__(self, name: str, category: str, planet: str, character: str, limbs: str, carapace: bool):
        super().__init__(name, category, planet, character)
        self._limbs = limbs
        self._carapace = carapace

    def __str__(self):
        if self._carapace:
            return f'   {super().__str__()}\n   {self._name} обитает в воде. Для передвижения использует ' \
                   f'{self._limbs}, а надёжной защитой служит панцирь.'
        else:
            return f'{super().__str__()}\n{self._name} обитает в воде. Для передвижения использует {self._limbs}.'

    def get_limbs(self):
        return self._limbs

    def get_carapace(self):
        return self._carapace


class PredatorFlying(Flying):
    def __init__(self, name: str, category: str, planet: str, character: str, wings: str, flight_altitude: int,
                 food: str, feature: str):
        super().__init__(name, category, planet, character, wings, flight_altitude)
        self._food = food
        self._feature = feature

    def __str__(self):
        return f'   {super().__str__()}\n   {self._name} хищник. Питается {self._food}. В охоте за добычей использует' \
               f' {self._feature}.'

    def get_food(self):
        return self._food

    def get_feature(self):
        return self._feature

    def set_feature(self, new_feature):
        self._feature = new_feature
        return self._feature


class TamedAquatic(Aquatic):
    def __init__(self, name: str, category: str, planet: str, character: str, limbs: str, carapace: bool,
                 application_area: str):
        super().__init__(name, category, planet, character, limbs, carapace)
        self._limbs = limbs
        self._carapace = carapace




