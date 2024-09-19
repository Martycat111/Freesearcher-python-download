import requests, os

def list_github_repo_files():
    api_url = "https://api.github.com/repos/Martycat111/Freesearcher-Python_Files/contents"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        contents = response.json()
        if isinstance(contents, list):
            for content in contents:
                print(f"- {content['path']}" if content['type'] == 'file' else f"[Directory] {content['path']}")
        else:
            print("Failed to list files: Unexpected response format.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while listing files: {e}")

while True:
    user = input(">>> ").strip().lower()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if user == "search-list":
        list_github_repo_files()
    else:
        url = f'https://raw.githubusercontent.com/Martycat111/Freesearcher-Python_Files/main/{user}'
        file_path = os.path.join(script_dir, user)
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {user} at {file_path}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Error: The file '{user}' was not found in the repository.")
            else:
                print(f"An error occurred: {e.response.status_code}")
        except Exception as e:
            print(f"Error writing to file: {e}")
