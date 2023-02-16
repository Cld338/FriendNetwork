from datetime.datetime import now
import pandas as pd
import random
import time
import os

def get_followers_id(id, pk_id, count=-1):
    import requests
    cookies = {
        'mid': 'YfZFUgALAAFR-iY66FPx9N0vjYsQ',
        'ig_did': '8016FF0E-A117-4D80-A6A2-E481C1D30CCE',
        'datr': 'hhevYvExmCwk8gZVtFds_agf',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'dpr': '0.8999999761581421',
        'ig_nrcb': '1',
        'shbid': '"4636\\05435842600577\\0541707402656:01f79f0e1a10aace3cc548d478b13c943a89232cac96d02d041a1d6325e2d91347e678c5"',
        'shbts': '"1675866656\\05435842600577\\0541707402656:01f74b496748d9b5d66ccca3e6ea0fdc53ad2bea0298ebe61e575a2b674af3316dc0cdfd"',
        'fbsr_124024574287414': 'jAlwkHJ9xbuNFUFN4AdXrJSzz-ivBm8W8_uly7uBxHQ.eyJ1c2VyX2lkIjoiMTAwMDM5MDcxMDI1OTQ3IiwiY29kZSI6IkFRQ0RrVnp3LWcwd2RXVDl6clR1Sjd0OXVhZjREN0Zyem9VRk1mVlhYRUtHT0d3M3o2NEhEN0xoS3I1TmdGRm84RUFRSHBLUmJLMkFjYUE0ZS03d2o3R2NIMUxyd2tPUGk4UFFKU1FuaUMxNDhjMVh2ZC1WVVFQRGlGSHVBUkMzOW1BMk5CU3VEeXczTlpBS1g0VVh2YU1wZ0k2ZUI3djBvb283ZHVFM2JCTkp1aFBLd0JxRmxfMTJ2VlRkeVkxeFpPNkg3YzFiNHlSSEJBcnl1UnMycUhFckRLWlI1WFR0WWRVWjZwaEFKY2x2MzBVdTFLTTdmMnJITTUzdGwxczdzRjFVdkxISlB4S0s1RDZJZG84T2RSTFJiZ1dPTlRxaU5DalRJOGMwcklqckgtbmxYSlRfNmY0Ul9MT3ROaVd0enMyMkFlZDhTc3ppa2F5UV95Zll3NW9sIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpMZExTT1pCUTRzdEFLQUcwbVJNVzhWMjVyRlVHeGdxRXNzTmdaQUZHRTdLWU1XRWVlM0ZTdm4ydlFxMUxUWHZEVjVaQzM3dVpBNnB5ZlJSUkxuOG9BN29UbUdUa2xJOE1jR2lrSkZmRzBoMHY1aWlJZTNvS3huaHBvcWxlQlZxUVhQcUpRVnNwdElqOU5iQTlvWFVZMTRFYzc4ekRheXpqYTRHbFBoIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzY0NzA4Mzh9',
        'csrftoken': 'pJ3lEhUwEqjLXdcQHxQBft7IP14kPeGH',
        'ds_user_id': '58009448489',
        'sessionid': '58009448489%3AlQ85LRzgAVk5ew%3A0%3AAYd-JheWfHF0_PNRbzWJwxcUr1UfxkcxEaTLhJ-QAg',
        'fbsr_124024574287414': 'jAlwkHJ9xbuNFUFN4AdXrJSzz-ivBm8W8_uly7uBxHQ.eyJ1c2VyX2lkIjoiMTAwMDM5MDcxMDI1OTQ3IiwiY29kZSI6IkFRQ0RrVnp3LWcwd2RXVDl6clR1Sjd0OXVhZjREN0Zyem9VRk1mVlhYRUtHT0d3M3o2NEhEN0xoS3I1TmdGRm84RUFRSHBLUmJLMkFjYUE0ZS03d2o3R2NIMUxyd2tPUGk4UFFKU1FuaUMxNDhjMVh2ZC1WVVFQRGlGSHVBUkMzOW1BMk5CU3VEeXczTlpBS1g0VVh2YU1wZ0k2ZUI3djBvb283ZHVFM2JCTkp1aFBLd0JxRmxfMTJ2VlRkeVkxeFpPNkg3YzFiNHlSSEJBcnl1UnMycUhFckRLWlI1WFR0WWRVWjZwaEFKY2x2MzBVdTFLTTdmMnJITTUzdGwxczdzRjFVdkxISlB4S0s1RDZJZG84T2RSTFJiZ1dPTlRxaU5DalRJOGMwcklqckgtbmxYSlRfNmY0Ul9MT3ROaVd0enMyMkFlZDhTc3ppa2F5UV95Zll3NW9sIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpMZExTT1pCUTRzdEFLQUcwbVJNVzhWMjVyRlVHeGdxRXNzTmdaQUZHRTdLWU1XRWVlM0ZTdm4ydlFxMUxUWHZEVjVaQzM3dVpBNnB5ZlJSUkxuOG9BN29UbUdUa2xJOE1jR2lrSkZmRzBoMHY1aWlJZTNvS3huaHBvcWxlQlZxUVhQcUpRVnNwdElqOU5iQTlvWFVZMTRFYzc4ekRheXpqYTRHbFBoIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzY0NzA4Mzh9',
        'rur': '"CCO\\05458009448489\\0541708006892:01f734dae1b6c000fdd3b2d1af9f2507e0d7009bca11709edea8895823da08a5fe16f2de"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'mid=YfZFUgALAAFR-iY66FPx9N0vjYsQ; ig_did=8016FF0E-A117-4D80-A6A2-E481C1D30CCE; datr=hhevYvExmCwk8gZVtFds_agf; fbm_124024574287414=base_domain=.instagram.com; dpr=0.8999999761581421; ig_nrcb=1; shbid="4636\\05435842600577\\0541707402656:01f79f0e1a10aace3cc548d478b13c943a89232cac96d02d041a1d6325e2d91347e678c5"; shbts="1675866656\\05435842600577\\0541707402656:01f74b496748d9b5d66ccca3e6ea0fdc53ad2bea0298ebe61e575a2b674af3316dc0cdfd"; fbsr_124024574287414=jAlwkHJ9xbuNFUFN4AdXrJSzz-ivBm8W8_uly7uBxHQ.eyJ1c2VyX2lkIjoiMTAwMDM5MDcxMDI1OTQ3IiwiY29kZSI6IkFRQ0RrVnp3LWcwd2RXVDl6clR1Sjd0OXVhZjREN0Zyem9VRk1mVlhYRUtHT0d3M3o2NEhEN0xoS3I1TmdGRm84RUFRSHBLUmJLMkFjYUE0ZS03d2o3R2NIMUxyd2tPUGk4UFFKU1FuaUMxNDhjMVh2ZC1WVVFQRGlGSHVBUkMzOW1BMk5CU3VEeXczTlpBS1g0VVh2YU1wZ0k2ZUI3djBvb283ZHVFM2JCTkp1aFBLd0JxRmxfMTJ2VlRkeVkxeFpPNkg3YzFiNHlSSEJBcnl1UnMycUhFckRLWlI1WFR0WWRVWjZwaEFKY2x2MzBVdTFLTTdmMnJITTUzdGwxczdzRjFVdkxISlB4S0s1RDZJZG84T2RSTFJiZ1dPTlRxaU5DalRJOGMwcklqckgtbmxYSlRfNmY0Ul9MT3ROaVd0enMyMkFlZDhTc3ppa2F5UV95Zll3NW9sIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpMZExTT1pCUTRzdEFLQUcwbVJNVzhWMjVyRlVHeGdxRXNzTmdaQUZHRTdLWU1XRWVlM0ZTdm4ydlFxMUxUWHZEVjVaQzM3dVpBNnB5ZlJSUkxuOG9BN29UbUdUa2xJOE1jR2lrSkZmRzBoMHY1aWlJZTNvS3huaHBvcWxlQlZxUVhQcUpRVnNwdElqOU5iQTlvWFVZMTRFYzc4ekRheXpqYTRHbFBoIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzY0NzA4Mzh9; csrftoken=pJ3lEhUwEqjLXdcQHxQBft7IP14kPeGH; ds_user_id=58009448489; sessionid=58009448489%3AlQ85LRzgAVk5ew%3A0%3AAYd-JheWfHF0_PNRbzWJwxcUr1UfxkcxEaTLhJ-QAg; fbsr_124024574287414=jAlwkHJ9xbuNFUFN4AdXrJSzz-ivBm8W8_uly7uBxHQ.eyJ1c2VyX2lkIjoiMTAwMDM5MDcxMDI1OTQ3IiwiY29kZSI6IkFRQ0RrVnp3LWcwd2RXVDl6clR1Sjd0OXVhZjREN0Zyem9VRk1mVlhYRUtHT0d3M3o2NEhEN0xoS3I1TmdGRm84RUFRSHBLUmJLMkFjYUE0ZS03d2o3R2NIMUxyd2tPUGk4UFFKU1FuaUMxNDhjMVh2ZC1WVVFQRGlGSHVBUkMzOW1BMk5CU3VEeXczTlpBS1g0VVh2YU1wZ0k2ZUI3djBvb283ZHVFM2JCTkp1aFBLd0JxRmxfMTJ2VlRkeVkxeFpPNkg3YzFiNHlSSEJBcnl1UnMycUhFckRLWlI1WFR0WWRVWjZwaEFKY2x2MzBVdTFLTTdmMnJITTUzdGwxczdzRjFVdkxISlB4S0s1RDZJZG84T2RSTFJiZ1dPTlRxaU5DalRJOGMwcklqckgtbmxYSlRfNmY0Ul9MT3ROaVd0enMyMkFlZDhTc3ppa2F5UV95Zll3NW9sIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpMZExTT1pCUTRzdEFLQUcwbVJNVzhWMjVyRlVHeGdxRXNzTmdaQUZHRTdLWU1XRWVlM0ZTdm4ydlFxMUxUWHZEVjVaQzM3dVpBNnB5ZlJSUkxuOG9BN29UbUdUa2xJOE1jR2lrSkZmRzBoMHY1aWlJZTNvS3huaHBvcWxlQlZxUVhQcUpRVnNwdElqOU5iQTlvWFVZMTRFYzc4ekRheXpqYTRHbFBoIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzY0NzA4Mzh9; rur="CCO\\05458009448489\\0541708006892:01f734dae1b6c000fdd3b2d1af9f2507e0d7009bca11709edea8895823da08a5fe16f2de"',
        'referer': 'https://www.instagram.com/instagram/followers/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'viewport-width': '1008',
        'x-asbd-id': '198387',
        'x-csrftoken': 'pJ3lEhUwEqjLXdcQHxQBft7IP14kPeGH',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2v0TxyZrSLm_hhZBdGOPheKLhtVzLNldvuyyuRMGf5iOFX',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'count': f'{count}',
        'search_surface': 'follow_list_page',
        
    }

    response = requests.get(
        f'https://www.instagram.com/api/v1/friendships/{pk_id}/followers/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(id)
    print(response)

    follower_ls = {}
    if response.status_code == 429: #sleep while instagram allows
        print(time.time())
        log(f"error: {response.status_code}, {pk_id}")
        time.sleep(7200)
        return get_followers_id(id=id, pk_id=pk_id)

    elif  response.status_code == 401: #authorization error
        log(f"error: {response.status_code}")
        time.sleep(999999)
    elif response.status_code != 200: #something else
        save_node(f"{path}/error", pk_id, follower_ls)
        return {}

    try:
        for user in response.json()["users"]:
            follower_ls[user["pk_id"]]=user["username"]
        if len(response.json()["users"])==0:
            save_node(f"{path}/private", pk_id, follower_ls)
            return follower_ls
    except:
        time.sleep(20)
        return get_followers_id(id=id, pk_id=pk_id, count=100)
    save_node(f"{path}/network", pk_id, follower_ls)
    return follower_ls


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def traslate_pk_id(pk):
    df = pd.read_csv(f"{path}/name_id.csv")
    for i in range(len(df)):
        if str(df["pk_id"][i]) == str(int(pk)):
            return df["id"][i]
    return -1


def traslate_id_pk(id):
    df = pd.read_csv(f"{path}/name_id.csv")
    for i in range(len(df)):
        if df["id"][i] == id:
            return df["pk_id"][i]
    return -1


def save_node(Dir, name, data):
    file = open(f'{Dir}/{name}.txt', 'w')
    file.write("\n".join(sorted(data.keys())))
    file.close()


def save_name_id(Dict):
    mainDF = pd.read_csv(path+"/name_id.csv")
    DF = pd.DataFrame([[i[1] for i in Dict.items()], [i[0] for i in Dict.items()]])
    DF = DF.transpose()
    DF.columns = ["id", "pk_id"]
    mainDF.columns = ["id", "pk_id"]
    mainDF = pd.concat([mainDF, DF], axis=0)
    mainDF = mainDF.drop_duplicates()
    mainDF.to_csv(path+"/name_id.csv", index=False)
    



def readFollowerData(pk_id, id):
    file = open(f'{path}/network/{pk_id}.txt','r')
    while True:
        line = file.readline()
        if not line :
            break
        ls[line.rstrip()] = traslate_pk_id(line.rstrip())
        if traslate_pk_id(line.rstrip()) == -1:
            ls = get_followers_id(id=id, pk_id=pk_id)
            time.sleep(20)
        return ls


def filesInFolder(Dir, extention=0):
    if extention:
        return [file.replace(f".{extention}", "") for file in os.listdir(Dir) if file.endswith(f".{extention}")]
    else:
        return [file for file in os.listdir(Dir)]
    


def log(text):
    file = open(f'{path}/log.txt', 'a')
    file.write(f"{now()} - {text}\n")
    file.close()



def get_followers(depth=1, pk_id=0):
    global mainDF
    file_list_txt = filesInFolder(f"{path}/network", "txt")
    follower_list = get_followers_id(id='seed', pk_id=pk_id)
    for i in range(depth):
        t = time.time()
        target_ls = {}
        n = 0
        N = len(follower_list)
        for j in list(dict.fromkeys(follower_list.items())):
            log(f"{i} ")
            private_list_txt = filesInFolder(f"{path}/private", "txt")
            file_list_txt = filesInFolder(f"{path}/network", "txt")
            n+=1
            if j[0] in file_list_txt:
                ls = readFollowerData(j[0], j[1])
                target_ls.update(ls)
                print(f"{i+1} {n}/{N}, {n/N}")
                print(j[1])
                print(len(target_ls))
            elif j[0] not in private_list_txt:
                target_ls.update(get_followers_id(id=j[1], pk_id=j[0]))
                print(len(target_ls))
                time.sleep(20 + random.randint(1,5))
            print("예상 시간 :", (time.time() - t)/(n/N))
            print("남은 시간 :", (time.time() - t)*(N/n-1))
        follower_list = dict(target_ls)
        pd.DataFrame([[i[1] for i in target_ls.items()], [i[0] for i in target_ls.items()]]).to_csv(path+"/last_work.csv")

        save_name_id(follower_list)
        

if __name__=="__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    
    createDirectory(f"{path}/network")
    createDirectory(f"{path}/private")
    createDirectory(f"{path}/error")

    file_list_txt = filesInFolder(f"{path}/network", "txt")
    try:
        mainDF = pd.read_csv(path+"/name_id.csv")
        print(mainDF)
    except:
        mainDF = pd.DataFrame([[], []])
        mainDF = mainDF.transpose()
    get_followers(2, 46512177764)   





#wldbsdld__ : 38735207759
#taeseong_0211 : 49267325443
#6u0om : 17172938212
#hhsm0204 : 51243864788
#n_namyong_ : 50170556217
#kangms9647 : 46512177764
#_wyoung__ : 34979173274
#hiliwoo : 54797325542

#_imyour._.pjy : 5474550939
#160jy_ : 49165203873
#orapaduck : 58009448489
