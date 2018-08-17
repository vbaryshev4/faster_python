from time import sleep


class User:
    """docstring for User"""
    def __init__(self, user_vk_id, vk_city_id, city_name, vkapi):
        self.user_vk_id = user_vk_id
        self.vk_city_id = vk_city_id
        self.city_name = city_name
        self.user_albums = None
        self.user_albums_count = None
        self.user_photos_count = None
        self.vkapi = vkapi
        self.user_photos_links = None

    def get_photos_links(self):

        if self.user_photos_links is None:
            result = []

            if self.user_albums is None:
                self.get_user_albums()

            for album in self.user_albums['items']:
                sleep(0.4)
                photos = self.vkapi.photos.get(
                    owner_id=self.user_vk_id, 
                    album_id=album['id'],
                    v=5.80
                    )
                for photo_item in photos['items']:
                    result.append(photo_item['photo_604'])

            self.user_photos_links = result

        return self.user_photos_links

    def get_user_albums(self):

        if self.user_albums is None:
            albums = self.vkapi.photos.getAlbums(
                owner_id=self.user_vk_id, 
                photo_sizes=1, 
                v=5.80
                )
            self.user_albums = albums
            self.user_albums_count = albums['count']
            self.user_photos_count = sum([i['size'] for i in albums['items']])

        return self.user_albums


class GetUsers:
    """docstring for GetUsers"""
    def __init__(self, vkapi, queue_limit):
        self.vkapi = vkapi
        self.users = None
        self.queue_limit = queue_limit
        self.users_photos_count = None

    def get_users(self, vk_city_id=None, city_name=None, sex=None, birth_year=None, users_log=None):

        if self.users is None:
            result = []
            data = self.vkapi.users.search(
                count=self.queue_limit, 
                city=vk_city_id,
                sex=sex,
                birth_year=birth_year, 
                coutry=4, 
                v=5.80
                )

            for item in data['items']:
                sleep(0.4)
                if item['id'] not in users_log:
                    person = User(item['id'], vk_city_id, city_name, self.vkapi)
                    person.get_user_albums()
                    if person.user_photos_count > 10 and person.user_photos_count < 400:
                        try:
                            person.get_photos_links()
                            result.append(person)
                        except...:
                            continue
            
            self.users = result
            self.users_photos_count = sum([i.user_photos_count for i in self.users])

        return self.users

