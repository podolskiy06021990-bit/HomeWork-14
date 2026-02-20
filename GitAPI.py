import requests, json

class GitHubAPI:
    BASE_URL = 'https://api.github.com'

    def __init__(self):
        pass

    def _make_request(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f'Error 404: Resource not found for endpoint {endpoint}')
            elif response.status_code == 403:
                print('Error 403: Rate limit exceeded or access forbidden')
            else:
                print(f'Error {response.status_code}: {response.reason}')
        except requests.RequestException as e:
            print(f'Network error: {e}')
        return None

    def get_user_info(self, username):
        """
        Получает информацию о пользователе GitHub по логину.
        """
        endpoint = f'/users/{username}'
        return self._make_request(endpoint)

    def get_repo_info(self, owner, repo):
        """
        Получает информацию о репозитории GitHub.
        """
        endpoint = f'/repos/{owner}/{repo}'
        return self._make_request(endpoint)

    def get_user_repos(self, username):
        """
        Получает список репозиториев пользователя.
        """
        endpoint = f'/users/{username}/repos'
        return self._make_request(endpoint)

    def save_to_json(self, data, filename):
        """
        Сохраняет данные в JSON-файл.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Данные успешно сохранены в файл {filename}")
        except IOError as e:
            print(f"Ошибка при сохранении файла: {e}")

    # Пример использования:
if __name__ == '__main__':
    gh = GitHubAPI()

    user_info = gh.get_user_info("podolskiy06021990-bit")
    if user_info:
        print(f"Пользователь: {user_info['login']}, Имя: {user_info.get('name', 'не указано')}")
        gh.save_to_json(user_info, 'user_podolskiy06021990-bit.json')

    repo_info = gh.get_repo_info("podolskiy06021990-bit", "Python_database_orm")
    if repo_info:
        print(f"Репозиторий: {repo_info['name']}, Описание: {repo_info.get('description', 'нет описания')}")
        gh.save_to_json(repo_info, 'repo_Python_database_orm.json')

#