import datetime
import requests


def get_contest():
    # 设置请求的URL和参数
    url = f'https://codeforces.com/api/contest.list?gym=false'
    # 发送GET请求
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 解析返回的JSON数据
        data = response.json()

        # 检查是否查询成功
        if data['status'] == 'OK':
            return data['result']
        else:
            return {"error": "查询失败: " + data['status']}
    else:
        return {"error": "请求失败，状态码: " + str(response.status_code)}


def format_contest():
    contest_data = get_contest()

    # 检查是否返回了错误
    if 'error' in contest_data:
        return contest_data['error']
    else:
        result = "这是近期Codeforces比赛喵~~~"
        for contest in contest_data:
            if contest['phase'] == "BEFORE":
                timestamp = contest['startTimeSeconds']
                dt_object = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(hours=8)
                result = result + "\n" + f"{contest['name']} Typ:{contest['type']}"
                result = result + "\n" + f"开始时间(UTC+8):{dt_object} \n "

        return result


if __name__ == "__main__":
    format_contest()