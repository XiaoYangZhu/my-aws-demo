import os
from nova_act import NovaAct, BOOL_SCHEMA

user_data_dir='/Users/xiaoyzhu/genai/nova-act/user_data_info'
logs_directory='/Users/xiaoyzhu/genai/nova-act/log_info'
video_directory='/Users/xiaoyzhu/genai/nova-act/video_info'

if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

if not os.path.exists(video_directory):
    os.makedirs(video_directory)

if os.path.exists(user_data_dir) and os.path.isdir(user_data_dir):
    print(f"User data dir already exists: {user_data_dir=}.")
    with NovaAct(starting_page="https://amazon.com/", user_data_dir=user_data_dir, clone_user_data_dir=False, logs_directory=logs_directory, record_video=True) as nova:
        result = nova.act("Am I logged in?", schema=BOOL_SCHEMA)
        if not result.matches_schema:
            # act response did not match the schema ¯\_(ツ)_/¯
            print(f"Invalid result: {result=}")
        else:
            # result.parsed_response is now a bool
            if result.parsed_response:
                print("You are logged in")
                nova.act("search for a coffee maker")
                nova.act("select the second result")
                nova.act("scroll down or up until you see 'add to cart' and then click 'add to cart'")
                #nova.act("then logout my amazon.com account by clicking on the 'Account & Lists' and then click on the 'Sign Out'")
                input("PLEASE CONFIRM THE ACTION TAKEN ALREADY!!!")
            else:
                print("You are NOT logged in")
                input("Log into your websites, after the login, then press enter here...")
                print(f"User data dir saved to {user_data_dir=}")
                nova.act("search for a coffee maker")
                nova.act("select the second result")
                nova.act("scroll down or up until you see 'add to cart' and then click 'add to cart'")
                #nova.act("then logout my amazon.com account by clicking on the 'Account & Lists' and then click on the 'Sign Out'")
                input("PLEASE CONFIRM THE ACTION TAKEN ALREADY!!!")
else:
    print(f"User data dir does NOT exist: {user_data_dir=}, and creating the folder...")
    os.makedirs(user_data_dir, exist_ok=True)
    with NovaAct(starting_page="https://amazon.com/", user_data_dir=user_data_dir, clone_user_data_dir=False, logs_directory=logs_directory, record_video=True) as nova:
        result = nova.act("Am I logged in?", schema=BOOL_SCHEMA)
        if not result.matches_schema:
            # act response did not match the schema ¯\_(ツ)_/¯
            print(f"Invalid result: {result=}")
        else:
            # result.parsed_response is now a bool
            if result.parsed_response:
                print("You are logged in")
                nova.act("search for a coffee maker")
                nova.act("select the second result")
                nova.act("scroll down or up until you see 'add to cart' and then click 'add to cart'")
                #nova.act("then logout my amazon.com account by clicking on the 'Account & Lists' and then click on the 'Sign Out'")
                input("PLEASE CONFIRM THE ACTION TAKEN ALREADY!!!")
            else:
                print("You are NOT logged in")
                input("Log into your websites, after the login, then press enter here...")
                print(f"User data dir saved to {user_data_dir=}")
                nova.act("search for a coffee maker")
                nova.act("select the second result")
                nova.act("scroll down or up until you see 'add to cart' and then click 'add to cart'")
                #nova.act("then logout my amazon.com account by clicking on the 'Account & Lists' and then click on the 'Sign Out'")
                input("PLEASE CONFIRM THE ACTION TAKEN ALREADY!!!"))