import requests

headers = {
<<<<<<< HEAD
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

params = {
    'v': 'KmzvSo90Zj4',
}

response = requests.get('https://www.youtube.com/watch', params=params, headers=headers)

html = BS(response.content, 'html.parser')

title = html.select("title")

print(title)
=======
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'ru-RU,ru;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://jup.ag/perps',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://jup.ag/swap/USDC-SOL', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'cf7d8088-24dc-4f6b-9ac9-6c325cd614da',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"cf7d8088-24dc-4f6b-9ac9-6c325cd614da"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

params = {
    'sentry_key': '825db91cf4c44e42bfcad0fab7c234e6',
    'sentry_version': '7',
    'sentry_client': 'sentry.javascript.nextjs/7.74.1',
}

data = '{}\n{"type":"client_report"}\n{"timestamp":1719058516.656,"discarded_events":[{"reason":"network_error","category":"session","quantity":1},{"reason":"sample_rate","category":"transaction","quantity":1}]}'

response = requests.post(
    'https://o4505503099781120.ingest.sentry.io/api/4505503106400256/envelope/',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '07434e18-53f4-43f7-adb1-ca93be79019a',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"07434e18-53f4-43f7-adb1-ca93be79019a"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'a8270739-a968-4692-aab8-a22dd7190d84',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"a8270739-a968-4692-aab8-a22dd7190d84"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '09ad9b7c-79b4-4122-bfc3-959e8673fb71',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"09ad9b7c-79b4-4122-bfc3-959e8673fb71"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'cec3aed5-1f66-476c-9914-4297cb09470a',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"cec3aed5-1f66-476c-9914-4297cb09470a"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '37bdec0b-79a4-4048-9951-0776b2e48e94',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"37bdec0b-79a4-4048-9951-0776b2e48e94"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '9d15b104-3dda-4b7a-a057-a56e9696fb0d',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"9d15b104-3dda-4b7a-a057-a56e9696fb0d"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'fe257b7d-35c1-46df-baff-8429dc480ac7',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"fe257b7d-35c1-46df-baff-8429dc480ac7"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://cache.jup.ag/reference-fees', headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

response = requests.get(
    'https://birdeye-proxy.jup.ag/defi/multi_price?list_address=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v,So11111111111111111111111111111111111111112',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"cc4b6beb9997da5591fa1760b250a9358b26873b"',
    'origin': 'https://jup.ag',
    'priority': 'u=4, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://cache.jup.ag/reference-fees', headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

params = {
    'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
    'type': '5m',
    'time_to': '1719058503',
}

response = requests.get('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

params = {
    'address': 'So11111111111111111111111111111111111111112',
    'type': '5m',
    'time_to': '1719058503',
}

response = requests.get('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '9c64bdab-525e-4ac9-93a3-354655861839',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"9c64bdab-525e-4ac9-93a3-354655861839"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '02fe7c1e-1b5c-44e3-aad6-cf788242c197',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"02fe7c1e-1b5c-44e3-aad6-cf788242c197"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '098ab8ed-de4c-4958-ad9a-f44f309a876f',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"098ab8ed-de4c-4958-ad9a-f44f309a876f"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '0feeb437-19f5-46a7-a2dc-45a2c900f7fb',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"0feeb437-19f5-46a7-a2dc-45a2c900f7fb"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '2461f193-5803-46cc-bc15-9849c4570bd6',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"2461f193-5803-46cc-bc15-9849c4570bd6"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'b699939f-314a-44ce-8d8a-4c87addfa702',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"b699939f-314a-44ce-8d8a-4c87addfa702"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'fa1c9ef4-2a37-4118-8536-6234e66f192d',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"fa1c9ef4-2a37-4118-8536-6234e66f192d"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '6ea15e89-750e-42df-8df4-6db6d07bc3e9',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"6ea15e89-750e-42df-8df4-6db6d07bc3e9"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'e7133c61-8a34-43f4-80a1-9465f5dba8aa',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"e7133c61-8a34-43f4-80a1-9465f5dba8aa"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'de8959e3-45cc-45b6-bedd-37b6c0c85e25',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"de8959e3-45cc-45b6-bedd-37b6c0c85e25"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'fee04efc-7c37-4400-b232-3d58502c4fd3',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"fee04efc-7c37-4400-b232-3d58502c4fd3"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '1c7bd5a1-4b57-42f5-91b3-23a45cdfc9da',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"1c7bd5a1-4b57-42f5-91b3-23a45cdfc9da"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '0f61fb63-724f-4ad7-9f3f-975ce703ff3f',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"0f61fb63-724f-4ad7-9f3f-975ce703ff3f"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'c0a60a42-51c6-4220-9f69-df8da48e7628',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"c0a60a42-51c6-4220-9f69-df8da48e7628"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '4f32a40c-4202-4112-8b71-22e6786addb7',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"4f32a40c-4202-4112-8b71-22e6786addb7"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '6ca79497-1d14-466c-8fd2-7cb6282ed146',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"6ca79497-1d14-466c-8fd2-7cb6282ed146"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '16d36291-756a-4a7f-84be-3283c3e3e6cc',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"16d36291-756a-4a7f-84be-3283c3e3e6cc"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '589c88ea-481e-4b7e-b591-001dc410c012',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"589c88ea-481e-4b7e-b591-001dc410c012"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '2c0b9435-b581-4d29-889a-5577f9b8fb8a',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"2c0b9435-b581-4d29-889a-5577f9b8fb8a"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

response = requests.get(
    'https://birdeye-proxy.jup.ag/defi/multi_price?list_address=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v,So11111111111111111111111111111111111111112',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '129cf15b-ef8d-4ff1-8b2a-5f5943707a04',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"129cf15b-ef8d-4ff1-8b2a-5f5943707a04"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'a8fe4c88-9afe-4973-8ca6-35fb44780515',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"a8fe4c88-9afe-4973-8ca6-35fb44780515"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '2de1600f-a52f-4db0-bd1f-bfa1c3e8c50b',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"2de1600f-a52f-4db0-bd1f-bfa1c3e8c50b"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'da5e4109-fe58-410a-8d35-70ae2f7eb02f',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"da5e4109-fe58-410a-8d35-70ae2f7eb02f"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '4a5493e3-667b-4015-a11a-877895279415',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"4a5493e3-667b-4015-a11a-877895279415"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '19ffd36c-d080-4c9c-8390-d61aa47dd98e',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"19ffd36c-d080-4c9c-8390-d61aa47dd98e"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '36a29e99-8427-4315-93ed-5e5ad1dd5420',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"36a29e99-8427-4315-93ed-5e5ad1dd5420"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '190cffab-a813-4590-8819-ad9f2994a2d0',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"190cffab-a813-4590-8819-ad9f2994a2d0"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '64279373-0ec5-482b-b48e-db818cfd4eb6',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"64279373-0ec5-482b-b48e-db818cfd4eb6"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'e7a860a1-2860-4c1b-b10e-3278788e10de',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"e7a860a1-2860-4c1b-b10e-3278788e10de"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

params = {
    'sentry_key': '825db91cf4c44e42bfcad0fab7c234e6',
    'sentry_version': '7',
    'sentry_client': 'sentry.javascript.nextjs/7.74.1',
}

data = '{}\n{"type":"client_report"}\n{"timestamp":1719058608.955,"discarded_events":[{"reason":"network_error","category":"internal","quantity":1}]}'

response = requests.post(
    'https://o4505503099781120.ingest.sentry.io/api/4505503106400256/envelope/',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '7a1e8e9b-c870-42b6-8e47-7d1ca701774f',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"7a1e8e9b-c870-42b6-8e47-7d1ca701774f"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '73863a38-fb40-4630-9d8e-91fdbb1f5b26',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"73863a38-fb40-4630-9d8e-91fdbb1f5b26"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

response = requests.get(
    'https://birdeye-proxy.jup.ag/defi/multi_price?list_address=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v,So11111111111111111111111111111111111111112',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'b4973a6d-8e66-4030-98db-e7a419ce8bd6',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"b4973a6d-8e66-4030-98db-e7a419ce8bd6"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '06b14b71-3e0c-4cc9-a8d8-67721c18577f',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"06b14b71-3e0c-4cc9-a8d8-67721c18577f"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'cf0d6d78-cfae-4366-9eba-7f5ff3944225',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"cf0d6d78-cfae-4366-9eba-7f5ff3944225"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '2dd99717-f65c-4558-8c0f-871f8ab8f0e2',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"2dd99717-f65c-4558-8c0f-871f8ab8f0e2"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"6c6695819668f928f33d1e51b8cbc00e56072ce4"',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://cache.jup.ag/reference-fees', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://price.jup.ag/v4/price?ids=So11111111111111111111111111111111111111112,EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v,Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB,EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm,Faf89929Ni9fbg4gmVZTca7eW6NFg877Jqn6MizT3Gvw,HRw8mqK8N3ASKFKJGMJpy4FodwR3GKvCFKPDQNqUNuEP,J1toso1uCk3RLmjorhTtrVwY9HJ7X8V9yYac6Y7kGCPn,3B5wuUrMEi5yATD7on46hKfej3pfmd7t1RKgrsN3pump,AujTJJ7aMS8LDo3bFzoyXDwT3jBALUbu4VZhzZdTZLmG,3S8qX1MsMqRbiwKg2cQyx7nis1oHMgaCuc9c4VfvVdPN,7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr,JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN,mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So,jupSoLaHXQiZZTSfEWMTRRgpnyFm8f6sZdosWBjx93v,7BgBvyjrZX1YKz4oh9mjb8ZScatkkwb8DzFx7LoiVkM3,3XTp12PmKMHxB6YkejaGPUjMGBLKRGgzHWgJuVTsBCoP,27G8MtK7VtTcCHkpASjSDdkWWYfoqT6ggEuKidVJidD4,bSo13r4TkiE4KumL71LsHTPpL2euBYLFx6h9HP3piy1,DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263,5mbK36SZ7J19An8jFochhQS4of8g6BwUjbeCSxBSoWdp,BZLbGTNCSFfoth2GYDtwr7e4imWzpR5jqcUuGEwr646K,4Cnk9EPnW5ixfLZatCPJjDB1PUtcRpVVgTQukm9epump,3psH1Mj1f7yUfaD5gh6Zj7epE8hhrMkMETgv5TshQA4o,7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs,5oVNBeEEQvYi1cX3ir8Dx5n1P7pdxydbGF2X4TxVusJm,8wXtPeU6557ETkp9WHFY1n1EcU6NxDvbAggHGsMYiHsB,5z3EqYQo9HiCEs3R84RCDMu2n7anpDMxRhdK8PSWmrRC,MEW1gQWJ3nEXg2qgERiKu7FAFj79PHvQVREQUzScPP5,FU1q8vJpZNUrmqsciSjp8bAKKidGsLmouB8CBdf8TKQv,25hAyBQfoDhfWx9ay6rarbgvWGwDdNqcHsXS3jQ3mTDJ,3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh,6D7NaB2xsLd7cauWu1wKk6KBsJohJmP2qZH9GEfVi5Ui,he1iusmfkpAdwvxLNGV8Y1iSbj4rUy6yMhEA3fotn9A,HaP8r3ksG76PhQLTqR8FYBeNiQpejcFbQmiHbg787Ut1,rndrizKT3MK1iimdxRdWabcF7Zg7AR5T4nud4EkHBof,LSTxxxnJzKDFSLr4dUkPcmCf5VyryEqzPLz5j4bpxFp,A9mUU4qviSctJVPJdBJWkb28deg915LYJKrzQ19ji3FM,jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL,9sjyR4GrozeV8a9xM3ykKPGPXJYASy9AuufzefCyaCnP,HhJpBhRRn4g56VsyLuT8DL5Bv31HkXqsrahTTUCZeZg4,8vCAUbxejdtaxn6jnX5uaQTyTZLmXALg9u1bvFCAjtx7,ULwSJmmpxmnRfpu6BjnK6rprKXqD5jXUmPpS1FxHXFy,nosXBVoaCTtYdLvKY6Csb4AC8JCdQKKAaWYtx2ZMoo7,69kdRLyP5DTRkpHraaSZAQbWmAwzF9guKjZfzMXzcbAs,2fUFhZyd47Mapv9wcfXh5gnQwFXtqcYu9xAN4THBpump,WENWENvqqNya429ubCdR81ZmD69brwQaaBYY6p3LCpk,B5WTLaRwaUQpKk7ir1wniNB6m5o8GgMrimhKMYan2R6B,ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82,vSoLxydx6akxyMD9XEcPvGYNGq6Nn66oqVb3UkGkei7,26KMQVgDUoB6rEfnJ51yAABWWJND8uMtpnQgsHQ64Udr,METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m,GtDZKAqvMZMnti46ZewMiXCa4oXF4bZxwQPoKzXPFxZn,A3eME5CetyZPBoWbRUwY3tSe25S6tb18ba9ZPbWk9eFJ,85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ,5LafQUrVco6o7KMz42eqVEJ9LW31StPyGjeeu5sKoMtA,SHDWyBxihqiCj6YekG2GUr7wqKLeLAMK1gHZck9pL6y,9EYScpiysGnEimnQPzazr7Jn9GVfxFYzgTEj85hV9L6U,hntyVP6YFm1Hg25TN9WGLqM12b8TQmcknKrdu1oxWux,4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R,H7bTHGb5Cvo5fGe5jBDNDPUv8KykQnzyZA3qZ8sH7yxw,BX9yEgW8WkoWV8SvqTMMCynkQWreRTJ9ZS81dRXYnnR9,NYANpAp9Cr7YarBNrby7Xx4xU6No6JKTBuohNA3yscP,AMjzRn1TBQwQfNAjHFeBb7uGbbqbJB7FzXAnGgdFPk6K,HZ1JovNiVvGrGNiiYvEozEVgZ58xaU3RKwX8eACQBCt3,8doS8nzmgVZEaACxALkbK5fZtw4UuoRp4Yt8NEaXfDMb,MangmsBgFqJhW4cLUR9LxfVgMboY1xAoP8UUBiWwwuY,picobAEvs6w7QEknPce34wAE4gknZA9v5tTonnmHYdX,jucy5XJ76pHVvtPZb5TKRcGQExkwit2P5s4vY8UzmpC,HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9,6FVyLVhQsShWVUsCq2FJRr1MrECGShc3QxBwWtgiVFwK,DriFtupJYLTosbwoN8koMbEYSx54aFAVLddWsbksjwg7,9mV4WUukVsva5wYcYW4veo34CNDiF44sh3Ji65JNdvh5,Dnb9dLSXxAarXVexehzeH8W8nFmLMNJSuGoaddZSwtog,6ogzHhzdrQr9Pgv6hZ2MNze7UrzBMAFyBBWUYp1Fhitx,7G7SMGV9nSG316ykk6iobjMZWa8GZb15Wd25kgaZGTaZ,NeonTjSjsuo3rexg9o6vHuMXw62f9V7zvmu8M8Zut44,ZEUS1aR7aX8DFFJf5QjWj2ftDDdNTroMNGo8YoQm3Gq,DTEqTxxGFn3SZ4C8tNP35X8iegCCgCBrX974WFSuYVZh,BavuJ8bntC79A8aHTxQi1EUhcCnqvEU8KSBE4sVCAaHc,9n8b1EXLCA8Z22mf7pjLKVNzuQgGbyPfLrmFQvEcHeSU,LAinEtNLgpmCP9Rvsf5Hn8W6EhNiKLZQti1xfWMLy6X,DF5yCVTfhVwvS1VRfHETNzEeh1n6DjAqEBs3kj9frdAr,9MBzpyMRkj2r5nTQZMMnxnCm5j1MAAFSYUtbSKjAF3WU,Fch1oixTPri8zxBnmdCEADoJW2toyFHxqDZacQkwdvSP,947tEoG318GUmyjVYhraNRvWpMX7fpBTDQFBoJvSkSG3,Dn4noZ5jgGfkntzcQSUZ8czkreiZ1ForXYoV2H8Dm7S1,GDfnEsia2WLAW5t8yx2X5j2mkfA74i5kwGdDuZHt7XmG,ATLASXmbPQxBUYbxPsV97usA3fPQYEqzQBUHgiFCUsXx,C3JX9TWLqHKmcoTDTppaJebX2U7DcUQDEHVSmJFz6K6S,Afo4NumBNHDXc7m7p6qjZ1pF3LbqYfG5k1CNrGve8rVu,FvER7SsvY5GqAMawf7Qfb5MnUUmDdbPNPg4nCa4zHoLw,TNSRxcUxoT9xBG3de7PiJyTDYu7kskLqcpddxnEJAS6,BonK1YhkXEGLZzwtcvRTip3gAL9nCeQD7ppZBLXhtTs,KMNo3nJsBXfcpJTVhZcXLW7RmTwTt4GVFE7suUBo9sS,BMt3pq4g8ggWWBnd6DJ1jhVyTkHfWjAfJwWW6sRCbQJv,Av6qVigkb7USQyPXJkUvAEm4f599WTRvd75PUWBA9eNm,3BgwJ8b7b9hHX4sgfZ2KJhv9496CoVfsMK2YePevsBRw,9gwTegFJJErDpWJKjPfLr2g2zrE3nL1v5zpwbtsk3c6P,xN9Qd63mUYg7npanmdksmcqp3NQjTcGFQPTyq2F1TQC,DtR4D9FtVoTX2569gaL837ZgrB6wNjj6tkmnX9Rdk9B2',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"6ad05f4e070a263716979dd4d4e47894"',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://static.jup.ag/banner/metadata.json', headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

params = {
    'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
    'type': '5m',
    'time_to': '1719058503',
}

response = requests.get('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

params = {
    'address': 'So11111111111111111111111111111111111111112',
    'type': '5m',
    'time_to': '1719058503',
}

response = requests.get('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"0fff7f5a0a7aacdaba293b6429284291"',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://static.jup.ag/banner/uplink-vote/banner.json', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'e7ae4833-bf0f-4678-af69-2a7903804a64',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"e7ae4833-bf0f-4678-af69-2a7903804a64"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '9dbcc140-bb54-4440-aefa-02471a67f54f',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"9dbcc140-bb54-4440-aefa-02471a67f54f"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'bda148c9-adb0-40d5-9486-03b0351d1f21',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"bda148c9-adb0-40d5-9486-03b0351d1f21"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '354794e8-1c47-42cc-add5-e045f83b6f2e',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"354794e8-1c47-42cc-add5-e045f83b6f2e"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '99de9d02-b2d7-4b9d-a4c5-e8c62559cd33',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"99de9d02-b2d7-4b9d-a4c5-e8c62559cd33"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '2f5d1885-559e-4cc0-b9a8-6c2b850f942c',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"2f5d1885-559e-4cc0-b9a8-6c2b850f942c"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '24269877-db45-437e-8dc9-95e0a1847a64',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"24269877-db45-437e-8dc9-95e0a1847a64"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'bb18c2c0-2637-4273-9d21-5a0e7a99db03',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"bb18c2c0-2637-4273-9d21-5a0e7a99db03"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '42a5a0cf-5f16-4539-92f9-35dab17f15e6',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"42a5a0cf-5f16-4539-92f9-35dab17f15e6"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '957005b9-526e-41c4-a5ab-4cfe03f70946',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"957005b9-526e-41c4-a5ab-4cfe03f70946"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '69c75164-f1bb-4033-b171-8b36a03e18bb',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"69c75164-f1bb-4033-b171-8b36a03e18bb"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '3b4611cf-809f-4edc-8378-1475dec132e4',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"3b4611cf-809f-4edc-8378-1475dec132e4"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '135711d5-c140-483a-a6ca-2bb1ab20cad8',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"135711d5-c140-483a-a6ca-2bb1ab20cad8"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '75000679-20a4-4728-b34b-6da306e30949',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"75000679-20a4-4728-b34b-6da306e30949"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

response = requests.get(
    'https://birdeye-proxy.jup.ag/defi/multi_price?list_address=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v,So11111111111111111111111111111111111111112',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '815f4de5-123e-4aca-a67b-10b967369d97',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"815f4de5-123e-4aca-a67b-10b967369d97"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '24f23432-d1d6-4c20-b5a4-f95b0062e41d',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"24f23432-d1d6-4c20-b5a4-f95b0062e41d"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'c392e694-d6a4-4008-9eff-612449d64d82',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"c392e694-d6a4-4008-9eff-612449d64d82"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '22f9bbac-39c9-4fa1-85d1-20579e3b0494',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"22f9bbac-39c9-4fa1-85d1-20579e3b0494"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'a279c3ce-0413-4cc5-9921-9018b54a9bfc',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"a279c3ce-0413-4cc5-9921-9018b54a9bfc"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '297ecb8e-4629-4171-b869-e743e0c17a70',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"297ecb8e-4629-4171-b869-e743e0c17a70"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'be4e8cfb-86d0-4d96-ad47-a9c114e44c2c',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"be4e8cfb-86d0-4d96-ad47-a9c114e44c2c"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '4dfb47f2-67b7-4a38-a5a4-48bd659c3f30',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"4dfb47f2-67b7-4a38-a5a4-48bd659c3f30"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'ee26ea32-4120-4613-85cf-5bc2256cc231',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"ee26ea32-4120-4613-85cf-5bc2256cc231"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=b679918d1ac548c5869f00607b0af556',
    'if-none-match': 'W/"fgv9exxsz177xb"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': 'b679918d1ac548c5869f00607b0af556-87530f7d7616f1de-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-nextjs-data': '1',
}

params = {
    'inOut': 'USDC-SOL',
}

response = requests.get('https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en/va/USDC-SOL.json', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'f99e911e-fee1-4685-862f-d49fe70517a3',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"f99e911e-fee1-4685-862f-d49fe70517a3"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '72a71ada-8a91-4931-ac69-d305b76226a1',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"72a71ada-8a91-4931-ac69-d305b76226a1"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '59ab7e94-d26e-43ec-af2a-12502ce6510b',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"59ab7e94-d26e-43ec-af2a-12502ce6510b"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '3c250435-69eb-4cc3-9a63-47850f1c445b',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"3c250435-69eb-4cc3-9a63-47850f1c445b"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '49303a62-06b0-463f-85ad-c01030aa39e2',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"49303a62-06b0-463f-85ad-c01030aa39e2"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

params = {
    'sentry_key': '825db91cf4c44e42bfcad0fab7c234e6',
    'sentry_version': '7',
    'sentry_client': 'sentry.javascript.nextjs/7.74.1',
}

data = '{}\n{"type":"client_report"}\n{"timestamp":1719059747.656,"discarded_events":[{"reason":"network_error","category":"internal","quantity":1}]}'

response = requests.post(
    'https://o4505503099781120.ingest.sentry.io/api/4505503106400256/envelope/',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/',
    'Origin': 'https://jup.ag',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://cdn.jsdelivr.net/gh/nuxodin/dialog-polyfill@1.4.1/dialog.min.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/css/fd71496e888b2f20.css', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/webpack-7a6900f938bdee42.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/framework-ee8c315285b1b2ee.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/main-28402c6c4c3f6eb2.js', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/_app-3e22a67b30a2686c.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/9603-e71d4b096187cf22.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4508-9053d597488181be.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/6322-95a8f4351944a179.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/3215-7dc59b52400a7d5c.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/7369-742a4299549785e7.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/7821-ff65d247e81aeb4f.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/7375-74e79963071db593.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4518-7ee238367b063aec.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4371-b0e6cb15a3491077.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4669-c4e1087de3686680.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/6549-03798290fa08dfea.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/2029-57ea5c953dc50538.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/80-9ed5a53b8b156b7b.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/5102-751138fba9560bd4.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/swap/%5BinOut%5D-23db41ca690e8f45.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/pw750cpaaUYEiqJV7ykZ-/_buildManifest.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/pw750cpaaUYEiqJV7ykZ-/_ssgManifest.js', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('chrome-extension://aflkmfhebedbjioipglgcbcmnbpgliof/injected.js', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('chrome-extension://ejjladinnckdgjemekebdpeokbikhfci/static/js/inpage.js', headers=headers)


headers = {
    'Referer': '',
    'Origin': 'https://jup.ag',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('chrome-extension://khpkpbbcccdmmclmpigdgddabeilkdpd/assets/index.ts.c44951f8.js', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('chrome-extension://omaabbefbmiijedngplfjmnooppbclkk/provider.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'Origin': 'https://jup.ag',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/cf-fonts/v/inter/5.0.16/latin/wght/normal.woff2', headers=headers)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"2d0037ff6258b4e68f10fc81657d22b8"',
    'priority': 'i',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://jup.ag/svg/jupiter-logo.svg', headers=headers)


headers = {
    'Referer': '',
    'Origin': 'https://jup.ag',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('chrome-extension://khpkpbbcccdmmclmpigdgddabeilkdpd/assets/log.4885de7a.js', headers=headers)


headers = {
    'Referer': '',
    'Origin': 'https://jup.ag',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('chrome-extension://khpkpbbcccdmmclmpigdgddabeilkdpd/assets/innerFrom.5e95570e.js', headers=headers)


headers = {
    'Referer': '',
    'Origin': 'https://jup.ag',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'chrome-extension://khpkpbbcccdmmclmpigdgddabeilkdpd/assets/KeepAliveConnection.0c69c5ea.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/',
    'Origin': 'https://jup.ag',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get(
    'https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015',
    headers=headers,
)


headers = {
    'Referer': '',
    'Origin': 'https://jup.ag',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('chrome-extension://khpkpbbcccdmmclmpigdgddabeilkdpd/dapp-api.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
}

params = {
    'sentry_key': '825db91cf4c44e42bfcad0fab7c234e6',
    'sentry_version': '7',
    'sentry_client': 'sentry.javascript.nextjs/7.74.1',
}

data = '{"sent_at":"2024-06-22T12:35:48.300Z","sdk":{"name":"sentry.javascript.nextjs","version":"7.74.1"}}\n{"type":"session"}\n{"sid":"7b65731821a94676ac7111fbf482fee3","init":true,"started":"2024-06-22T12:35:48.300Z","timestamp":"2024-06-22T12:35:48.300Z","status":"ok","errors":0,"attrs":{"release":"eb2b2e39b80875b912384ebef0745a7beeee88af","environment":"mainnet-beta","user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}}'

response = requests.post(
    'https://o4505503099781120.ingest.sentry.io/api/4505503106400256/envelope/',
    params=params,
    headers=headers,
    data=data,
)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': '"2e5a304768451e41b69af61f0dcf35a0"',
    'priority': 'i',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://jup.ag/favicon-96x96.png', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': '"rft81arlrnt"',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://tiplink.io/api/wallet_adapter_ancestors/eyJjbGllbnRJZCI6ImY5NTliNjkzLWJiNjMtNDI0Zi05OWIyLTg3YWNlMWVkYmIxZCIsInJlZmVycmVyVXJsIjoiaHR0cHM6Ly9qdXAuYWcifQ==',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=4, i',
    'purpose': 'prefetch',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://tiplink.io/embedded_wallet?c=f959b693-bb63-424f-99b2-87ace1edbb1d&ref=https://jup.ag&v=2.1.13',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/9875.3bfa462bce90ab95.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/6116.5bd21ec98ee06c66.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://cache.jup.ag/reference-fees', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"6ad05f4e070a263716979dd4d4e47894"',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://static.jup.ag/banner/metadata.json', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '6a09c35b-ec94-47fe-866c-d435c7ac954c',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"6a09c35b-ec94-47fe-866c-d435c7ac954c"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '6ca70778-aa18-416f-841b-47890b8407b1',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"6ca70778-aa18-416f-841b-47890b8407b1"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': '"7260618ada236307ace12695af22f2770ab69ccc"',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://worker.jup.ag/lst-apys', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://quote-api.jup.ag/v6/program-id-to-label', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'jsonrpc': '2.0',
    'id': 'getAssetBatch',
    'method': 'getAssetBatch',
    'params': {
        'ids': [
            'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
            'So11111111111111111111111111111111111111112',
        ],
    },
}

response = requests.post('https://jupiter-fe.helius-rpc.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"jsonrpc":"2.0","id":"getAssetBatch","method":"getAssetBatch","params":{"ids":["EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v","So11111111111111111111111111111111111111112"]}}'
#response = requests.post('https://jupiter-fe.helius-rpc.com/', headers=headers, data=data)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'w': '48',
    'h': '48',
    'url': 'https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/logo.png',
}

response = requests.get('https://wsrv.nl/', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'w': '48',
    'h': '48',
    'url': 'https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/So11111111111111111111111111111111111111112/logo.png',
}

response = requests.get('https://wsrv.nl/', params=params, headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

response = requests.get(
    'https://birdeye-proxy.jup.ag/defi/multi_price?list_address=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v,So11111111111111111111111111111111111111112',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en;q=0.8',
    'access-control-request-headers': 'x-api-key',
    'access-control-request-method': 'GET',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
    'type': '5m',
    'time_to': '1719059748',
}

response = requests.options('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

params = {
    'address': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
    'type': '5m',
    'time_to': '1719059748',
}

response = requests.get('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

params = {
    'address': 'So11111111111111111111111111111111111111112',
    'type': '5m',
    'time_to': '1719059748',
}

response = requests.get('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en;q=0.8',
    'access-control-request-headers': 'x-api-key',
    'access-control-request-method': 'GET',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'address': 'So11111111111111111111111111111111111111112',
    'type': '5m',
    'time_to': '1719059748',
}

response = requests.options('https://birdeye-proxy.jup.ag/defi/history_price', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en;q=0.8',
    'access-control-request-headers': 'content-type',
    'access-control-request-method': 'POST',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.options('https://jupiter-fe.helius-rpc.com/', headers=headers)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2720%27%20height=%2720%27/%3e',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA4IiBoZWlnaHQ9IjEwOCIgdmlld0JveD0iMCAwIDEwOCAxMDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxMDgiIGhlaWdodD0iMTA4IiByeD0iMjYiIGZpbGw9IiNBQjlGRjIiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00Ni41MjY3IDY5LjkyMjlDNDIuMDA1NCA3Ni44NTA5IDM0LjQyOTIgODUuNjE4MiAyNC4zNDggODUuNjE4MkMxOS41ODI0IDg1LjYxODIgMTUgODMuNjU2MyAxNSA3NS4xMzQyQzE1IDUzLjQzMDUgNDQuNjMyNiAxOS44MzI3IDcyLjEyNjggMTkuODMyN0M4Ny43NjggMTkuODMyNyA5NCAzMC42ODQ2IDk0IDQzLjAwNzlDOTQgNTguODI1OCA4My43MzU1IDc2LjkxMjIgNzMuNTMyMSA3Ni45MTIyQzcwLjI5MzkgNzYuOTEyMiA2OC43MDUzIDc1LjEzNDIgNjguNzA1MyA3Mi4zMTRDNjguNzA1MyA3MS41NzgzIDY4LjgyNzUgNzAuNzgxMiA2OS4wNzE5IDY5LjkyMjlDNjUuNTg5MyA3NS44Njk5IDU4Ljg2ODUgODEuMzg3OCA1Mi41NzU0IDgxLjM4NzhDNDcuOTkzIDgxLjM4NzggNDUuNjcxMyA3OC41MDYzIDQ1LjY3MTMgNzQuNDU5OEM0NS42NzEzIDcyLjk4ODQgNDUuOTc2OCA3MS40NTU2IDQ2LjUyNjcgNjkuOTIyOVpNODMuNjc2MSA0Mi41Nzk0QzgzLjY3NjEgNDYuMTcwNCA4MS41NTc1IDQ3Ljk2NTggNzkuMTg3NSA0Ny45NjU4Qzc2Ljc4MTYgNDcuOTY1OCA3NC42OTg5IDQ2LjE3MDQgNzQuNjk4OSA0Mi41Nzk0Qzc0LjY5ODkgMzguOTg4NSA3Ni43ODE2IDM3LjE5MzEgNzkuMTg3NSAzNy4xOTMxQzgxLjU1NzUgMzcuMTkzMSA4My42NzYxIDM4Ljk4ODUgODMuNjc2MSA0Mi41Nzk0Wk03MC4yMTAzIDQyLjU3OTVDNzAuMjEwMyA0Ni4xNzA0IDY4LjA5MTYgNDcuOTY1OCA2NS43MjE2IDQ3Ljk2NThDNjMuMzE1NyA0Ny45NjU4IDYxLjIzMyA0Ni4xNzA0IDYxLjIzMyA0Mi41Nzk1QzYxLjIzMyAzOC45ODg1IDYzLjMxNTcgMzcuMTkzMSA2NS43MjE2IDM3LjE5MzFDNjguMDkxNiAzNy4xOTMxIDcwLjIxMDMgMzguOTg4NSA3MC4yMTAzIDQyLjU3OTVaIiBmaWxsPSIjRkZGREY4Ii8+Cjwvc3ZnPgo=',
    headers=headers,
)


headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'http://data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2724%27%20height=%2724%27/%3e',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getAccountInfo',
    'jsonrpc': '2.0',
    'params': [
        '3kNVxDf6NYnneLejabUrTrySgwHUrffMihRLVBJaZZ5q',
        {
            'encoding': 'base64',
            'commitment': 'confirmed',
        },
    ],
    'id': 'd17e9a45-ff3e-4407-bfb1-f4b64c2cc6f3',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getAccountInfo","jsonrpc":"2.0","params":["3kNVxDf6NYnneLejabUrTrySgwHUrffMihRLVBJaZZ5q",{"encoding":"base64","commitment":"confirmed"}],"id":"d17e9a45-ff3e-4407-bfb1-f4b64c2cc6f3"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '6c70d3c3-4842-413c-8c8f-7913f0e53836',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"6c70d3c3-4842-413c-8c8f-7913f0e53836"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': '"2e5a304768451e41b69af61f0dcf35a0"',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://jup.ag/favicon-96x96.png', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"d13ee0d9e36150259587c0dcf4f69755"',
    'priority': 'u=2',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'manifest',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://jup.ag/manifest.json', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'if-none-match': 'W/"0fff7f5a0a7aacdaba293b6429284291"',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://static.jup.ag/banner/uplink-vote/banner.json', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'ids': 'AbrMJWfDVRZ2EWCQ1xSCpoVeVgZNpq1U2AoYG98oRXfn',
}

response = requests.get('https://price.jup.ag/v4/price', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=9527467889794211a25ba26719f83a95',
    'if-none-match': 'W/"df57a5wqj377xb"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '9527467889794211a25ba26719f83a95-8adad4545331682f-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-middleware-prefetch': '1',
    'x-nextjs-data': '1',
}

response = requests.get('https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en.json', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=9527467889794211a25ba26719f83a95',
    'if-none-match': 'W/"63h3rg6juc78b5"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '9527467889794211a25ba26719f83a95-a9b259df0d351c70-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-middleware-prefetch': '1',
    'x-nextjs-data': '1',
}

response = requests.get('https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en/bridge-compare.json', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=9527467889794211a25ba26719f83a95',
    'if-none-match': 'W/"17azns9dd8878b5"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '9527467889794211a25ba26719f83a95-8d0dcda2e5787ddd-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-middleware-prefetch': '1',
    'x-nextjs-data': '1',
}

response = requests.get('https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en/perps.json', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=9527467889794211a25ba26719f83a95',
    'if-none-match': 'W/"df57a5wqj377xb"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '9527467889794211a25ba26719f83a95-a9995b714eba54cb-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-middleware-prefetch': '1',
    'x-nextjs-data': '1',
}

params = {
    'inOut': 'USDC-SOL',
}

response = requests.get('https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en/swap/USDC-SOL.json', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=9527467889794211a25ba26719f83a95',
    'if-none-match': 'W/"zly565ynp678b5"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '9527467889794211a25ba26719f83a95-96f1e5e223aac5df-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-middleware-prefetch': '1',
    'x-nextjs-data': '1',
}

params = {
    'inOut': 'USDC-SOL',
}

response = requests.get(
    'https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en/limit/USDC-SOL.json',
    params=params,
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=9527467889794211a25ba26719f83a95',
    'if-none-match': 'W/"4embnm7dgp77xb"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '9527467889794211a25ba26719f83a95-94994af2cefdd82e-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-middleware-prefetch': '1',
    'x-nextjs-data': '1',
}

params = {
    'inOut': 'USDC-SOL',
}

response = requests.get('https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en/dca/USDC-SOL.json', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-environment=mainnet-beta,sentry-release=eb2b2e39b80875b912384ebef0745a7beeee88af,sentry-public_key=825db91cf4c44e42bfcad0fab7c234e6,sentry-trace_id=9527467889794211a25ba26719f83a95',
    'if-none-match': 'W/"gdrcobnta477sd"',
    'priority': 'u=1, i',
    'purpose': 'prefetch',
    'referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '9527467889794211a25ba26719f83a95-914cbb6fc1e104c8-0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-middleware-prefetch': '1',
    'x-nextjs-data': '1',
}

params = {
    'inOut': 'USDC-SOL',
}

response = requests.get('https://jup.ag/_next/data/pw750cpaaUYEiqJV7ykZ-/en/va/USDC-SOL.json', params=params, headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/bridge-compare-7e74f3f06abdcfe1.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/bridge-compare-7e74f3f06abdcfe1.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/2358-46bf75af2c83307f.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/6308-b89a054a687e2737.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/5288-ddb545754f98f2aa.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/1263-72b97e838adbda8b.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get(
    'https://jup.ag/_next/static/chunks/pages/perps/%5Bdirection%5D/%5BinOut%5D-aa378006b1d4c033.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/2358-46bf75af2c83307f.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/6308-b89a054a687e2737.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/5288-ddb545754f98f2aa.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/1263-72b97e838adbda8b.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get(
    'https://jup.ag/_next/static/chunks/pages/perps/%5Bdirection%5D/%5BinOut%5D-aa378006b1d4c033.js',
    headers=headers,
)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/3375-65773ff26f196f37.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/3073-d7fbf3ba568ac7ed.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/3064-6b3f1fa331cfb6b1.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4540-815c0efcb92e5e10.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/limit/%5BinOut%5D-dfe7817ff08c9711.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/1364-0c1a51b6fae78088.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/1602-22ca2c1c639b8917.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4156-e0e4c5e804dead96.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/va/%5BinOut%5D-698e7af71bfff719.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/3375-65773ff26f196f37.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/3073-d7fbf3ba568ac7ed.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/3064-6b3f1fa331cfb6b1.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4540-815c0efcb92e5e10.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/limit/%5BinOut%5D-dfe7817ff08c9711.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/1364-0c1a51b6fae78088.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/1602-22ca2c1c639b8917.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/4156-e0e4c5e804dead96.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/va/%5BinOut%5D-698e7af71bfff719.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/2886-cbc265d0a2f4aeed.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/8615-7c5cb27bebc6b2b3.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/dca/%5BinOut%5D-499d22b863309382.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/2886-cbc265d0a2f4aeed.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/8615-7c5cb27bebc6b2b3.js', headers=headers)


headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'Referer': 'https://jup.ag/swap/USDC-SOL',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://jup.ag/_next/static/chunks/pages/dca/%5BinOut%5D-499d22b863309382.js', headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'c7bd46ad-5efb-49a2-bfa7-7128021fe069',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"c7bd46ad-5efb-49a2-bfa7-7128021fe069"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'verbose': '1',
    'ip': '0',
    '_': '1719059753384',
}

data = {
    'data': 'WwogICAgeyJldmVudCI6ICIkbXBfd2ViX3BhZ2VfdmlldyIsInByb3BlcnRpZXMiOiB7IiRvcyI6ICJNYWMgT1MgWCIsIiRicm93c2VyIjogIkNocm9tZSIsIiRyZWZlcnJlciI6ICJodHRwczovL2p1cC5hZy9wZXJwcyIsIiRyZWZlcnJpbmdfZG9tYWluIjogImp1cC5hZyIsIiRjdXJyZW50X3VybCI6ICJodHRwczovL2p1cC5hZy9zd2FwL1VTREMtU09MIiwiJGJyb3dzZXJfdmVyc2lvbiI6IDEyNiwiJHNjcmVlbl9oZWlnaHQiOiA4MDksIiRzY3JlZW5fd2lkdGgiOiA0ODksIm1wX2xpYiI6ICJ3ZWIiLCIkbGliX3ZlcnNpb24iOiAiMi40OS4wIiwiJGluc2VydF9pZCI6ICJkeHlwNDExdjUyZXZibHZ1IiwidGltZSI6IDE3MTkwNTk3NDguMzgyLCJkaXN0aW5jdF9pZCI6ICIza05WeERmNk5Zbm5lTGVqYWJVclRyeVNnd0hVcmZmTWloUkxWQkphWlo1cSIsIiRkZXZpY2VfaWQiOiAiMThlYTM0OTRjNjc5Y2EtMDYwNzk4MGFkYWNmMmUtMWM2NDc2MjEtMTU3MTg4LTE4ZWEzNDk0YzY4OWNhIiwiJGluaXRpYWxfcmVmZXJyZXIiOiAiaHR0cHM6Ly9zZWFyY2guYnJhdmUuY29tLyIsIiRpbml0aWFsX3JlZmVycmluZ19kb21haW4iOiAic2VhcmNoLmJyYXZlLmNvbSIsIiR1c2VyX2lkIjogIjNrTlZ4RGY2TllubmVMZWphYlVyVHJ5U2d3SFVyZmZNaWhSTFZCSmFaWjVxIiwiY3VycmVudF9wYWdlX3RpdGxlIjogIlN3YXAgfCBKdXBpdGVyIiwiY3VycmVudF9kb21haW4iOiAianVwLmFnIiwiY3VycmVudF91cmxfcGF0aCI6ICIvc3dhcC9VU0RDLVNPTCIsImN1cnJlbnRfdXJsX3Byb3RvY29sIjogImh0dHBzOiIsInRva2VuIjogImU1N2Y1MGE2YTMwYjMzYzk0MThhMDg3MmM1NmNiMWQ4IiwibXBfc2VudF9ieV9saWJfdmVyc2lvbiI6ICIyLjQ5LjAifX0sCiAgICB7ImV2ZW50IjogIldhbGxldCBDb25uZWN0ZWQiLCJwcm9wZXJ0aWVzIjogeyIkb3MiOiAiTWFjIE9TIFgiLCIkYnJvd3NlciI6ICJDaHJvbWUiLCIkcmVmZXJyZXIiOiAiaHR0cHM6Ly9qdXAuYWcvcGVycHMiLCIkcmVmZXJyaW5nX2RvbWFpbiI6ICJqdXAuYWciLCIkY3VycmVudF91cmwiOiAiaHR0cHM6Ly9qdXAuYWcvc3dhcC9VU0RDLVNPTCIsIiRicm93c2VyX3ZlcnNpb24iOiAxMjYsIiRzY3JlZW5faGVpZ2h0IjogODA5LCIkc2NyZWVuX3dpZHRoIjogNDg5LCJtcF9saWIiOiAid2ViIiwiJGxpYl92ZXJzaW9uIjogIjIuNDkuMCIsIiRpbnNlcnRfaWQiOiAiOHU4cTNtNTB1Mmc0OXhvMCIsInRpbWUiOiAxNzE5MDU5NzQ4LjYwOSwiZGlzdGluY3RfaWQiOiAiM2tOVnhEZjZOWW5uZUxlamFiVXJUcnlTZ3dIVXJmZk1paFJMVkJKYVpaNXEiLCIkZGV2aWNlX2lkIjogIjE4ZWEzNDk0YzY3OWNhLTA2MDc5ODBhZGFjZjJlLTFjNjQ3NjIxLTE1NzE4OC0xOGVhMzQ5NGM2ODljYSIsIiRpbml0aWFsX3JlZmVycmVyIjogImh0dHBzOi8vc2VhcmNoLmJyYXZlLmNvbS8iLCIkaW5pdGlhbF9yZWZlcnJpbmdfZG9tYWluIjogInNlYXJjaC5icmF2ZS5jb20iLCIkdXNlcl9pZCI6ICIza05WeERmNk5Zbm5lTGVqYWJVclRyeVNnd0hVcmZmTWloUkxWQkphWlo1cSIsIm5hbWUiOiAiUGhhbnRvbSIsInRva2VuIjogImU1N2Y1MGE2YTMwYjMzYzk0MThhMDg3MmM1NmNiMWQ4IiwibXBfc2VudF9ieV9saWJfdmVyc2lvbiI6ICIyLjQ5LjAifX0KXQ==',
}

response = requests.post('https://mixpanel.jup.ag/track/', params=params, headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'verbose': '1',
    'ip': '0',
    '_': '1719059753387',
}

data = {
    'data': 'WwogICAgeyIkc2V0X29uY2UiOiB7IiRpbml0aWFsX3JlZmVycmVyIjogImh0dHBzOi8vc2VhcmNoLmJyYXZlLmNvbS8iLCIkaW5pdGlhbF9yZWZlcnJpbmdfZG9tYWluIjogInNlYXJjaC5icmF2ZS5jb20ifSwiJHRva2VuIjogImU1N2Y1MGE2YTMwYjMzYzk0MThhMDg3MmM1NmNiMWQ4IiwiJGRpc3RpbmN0X2lkIjogIjNrTlZ4RGY2TllubmVMZWphYlVyVHJ5U2d3SFVyZmZNaWhSTFZCSmFaWjVxIiwiJGRldmljZV9pZCI6ICIxOGVhMzQ5NGM2NzljYS0wNjA3OTgwYWRhY2YyZS0xYzY0NzYyMS0xNTcxODgtMThlYTM0OTRjNjg5Y2EiLCIkdXNlcl9pZCI6ICIza05WeERmNk5Zbm5lTGVqYWJVclRyeVNnd0hVcmZmTWloUkxWQkphWlo1cSJ9Cl0=',
}

response = requests.post('https://mixpanel.jup.ag/engage/', params=params, headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'b75fd4f9-0d6f-4d9c-8c5b-294af4ec25c1',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"b75fd4f9-0d6f-4d9c-8c5b-294af4ec25c1"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '95cd23e8-dca7-4d26-9e7c-de47b0f6e7f5',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"95cd23e8-dca7-4d26-9e7c-de47b0f6e7f5"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'f7c6e80b-1f81-4fd9-8288-1e2a3ab16d91',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"f7c6e80b-1f81-4fd9-8288-1e2a3ab16d91"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'bbfd519c-e84d-45dd-b7a9-2ba7f68583de',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"bbfd519c-e84d-45dd-b7a9-2ba7f68583de"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': 'f6d0003e-923f-49af-87a9-95e1616abf43',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"f6d0003e-923f-49af-87a9-95e1616abf43"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '92e3c6d1-7fc5-49d5-9c7a-b5364c906394',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"92e3c6d1-7fc5-49d5-9c7a-b5364c906394"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '002932cb-d21c-49d0-9c95-a10bfbb0f63e',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"002932cb-d21c-49d0-9c95-a10bfbb0f63e"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '1867c800-0c8a-4e2b-be73-bfd30d6ace1d',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"1867c800-0c8a-4e2b-be73-bfd30d6ace1d"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'a39aeca7-76db-466a-9e53-f018c865336a',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"a39aeca7-76db-466a-9e53-f018c865336a"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': 'd7054dca-d692-4871-af98-21b1c403c4ac',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"d7054dca-d692-4871-af98-21b1c403c4ac"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '49625ef9-805f-44e3-93bc-955b2c21e21e',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"49625ef9-805f-44e3-93bc-955b2c21e21e"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '30fa9741-06ed-48dc-85ce-1ad35b11beae',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"30fa9741-06ed-48dc-85ce-1ad35b11beae"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '6000fff7-1eb6-4213-80fb-72c1be85df05',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"6000fff7-1eb6-4213-80fb-72c1be85df05"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '4851ddae-64ee-45fe-80e2-8ff4f55ecd12',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"4851ddae-64ee-45fe-80e2-8ff4f55ecd12"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '1768578b-e627-4f46-8661-44dc1f2be5ad',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"1768578b-e627-4f46-8661-44dc1f2be5ad"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '97ad9e5a-6197-4a70-9280-f0cb79444a4e',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"97ad9e5a-6197-4a70-9280-f0cb79444a4e"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-api-key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NzI5MDEwNzZ9.c66gFnI20ymHoPWapB0JgISzqDIK6Q_Zg0oAVp8Ssyc',
}

response = requests.get(
    'https://birdeye-proxy.jup.ag/defi/multi_price?list_address=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v,So11111111111111111111111111111111111111112',
    headers=headers,
)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '5f246109-a026-4b06-91ae-c53bfc90ec47',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"5f246109-a026-4b06-91ae-c53bfc90ec47"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'ac727ae5-1837-4039-b8e3-95c6654e2bc7',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"ac727ae5-1837-4039-b8e3-95c6654e2bc7"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'f55b4ca2-159f-47ff-a4f1-2143eb793352',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"f55b4ca2-159f-47ff-a4f1-2143eb793352"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '38c8204c-150a-4b78-aa16-a66482755934',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"38c8204c-150a-4b78-aa16-a66482755934"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '824a1196-36e3-4a65-a8b8-6c9410ebb474',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"824a1196-36e3-4a65-a8b8-6c9410ebb474"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '7b13ecc1-86b0-481e-bbed-ff988d068733',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"7b13ecc1-86b0-481e-bbed-ff988d068733"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '4a129b70-cb7f-475d-8c30-a5a18ff11b32',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"4a129b70-cb7f-475d-8c30-a5a18ff11b32"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '7273dae0-bff1-4c0b-ab37-a341a6631d57',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"7273dae0-bff1-4c0b-ab37-a341a6631d57"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '6b9a7b15-deb2-4418-88b4-ab7ac79a43a2',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"6b9a7b15-deb2-4418-88b4-ab7ac79a43a2"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '37b09e6f-8836-4ef5-a268-fbb25289b65e',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"37b09e6f-8836-4ef5-a268-fbb25289b65e"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '7205d8c8-e750-465b-a037-0d10544a0aa6',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"7205d8c8-e750-465b-a037-0d10544a0aa6"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'b821bb27-91c7-4d3a-9800-dd7c20323dad',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"b821bb27-91c7-4d3a-9800-dd7c20323dad"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getRecentPerformanceSamples',
    'jsonrpc': '2.0',
    'params': [
        6,
    ],
    'id': '400fc2ae-005d-4f86-bb49-1eb5b63ec6c8',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getRecentPerformanceSamples","jsonrpc":"2.0","params":[6],"id":"400fc2ae-005d-4f86-bb49-1eb5b63ec6c8"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '74f3ebd9-8595-45f7-b141-a850bd608daf',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"74f3ebd9-8595-45f7-b141-a850bd608daf"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': 'b5e6ab52-c637-4fa0-8ba0-1d00b34a982b',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"b5e6ab52-c637-4fa0-8ba0-1d00b34a982b"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getSlot',
    'jsonrpc': '2.0',
    'params': [
        {
            'commitment': 'processed',
        },
    ],
    'id': '0310c1fe-d7c6-43eb-8d2d-274e096e2d13',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getSlot","jsonrpc":"2.0","params":[{"commitment":"processed"}],"id":"0310c1fe-d7c6-43eb-8d2d-274e096e2d13"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://jup.ag',
    'priority': 'u=1, i',
    'referer': 'https://jup.ag/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'solana-client': 'js/0.0.0-development',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'method': 'getMultipleAccounts',
    'jsonrpc': '2.0',
    'params': [
        [
            'Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG',
            'zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU',
        ],
        {
            'encoding': 'base64',
            'commitment': 'processed',
        },
    ],
    'id': '711ad1c3-354d-47b4-82f8-caa5f348005d',
}

response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"getMultipleAccounts","jsonrpc":"2.0","params":[["Bmf1QZJSqUgj1ienxK6oPpf8ZQe5yDKmh2upRy4ymTcG","zkeLx9TRSJCQtCVb9kXw8Mms6DETtv24ePL55tjDibU"],{"encoding":"base64","commitment":"processed"}],"id":"711ad1c3-354d-47b4-82f8-caa5f348005d"}'
#response = requests.post('https://jupiter-frontend.rpcpool.com/', headers=headers, data=data)

print(response.text)
>>>>>>> 2895152b266b97aad5118934c55c5905891ad1f5
