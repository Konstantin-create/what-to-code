class Config:
    api_urls: dict = {
        'what_to_code': 'https://what-to-code.com/api/ideas/random',
        'ideasai': 'https://ideasai.com'
        # 'gpt3': 'https://e1-server.ml:1033'
    }
    urls: list = [
        'https://what-to-code.com',
        'https://ideasai.com'
        # 'https://e1-server.ml:1033'
    ]

    GPT3_REQUEST = 'code idea'
    save_path = '~/.what-to-code'
