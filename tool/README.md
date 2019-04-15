# 基于TD-IDF的中文关键词提取

## requirements

默认环境python3，需要结巴分词器的支持

```bash
$ pip install jieba
```

## IDF(逆文档频率)生成

用法：

```bash
$ python gen_idf.py -i <inputdir> -o <outputfile>


python3 gen_idf.py -i test/ -o luna_pinyin.idf.dict.yaml


python3 gen_idf_mini.py -i test/ -o luna_pinyin.idf.dict.yaml


python3 gen_idf.py -i test/ -o ../luna_pinyin.extended.idf/luna_pinyin.idf.dict.yaml
```

- `-i <inputdir>`   ： 语料库目录，程序会扫描目录下的所有文件
- `-o <outputfile>` ： 保存idf到指定文件



pip install jieba
pip install pypinyin
