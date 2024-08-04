import sys
input = sys.stdin.readline

# 포켓몬 수와 질문 수 입력 받기
a, b = map(int, input().split())

# 포켓몬 딕셔너리 초기화
pokemon = {}
for i in range(a):
    pokemon[i + 1] = input().strip()

# 질문 리스트 초기화
queries = []
for i in range(b):
    q = input().strip()
    try:
        queries.append(int(q))
    except:
        queries.append(q)

# 포켓몬 이름 리스트 생성
pokemon_names = list(pokemon.values())

# 질문 처리 및 출력
for q in queries:
    if isinstance(q, int):
        print(pokemon[q])
    else:
        print(pokemon_names.index(q) + 1)
