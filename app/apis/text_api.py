# -*- coding:utf-8 -*-


class text:
    def add_content_api(self, file_path: str, content: str):
        # ファイルにコンテンツを追記する
        try:
            f = open(file_path, 'a')
            f.write(content)
            f.close()
        except:
            return False

        return True
