class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: float,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car: list) -> float:
        """
        Приймає список автомобілів, миє лише ті,
        у яких clean_mark нижче clean_power станції.
        Повертає дохід станції від миття цих автомобілів,
        округлений до 1 десятої.
        """
        total_income = 0
        for i in car:
            if i.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(i)
                print(f"***I can clean {i.brand}***")
                self.wash_single_car(i)
        return round(total_income, 1)

    def calculate_washing_price(self, car: any) -> float:
        """
        Розрахунок вартості миття автомобіля за формулою:
        клас комфорту авто * різниця між потужністю мийки
        та рівнем забруднення авто * рейтинг автомийки /
        відстань автомийки до центру міста
        """
        washing_price = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1)
        print(f"Price washing {car.brand}: {washing_price}")
        return washing_price

    def wash_single_car(self, car: str) -> None:
        """
        Миє один авто. Якщо clean_power станції більший за clean_mark авто,
        то clean_mark прирівнюється до clean_power.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        """
        Оновлює середній рейтинг та к-сть людей після отримання нової оцінки.
        """
        self.average_rating = round(
            (self.count_of_ratings * self.average_rating + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        print(f"New rating station: {self.average_rating}"
              f"({self.count_of_ratings}people)")
