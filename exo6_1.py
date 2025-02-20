def top_likes(users: dict):
    maxlikes = -1
    top_user = None

    for user, likes in sorted(users.items()):
        if likes > maxlikes:
            maxlikes = likes
            top_user = user
    print(top_user, maxlikes)
    return (top_user, maxlikes)



dic = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
assert top_likes(dic) == ('Ada',201)

dic = {'Bob': 102, 'Marc': 201, 'Alice': 103, 'Ada': 201}
assert top_likes(dic) == ('Ada',201)

dic = {'Bob':102}
assert top_likes(dic) == ('Bob',102)