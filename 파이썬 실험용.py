
# 클래스(붕어빵틀) 정의
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    
    def make_sound(self):
        print(f'{self.name}은 {self.sound}하고 웁니다.')


# 상속을 통한 클래스 확장
class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def show_info(self):
        print(f'이 개는 {self.breed}이고 이름은 {self.name}입니다.')


#객체(인스턴스,오브젝트) 생성
dog1 = Dog('골댕이', '월월', '골든 리트리버')
#속성은 name,sound,breed ......
#cf. 메써드와 속성의 구분? : 함수는 .함수(), 속성은 .속성?


#메서드(행위, 함수) 호출
dog1.make_sound()
dog1.show_info()

