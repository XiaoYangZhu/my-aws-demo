#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import fire  # type: ignore
import getpass

from nova_act import NovaAct

# 设置用户数据目录路径
user_data_dir = str(Path.home() / "..nova_act_126_profile2")

def main(record_video: bool = True,logs_directory="/Users/lht/Desktop"):
    # 确保目录存在
    print(f"设置 Chrome 用户数据目录: {user_data_dir}")
    print("将打开浏览器，请登录到 126.com，然后按回车键继续...")
    # username = input("请输入你的 126 用户名或邮箱: ")
    password = ""

    # 启动浏览器并等待用户登录
    with NovaAct(starting_page="https://www.126.com/", record_video=record_video,clone_user_data_dir=True) as nova:
        nova.act("enter username liu_ht and click on the password field")
        nova.act("enter '' in the password field")
        nova.page.keyboard.type(password)
        nova.act("press button and continue ")
        nova.act("select inbox menu")
        nova.act("read first mail")
        nova.act("reply the mail with thanks")
        nova.act("send mail")


        # nova.act("check the checkbox")
        # nova.act("login")

if __name__ == "__main__":
    fire.Fire(main)