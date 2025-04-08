import os

from nova_act import NovaAct
user_data_dir='/Users/xiaoyzhu/genai/nova-act/user_data_dir'
os.makedirs(user_data_dir, exist_ok=True)

with NovaAct(starting_page="https://amazon.com/", user_data_dir=user_data_dir, clone_user_data_dir=False):
    input("Log into your websites, then press enter...")

print(f"User data dir saved to {user_data_dir=}")