from pprint import pprint

if __name__ == '__main__':
    college = set()
    pprint(dir(college))
    pprint(type(college))
    college.add('Bill')
    college.add('Jim')
    college.add('Katy')
    pprint(college)

    family = {'Tom', 'Rae'}
    pprint(type(family))

    college = {'Bill', 'Katy', 'Verne', 'Dillon', 'Bruce', 'Olivia', 'Richard', 'Jim'}
    coworker = {'Aaron', 'Bill', 'Brandon', 'David', 'Frank', 'Connie', 'Kyle', 'Olivia'}
    family = {'Garry', 'Landon', 'Larry', 'Mark', 'Olivia', 'Katy', 'Rae', 'Tom'}

    friends1 = set.union(college, coworker, family)
    print(friends1)

    #     sorting friends into sets
    # set of all friends
    friends = {'Mark', 'Rae', 'Verne', 'Richard', 'Aaron', 'David', 'Bruce', 'Garry', 'Bill',
               'Connie', 'Larry', 'Jim', 'Landon', 'Dillon', 'Frank', 'Tom', 'Kyle', 'Katy',
               'Olivia', 'Brandon'}

    # set of people who live in my zip code
    zipcode = {'Jerry', 'Elaine', 'Cindy', 'Verne', 'Rudolph', 'Bill', 'Olivia', 'Jim', 'Lindsay',
               'Rae', 'Mark', 'Kramer', 'Landon', 'Newman', 'George'}

    # set of people who play Munchkin
    munchkins = {'Steve', 'Jackson', 'Frank', 'Bill', 'Mark', 'Landon', 'Rae'}

    # set of Olivia's friends
    olivia = {'Jim', 'Amanda', 'Verne', 'Nestor'}

    local_friends = friends.intersection(zipcode)
    print(local_friends)

    friends_to_invite = local_friends - munchkins
    print(friends_to_invite)

    invite = friends_to_invite.symmetric_difference(olivia)
    print(invite)
