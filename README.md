# 基于idf的小狼毫词库


# 部署位置：
1.复制目录下内容到以下文件夹
 ~/.config/ibus/rime  (Linux)
 ~/Library/Rime  (Mac OS)
 %APPDATA%\Rime  (Windows)


2.重新载入后生效





# 自己生成词典
访问https://github.com/t-web/tf-idf-keyword
到这里训练生成idf.txt文件后 将内容替换掉

use_preset_vocabulary: true
...
之后内容即可
