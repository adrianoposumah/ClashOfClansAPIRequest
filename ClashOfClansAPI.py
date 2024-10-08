import requests
import json

headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZiODNmYjg0LWEyODEtNGFiZS1iYTZlLWVlY2FjMDg5MTg0NyIsImlhdCI6MTcyODIxNDg0MSwic3ViIjoiZGV2ZWxvcGVyLzlhMTBjNTcwLWQyN2MtNTRhMi05YmNmLTk1ODI5ZGJmN2IxYyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4Mi4xLjEzNC4xMDgiLCIxODIuMS4xMzMuMjI3IiwiMTgyLjEuMTM0LjEyMCIsIjQ1Ljc5LjIxOC43OSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.x7O3cJmT1SvRsPPfafQk3TWUGDAy4PpwfURaBtSq3llk-zTkIbUpPq0Th8ZdBHTMqwr1R5jkWr74PPeuPqNnSQ',
    'Accept': 'application/json'
}

def get_user(player_tag):
    response = requests.get(
        f'https://cocproxy.royaleapi.dev/v1/players/%23{player_tag}', headers=headers)
    if response.status_code == 200:
        user_json = response.json()
        return user_json
    else:
        return {"error": "Gagal mengambil data pemain"}

def search_clans(clan_name):
    response = requests.get(
        f'https://cocproxy.royaleapi.dev/v1/clans/%23{clan_name}', headers=headers)
    if response.status_code == 200:
        clan_json = response.json()
        return clan_json
    else:
        return {"error": "Gagal mencari klan"}

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Hasil telah disimpan di {filename}")

print("Pilih opsi:")
print("1: Ambil informasi pemain")
print("2: Cari klan")

choice = input("Masukkan pilihan (1 atau 2): ")

if choice == "1":
 
    player_tag = input("Masukkan tag pemain (tanpa simbol #): ")
    user_data = get_user(player_tag)
    print("Informasi pemain:")
    print(user_data)

    save_to_json(user_data, f'player_{player_tag}.json')

elif choice == "2":

    clan_name = input("Masukkan nama klan: ")
    clan_data = search_clans(clan_name)
    print("Hasil pencarian klan:")
    print(clan_data)

    save_to_json(clan_data, f'clan_{clan_name.replace(" ", "_")}.json')

else:
    print("Pilihan tidak valid. Silakan coba lagi.")