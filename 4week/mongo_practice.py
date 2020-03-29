from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.dbsparta

def question1():
    # 어벤전스 평점 가져오기
    movie = db.movies.find_one({"title": "어벤져스: 엔드게임"})
    print(movie['star'])

def question2():
    # 어벤져스 엔드게임 평점이 같은 영화의 제목 가져오기
    avengers = db.movies.find_one({"title": "어벤져스: 엔드게임"})
    avengers_star = avengers['star']

    movies = list(db.movies.find({"star": avengers_star}))
    # print(movies)

    for movie in movies:
        print(movie['title'])

def question3():
    # 어벤져스 엔드게임 과 평점이 같은 영화의 평점을 0 으로 만들기
    avengers = db.movies.find_one({"title": "어벤져스: 엔드게임"})
    avengers_star = avengers['star']
    # 어벤져스랑 평점이 같은 영화 조회 후 수정(리스트로 가져오기 위해 list()로 감싸기)
    db.movies.update_many(
        {"star":avengers_star},
        {"$set":{"star":0}}
    )

    # update_many() : 조건에 맞는 모든 Document 수정하기

if __name__ == "__main__":
    # question1()
    # question2()
    question3()
