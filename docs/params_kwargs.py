from typing import Optional
class kwargs:
    def __init__(self,
        email: str = None,
        pswd: str = None,
        manager: str = None,
        name: str = None,
        sellist1 : str = None,
        text : str = None) -> None:
        self.name = name
        self.pswd = pswd
        self.email = email
        pass
if __name__ == "__main__":
    user = {
        "pswd": "Password123!"
        ,"email": "chulsoo.kim@example.com"
        ,"name": "김철수"
    }
    # kwargs(email=user["email"], name=user["name"])
    # kwargs(**user)   # ** 연산자 : function에서 통째로 넘겨줄때(여기서는 dict을 통째로 매칭되서 넘겨줌) / list를 통으로 넘길때는 *
    kwargs(user)
    pass