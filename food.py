class FoodAdder:
    def __init__(self, foods):
        self.foods = foods

    def add_food(self):
        name = input("음식 이름을 입력하세요: ")
        ingredients = input("재료 정보를 입력하세요(쉼표로 구분): ").split(",")
        self.foods.append({"name": name, "ingredients": ingredients})
        print(f"{name}이(가) 음식 목록에 추가되었습니다.")

class FoodSelector:
    def __init__(self, foods):
        self.foods = foods

    def select_food(self):
        if not self.foods:
            print("음식 목록이 비어 있습니다.")
            return
        choice = input("선택하실 음식 번호를 입력하세요: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(self.foods):
                print("잘못된 선택입니다.")
                return
            selected_food = self.foods[choice - 1]
            print(f"선택하신 음식: {selected_food['name']}")
            print(f"재료 정보: {', '.join(selected_food['ingredients'])}")
        except ValueError:
            print("잘못된 입력입니다.")

class FoodDeleter:
    def __init__(self, foods):
        self.foods = foods

    def delete_food(self):
        if not self.foods:
            print("음식 목록이 비어 있습니다.")
            return
        choice = input("삭제하실 음식 번호를 입력하세요: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(self.foods):
                print("잘못된 선택입니다.")
                return
            deleted_food = self.foods.pop(choice - 1)
            print(f"{deleted_food['name']}이(가) 음식 목록에서 삭제되었습니다.")
        except ValueError:
            print("잘못된 입력입니다.")

class FoodMenu:
    def __init__(self):
        self.foods = []
        self.adder = FoodAdder(self.foods)
        self.selector = FoodSelector(self.foods)
        self.deleter = FoodDeleter(self.foods)

    def display_menu(self):
        print("----------------------")
        print("음식 또는 재료를 추가, 선택, 삭제, 목록 출력, 종료을 수행하세요.")
        print("1. 음식 추가")
        print("2. 음식 선택")
        print("3. 음식 삭제")
        print("4. 음식 목록 출력")
        print("5. 종료")
        print("----------------------")

    def display_food_list(self):
        if not self.foods:
            print("음식 목록이 비어 있습니다.")
        else:
            print("음식 목록:")
            for idx, food in enumerate(self.foods, 1):
                print(f"{idx}. {food['name']} - 재료: {', '.join(food['ingredients'])}")

    def process_choice(self, choice):
        if choice == "1":
            self.adder.add_food()
        elif choice == "2":
            self.selector.select_food()
        elif choice == "3":
            self.deleter.delete_food()
        elif choice == "4":
            self.display_food_list()
        elif choice == "5":
            return False
        else:
            print("잘못된 입력입니다.")
        return True

    def run(self):
        while True:
            self.display_menu()
            choice = input("선택하실 작업을 입력하세요: ")
            if not self.process_choice(choice):
                break

menu = FoodMenu()
menu.run()