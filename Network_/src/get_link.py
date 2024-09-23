
import requests
import datetime

# 校园网地址
post_addr = "https://a.stu.edu.cn/ac_portal/login.php"

# 下面两个大括号里面都是复制自己学校校园网登录网站中的，冒号两边都要加上双引号
post_header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '70',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'a.stu.edu.cn',
    'Origin': 'https://a.stu.edu.cn',
    'Referer': 'https://a.stu.edu.cn/ac_portal/20170602150308/pc.html?template=20170602150308&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url=',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

post_data = {
    'opr': 'pwdLogin',
    'userName': '你自己的账号',
    'pwd': '你自己的密码',
    'ipv4or6': '',
    'rememberPwd': '0',
}


def write_info(info):
    cur_time = datetime.datetime.now()
    time_string = cur_time.strftime("%Y-%m-%d %H:%M:%S")
    info = time_string+":"+info + "\n"

    try:
        with open(r"C:\exe.log", 'a') as file:
            file.write(info)
    except  FileNotFoundError:
        print("文件不存在")
    except Exception as e:
        print("发生错误: ", str(e))
    else:
        print("成功追加信息到文件:",file)



def check_internet_connection(url="https://www.baidu.com/", timeout=5):
    """
    检查是否联网
    :param url: 测试联网状态的URL，默认为 https://www.baidu.com/
    :param timeout: 请求超时时间，默认为5秒
    :return: 如果联网，返回 True；否则返回 False
    """
    try:
        # 向指定URL发送GET请求
        response = requests.get(url, timeout=timeout)
        # 如果请求成功，返回True
        return True
    except requests.RequestException:
        # 如果请求失败，返回False
        return False

# 在脚本主体中使用此函数
info = ""
if check_internet_connection():
    print("已联网")
    info = "connected"
    # 这里放置联网后要执行的代码
else:
    print("未联网,启动联网脚本")
    # 这里放置未联网时的处理代码
    try:
        response = requests.post(post_addr, data=post_data, headers=post_header, verify=False)
        print(response.text)
    except requests.exceptions.SSLError as e:
        print("SSL证书验证失败:", e)
        info = "ssl fail"
    # response = requests.post(post_addr, data=post_data, headers=post_header, verify=False)
    # z = requests.post(post_addr, data=post_data, headers=post_header, verify=False)
    # 如果不想每次都手动关闭窗口可以删除下面的input，然后将print里的内容改成自己想要的
    print("连接成功，按任意键以退出")
    info = "connect success"
write_info(info)

