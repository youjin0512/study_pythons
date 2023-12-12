# function만 사용해 적 캐릭터 만들기
# first 적 캐릭터
name = "first"
health = 120
damage = 0

def attack(health, damage) :
    health = health - damage
    return health

### damage = attack(5)

# second 적 캐릭터
name = "second"
health = 200
damage = 0
### damage = attack(10)

# function만 사용 시 제한 극복 -> class
class Enemy :
    def __init__(self, name, health) :   # Enemy = Self, Self = Enemy    #여기에서의 name은 외부에서 들어온 name
        self.name = name     # 외부 변수 name 값이 내부 변수(self) name에 할당
        self.health = health
        self.damage = 0
        pass

    def attack(self, damage) :
        self.health = self.health - damage
        return self.health
    
    def function_name(self) :       # Enemy = Self, Self = Enemy
        pass
        return 0
    
# first_enemy = Enemy()  # 자신의 자원(functions와 variables(변수)) 확인
first_enemy = Enemy('first', 150)  # 자신의 자원(functions와 variables(변수)) 확인
second_enemy = Enemy('second', 300)
pass


# def function_name() : 
#   pass      # 내용 넣기
#   return 0