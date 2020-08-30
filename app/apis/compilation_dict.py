# -*- coding:utf-8 -*-
import subprocess


class compilation_dict_base:
    def compilation_dict(self):
        # 辞書をコンパイルするAPI
        try:
            # 辞書をコンパイルするコマンド
            subprocess.check_call(
                'cd user_dict && sudachipy ubuild -s /usr/local/lib/python3.7/site-packages/sudachidict_core/resources/system.dic user_dict.csv && cd ..', shell=True)
        except:
            return False
        return True
