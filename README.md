# REST Ginza API

## docker コンテナのビルド方法

```
docker-compose build
```

## 起動コマンド

```
docker-compose up
```

## REST Ginza API のテスト

### リクエスト

```
curl http://localhost:8080/
```

### リクエストの結果について

```
{
  "result": [
    {
      "count": 0,
      "dep": "compound",
      "head": 5,
      "lemma": "銀座",
      "orth": "銀座",
      "pos": "PROPN",
      "tag": "名詞-固有名詞-地名-一般"
    },
    .
    .
    .
    {
      "count": 8,
      "dep": "punct",
      "head": 5,
      "lemma": "。",
      "orth": "。",
      "pos": "PUNCT",
      "tag": "補助記号-句点"
    }
  ],
  "statu_code": 200,
  "word": "銀座でランチをご一緒しましょう。"
}
```

## 形態素解析

- 形態素解析の結果の中には以下のものが含まれる
  - トークン番号
  - テキスト
  - 読みカナ
  - 基本形
  - 品詞
  - 品詞詳細
  - トークンと各トークンの依存関係
  - 依存関係の親のトークン
  - 活用情報

### リクエスト

```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"word":"<word>"}'  http://localhost:8080/v1/morphological-analysis/
```

- 形態素解析したい文章を`<word>`に入力する

### リクエストの結果について

```
{
  "result": [
    {
      "count": 0,
      "dep": "obl",
      "head": 2,
      "inf": "*,*",
      "lemma": "李",
      "pos": "NOUN",
      "reading": "スモモ",
      "tag": [
        "名詞",
        "普通名詞",
        "一般"
      ],
      "text": "すもも"
    },
    .
    .
    .
    {
      "count": 6,
      "dep": "ROOT",
      "head": 6,
      "inf": "*,*",
      "lemma": "内",
      "pos": "NOUN",
      "reading": "ウチ",
      "tag": [
        "名詞",
        "普通名詞",
        "副詞可能"
      ],
      "text": "うち"
    }
  ],
  "statu_code": 200,
  "word": "すもももももももものうち"
}
```

## 単語ごとの数値の配列

- 数値の配列は１００次元の配列を返す

### リクエスト

```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"word":"<word>"}'  http://localhost:8080/v1/word-number-array/
```

- 単語ごとの数値の配列を取得したい文章を`<word>`に入力する

### リクエストの結果について

```
{
  "result": [
    {
      "text": "すもも",
      "vector": [
        -0.7878372669219971,
        .
        .
        .
        0.6613689661026001
      ]
    },
    .
    .
    .
    {
      "text": "うち",
      "vector": [
        -0.9727846384048462,
        .
        .
        .
        1.0649694204330444
      ]
    }
  ],
  "statu_code": 200,
  "word": "すもももももももものうち"
}
```

## ２つの単語の類似度

### リクエスト

```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"word1":"<word1>", "word2":"<word2>"}'  http://localhost:8080/v1/word-cos/
```

- 類似度を調べたい文章を`<word1>`、`<word2>`に入力する

### リクエストの結果について

```
{
  "result": 0.8016603151410209,
  "statu_code": 200,
  "word1": "おにぎり",
  "word2": "おむすび"
}
```

## 辞書の更新

### リクエスト

```
curl -X GET http://localhost:8080/v1/update-dict/
```

### リクエストの結果について

- 成功の場合

```
{
  "is_succeed": true,
  "status_code": 200
}
```

- 失敗の場合

```
{
  "is_succeed": false,
  "status_code": 500
}
```

## 辞書に単語を追加

### リクエスト

```
curl -v -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"headline":"<headline>", "left_connection_id":"<left_connection_id>", "right_connection_id":"<right_connection_id>", "cost":"<cost>", "part_of_speech_one":"<part_of_speech_one>", "part_of_speech_two":"<part_of_speech_two>", "part_of_speech_three":"<part_of_speech_three>", "part_of_speech_four":"<part_of_speech_four>", "part_of_speech_advanced_type":"<part_of_speech_advanced_type>", "part_of_speech_inflected_form":"<part_of_speech_inflected_form>", "reading":"<reading>", "normalized_notation":"<normalized_notation>", "dictionary_id":"<dictionary_id>", "split_type":"<split_type>", "a_unit_division_information":"<a_unit_division_information>", "b_unit_division_information":"<b_unit_division_information>", "unused":"<unused>"}'  http://localhost:8080/v1/add-dict/
```

- 各変数の詳細については以下を参照

https://github.com/WorksApplications/Sudachi/blob/develop/docs/user_dict.md

### リクエストの結果について

- 成功の場合

```
add dict success
```

- 失敗の場合

```
add dict faild
```
