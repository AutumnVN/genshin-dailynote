import genshinstats as gs
import requests as req

uid = 123456789
ltoken = ""
ltuid = ""

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

headers = {
    "x-rpc-app_version": "1.5.0",
    "x-rpc-client_type": "4",
    "x-rpc-language": "en-us",
    "ds": gs.genshinstats.generate_ds_token(gs.genshinstats.DS_SALT),
    "user-agent": USER_AGENT
}

resp = req.get(
    'https://bbs-api-os.hoyoverse.com/game_record/genshin/api/dailyNote',
    params=dict(server='os_asia', role_id=uid, schedule_type=1),
    headers=headers,
    cookies={'ltuid': ltuid, 'ltoken': ltoken})

print(resp.json().get('data'))
