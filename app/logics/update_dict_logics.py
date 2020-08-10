# -*- coding:utf-8 -*-
from dataclasses import dataclass

from apis import update_api

# resultの型
@dataclass
class UpdateDictResultModel:
    statu_code: int
    is_succeed: str


class update_dict_logic:
    # 形態素解析の辞書の更新をするロジック
    def update_dict(self) -> UpdateDictResultModel:
        # 変数
        updaste_api_base = update_api.updaste_api_base()

        # apiの呼び出し
        is_succeed = updaste_api_base.update_dict()

        # レスポンスの作成
        return {
            'status_code': 200,
            'is_succeed': is_succeed
        }
