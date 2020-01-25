#!/bin/bash
app_dir="/Users/amsaha/workspaces/git_proj/stk-app/"
venv="stk-screen/bin/activate"
cd $app_dir
source $venv
python "stk-screen/crawler/main.py"
