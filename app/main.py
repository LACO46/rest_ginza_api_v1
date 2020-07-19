# -*- coding:utf-8 -*-
import sys
sys.path.append('./')

# import file
import url_manager

if __name__ == "__main__":
    urls = url_manager.urls()
    urls.app.run(debug=True, host='0.0.0.0', port=80)
