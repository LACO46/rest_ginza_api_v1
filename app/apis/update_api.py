# -*- coding:utf-8 -*-
import subprocess


class updaste_api_base:
    # 形態素解析の辞書の更新をするAPI
    def update_dict(self):
        try:
            # pipのモジュールをアップデートする
            subprocess.check_call('pip install --upgrade pip', shell=True)

            # 辞書を更新する
            subprocess.check_call('pip install sudachidict_core', shell=True)
        except:
            return False
        return True
