'''
შექმენით კლასი Building. განუსაზღვრეთ ატრიბუტები: მისამართი, ფასი და
სართულების რაოდენობა. კლასს შეუქმენით გეთერები და სეთერები. დაიცავით
ენკაფსულაციის პრინციპი. კლასს განუსაზღვრეთ ფუნქცია print_info რომელიც
დაბეჭდავს კლასის ატრიბუტებს კარგად წაკითხვად ფორმატში. კლასს
გადაუტვირთეთ მეტობა-ნაკლებობის ოპერატორები. შედარება უნდა მოხდეს
საართულების რაოდენობით. შექმენით კლასის რამდენიმე ობიექტი და დაბეჭდეთ
მათზე ინფორმაცია.
'''

#8
class Building:
    def __init__(self, address, price, numbs_of_floor):
        self._address = address
        self._price = price
        self._numbs_of_floor = numbs_of_floor

    def print_info(self):
        print(f"მოცემული მისამართია: {self._address}, ფასია:{self._price}, სართულების რაოდენობაა: {self._numbs_of_floor}")

    def __lt__(self, other):
        return self._numbs_of_floor < other._numbs_of_floor

    def __ge__(self, other):
        return self._numbs_of_floor >= other._numbs_of_floor


first = Building('vake', 100000, 15)
second = Building('saburtalo', 90000, 12)

