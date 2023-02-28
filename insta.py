import pyarrow.csv as pacsv
import pandas as pd
import datetime
import socket
import json
import time
import os

def get_followers_id(id, pk_id, count=-1, n=0):
    import requests
    global file_list_json
    global private_list_json
    global error_list
    ipaddress=socket.gethostbyname(socket.gethostname())
    if ipaddress=="127.0.0.1":
        time.sleep(10)
        log("Internet Error")
        get_followers_id(id, pk_id)
    cookies = {

    }

    headers = {

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

    pk_id = str(pk_id)
    print(id, n+1)
    print(response)
    follower_ls = {}
    if response.status_code==400: #비공계 계정 또는 매우 많은 팔로워
        error_list.append(pk_id)
        error_list = list(set(error_list))
        saveJson(f'{path}/error.json', error_list)
    if response.status_code == 429: #Too Many Requests Error 예외처리
        log(f"error: {response.status_code}; {pk_id}")
        time.sleep(7200)
        return get_followers_id(id=id, pk_id=pk_id, n=n+1)
    elif  response.status_code == 401 or response.status_code == 500: #인증 오류
        log(f"error: {response.status_code}")
        time.sleep(999999)
    elif response.status_code != 200: #기타
        error_list.append(pk_id)
        saveJson(f'{path}/error.json', error_list)
        return {}

    try:
        if len(response.json()["users"])==0: #팔로워가 없는 경우 또는 비공계 계정인 경우
            private_list_json.append(str(pk_id))
            saveJson(f'{path}/private.json', private_list_json) #비공계 계정 목록에 해당 id 등록하기
            return follower_ls
        for user in response.json()["users"]:
            follower_ls[user["pk_id"]]=user["username"]

    except Exception as e: #reqursts 에러로 데이터가 누락된 경우 재시도
        log(f"{id}; {e}")
        time.sleep(36)
        if n==2:
            return follower_ls
        return get_followers_id(id=id, pk_id=pk_id, count=100, n=n+1)

    save_node(f"{path}/network", pk_id, follower_ls)
    file_list_json.append(pk_id)
    return follower_ls

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def update_df():
    """df 다시 불러오기"""
    global df
    global pk_id_dict
    global id_pk_dict
    df = pacsv.read_csv(f"{path}/name_id.csv").to_pandas()
    pk_id_dict = { pk_id:id for id, pk_id in zip(df["id"], df["pk_id"]) }
    id_pk_dict = { id:pk_id for id, pk_id in zip(df["id"], df["pk_id"]) }
    


def traslate_pk_id(pk):
    """pk_id를 id로 변환"""
    global pk_id_dict
    global df
    try:
        return pk_id_dict[str(pk).replace(".0", "")]
    except:
        return -1


def traslate_id_pk(id):
    """id를 pk_id로 변환"""
    global id_pk_dict
    global df
    try:
        return str(id_pk_dict[id]).replace(".0", "")
    except:
        return -1


def save_node(Dir, name, data):
    """해당 노드의 팔로워 정보를 Json에 저장하기"""
    with open(f'{Dir}/{name}.json', 'w', encoding='utf-8') as file:
        json.dump(sorted(data.keys()), file, indent="\t")

def loadJson(Dir):
    """Json 파일에 저장된 데이터 불러오기"""
    with open(Dir, 'r', encoding="utf-8") as file:
        ls = json.load(file)
    return ls

def saveJson(Dir, data):
    """데이터를 Json 파일에 저장하기"""
    with open(Dir, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent="\t")

def save_name_id(Dict):
    mainDF = pacsv.read_csv(f"{path}/name_id.csv").to_pandas()
    DF = pd.DataFrame([[i[1] for i in Dict.items()], [i[0] for i in Dict.items()]])
    DF = DF.transpose()
    DF.columns = ["id", "pk_id"]
    mainDF.columns = ["id", "pk_id"]
    mainDF = pd.concat([mainDF, DF], axis=0)
    mainDF = mainDF.drop_duplicates()
    mainDF.to_csv(path+"/name_id.csv", index=False)
    update_df()


def readFollowerData(pk_id, id):
    ls = {}
    with open(f'{path}/network/{pk_id}.json','r', encoding="utf-8") as file:
        followers_pk_id = json.load(file)
        for line in followers_pk_id:
            pk_to_id = traslate_pk_id(line)
            ls[line] = pk_to_id
            if pk_to_id == -1:
                log(f"{id}; {line} is not exist")
                print(f"{id}; {line} is not exist")
                ls = get_followers_id(id=id, pk_id=pk_id)
                save_name_id(ls)
                time.sleep(36)
                file.close()
                if len(ls)==0: #기존에는 공개 계정이어서 팔로워가 존재 했으나 더 이상 존재하지 않는 경우
                    os.remove(f'{path}/network/{pk_id}.json')
                return ls
    return ls


def filesInFolder(Dir, extention=0):
    if extention:
        return [file.replace(f".{extention}", "") for file in os.listdir(Dir) if file.endswith(f".{extention}")]
    else:
        return [file for file in os.listdir(Dir)]


def log(text):
    with open(f'{path}/log.txt', 'a') as file:
        file.write(f"{datetime.datetime.now()} - {text}\n")
        file.close()

time_ls = []
def printTimeRemaining(n, N, L):
    global time_ls
    if len(time_ls)==L:
        time_ls.pop(0)
    time_ls.append(time.time())
    meanTime = (time.time() - time_ls[0])/L
    print("예상 시간 :", (meanTime*N))
    print("남은 시간 :", meanTime*(N-n))


def get_followers(depth=1, pk_id=0):
    global file_list_json
    global private_list_json
    global error_list
    follower_list = readFollowerData(pk_id, "seed")
    print(follower_list)
    for i in range(depth):
        target_ls = {}
        n = 0
        N = len(follower_list)
        targetLength = 0
        for j in list(dict.fromkeys(follower_list.items())):
            j = (str(j[0]).replace(".0",""), j[1    ])
            log(f"{i+1} {j[1]}: {j[0]}")
            n+=1
            print(f"{i+1} {n}/{N}, {n/N}")
            print(j[1])
            print(j[0])
            if str(j[0]) not in error_list: #비공개 계정 또는 오류 발생
                if str(j[0]) in file_list_json: #이미 팔로워 데이터가 있는 경우
                    ls = readFollowerData(j[0], j[1]) #파일에서 노드의 팔로워 데이터를 불러온다
                    targetLength+=len(ls)
                    for key, value in zip(ls.keys(), ls.values()):
                        target_ls[key] = value
                    print(targetLength)
                elif not(str(j[0]) in private_list_json): #팔로워 데이터가 없는 경우
                    print(f"{j[0]} is not exist.")
                    ls=get_followers_id(id=j[1], pk_id=j[0]) #request를 통해 팔로워를 가져온다
                    targetLength+=len(ls)
                    target_ls.update(ls)
                    print(targetLength)
                    time.sleep(36)
                printTimeRemaining(n, N, 200)
        pd.DataFrame([[i[1] for i in target_ls.items()], [i[0] for i in target_ls.items()]]).transpose().to_csv(path+"/last_work.csv", index=False)
        follower_list = dict(target_ls)


if __name__=="__main__":
    path = os.path.dirname(os.path.realpath(__file__))
    createDirectory(f"{path}/network")
    file_list_json = filesInFolder(f"{path}/network", "json")
    private_list_json = loadJson(f'{path}/private.json')
    for i in range(len(private_list_json)):
        private_list_json[i] = str(private_list_json[i]).replace(".0", "")
    error_list = loadJson(f'{path}/error.json')
    # try:
    #     mainDF = pd.read_csv(path+"/name_id.csv")
    #     print(mainDF)
    # except:
    #     mainDF = pd.DataFrame([[], []])
    #     mainDF = mainDF.transpose()
    df = pacsv.read_csv(f"{path}/name_id.csv").to_pandas()
    id_pk_dict = { id:str(pk_id) for id, pk_id in zip(df["id"], df["pk_id"]) }
    pk_id_dict = { str(pk_id):id for id, pk_id in zip(df["id"], df["pk_id"]) }
    get_followers(2, "pk_id")
