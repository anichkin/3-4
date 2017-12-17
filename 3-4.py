from urllib.parse import urlencode
import requests

AUTORISER_URL = 'https://oauth.vk.com/authorize'
APP_ID = '6262295'
VERSION = '5.69'

auth_data = {
    'client_id': APP_ID,
    'redirect_url': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': VERSION
}
print('?'.join(
    (AUTORISER_URL, urlencode(auth_data))
))

TOKEN = '5372e7d19e098cbd96c42cffa2e61a3450535c14ea8daaa6139f3f8c1fd52ed6a4cfd9869e13038715a52'

params = {
    'access_token': TOKEN,
    'v': VERSION
}

response = requests.get('https://api.vk.com/method/friends.get', params)
response_json = response.json()
my_friend_list = response_json['response']['items']
print('Мой список друзей ', my_friend_list)


def get_friends_list(friend_id, VERSION):
    friend_params = {
        'user_id': friend_id,
        'v': VERSION
    }

    response_friend = requests.get('https://api.vk.com/method/friends.get', friend_params)
    response_friend_json = response_friend.json()
    if 'response' in response_friend_json.keys():
        friend_list = response_friend_json['response']['items']
        return friend_list


def friends_friends_list(my_friend_list):
    for friend_id in my_friend_list:
        print('Идентификатор друга: ', friend_id)
        print('список друзей друга: ', get_friends_list(friend_id, VERSION))


def cross_friends(my_friend_list):
    crossing_friends = get_friends_list(my_friend_list[0], VERSION)
    for friend_id in my_friend_list:
        if not get_friends_list(friend_id, VERSION):
            continue
        else:
            crossing_friends = list(set(crossing_friends) & set(get_friends_list(friend_id, VERSION)))
            print(crossing_friends)

friends_friends_list(my_friend_list)
cross_friends(my_friend_list)
