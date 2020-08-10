# -*- coding:utf-8 -*-

# import file
from logics import update_dict_logics


class update_dict_controller:
    # 形態素解析の辞書の更新をするコントローラ
    def update_dict(self):
        # 変数
        update_dict_logic = update_dict_logics.update_dict_logic()

        # ロジックの呼び出し
        return update_dict_logic.update_dict()
