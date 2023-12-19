try:
    from telethon.sync import TelegramClient
    from telethon.tl.functions.account import UpdateProfileRequest
    import requests, time, os, api
except ModuleNotFoundError:
    os.system('pip install --upgrade pip && pip install telethon && pip install asyncio && pip install aiocron && clear')
    os.sys.exit('installed the required packages !')

def get_credentials():
    api_id = input("Your api id: ")
    api_hash = input("Your api hash: ")
    number = input("Your Number: ")
    return api_id, api_hash, number

def save_credentials(api_id, api_hash, number):
    api.id = api_id
    api.hash = api_hash
    api.number = number
    with open("api.py", "w") as api_file:
        api_file.write(f"id = '{api_id}'\nhash = '{api_hash}'\nnumber = '{number}'")

def apicheck():
    if api.id is None or api.hash is None or api.number is None:
        api_id, api_hash, number = get_credentials()
        save_credentials(api_id, api_hash, number)
    else:
        print(f"Credentials already set.\nPlease Wait")
        main()

coins_info = {
    'bitcoin': 'BTC',
    'tether': 'USDT',
    'ethereum': 'ETH'
}


def set_bio(bio):
    client = TelegramClient('H3x', api.id, api.hash)
    client.start(api.number)
    client(UpdateProfileRequest(about=bio))

def main():
    while True:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={",".join(coins_info.keys())}&vs_currencies=usd')
            data = response.json()

            bio_text = "| Make money  for more 💵💰 | "
            
            for coin_id, coin_symbol in coins_info.items():
                bio_text += f"{coin_symbol} : $ {data[coin_id]['usd']}   |   "

            set_bio(bio_text)
            
            time.sleep(40)

        except Exception as e:
            print(f"An error occurred: {e}")

            time.sleep(10)
if __name__ == "__main__":
    apicheck()
