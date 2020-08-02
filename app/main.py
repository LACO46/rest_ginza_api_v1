# -*- coding:utf-8 -*-
import url_manager
import sys
sys.path.append('./')

# import file

if __name__ == "__main__":
    # url_managerのインスタンスの作成
    urls = url_manager.urls()

    # localhost:80で開放
    urls.app.run(debug=True, host='0.0.0.0', port=80)
