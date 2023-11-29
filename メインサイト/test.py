def handle_json(s: str, file_name: str = "sample.json"):
  import json

  key = "my_key" # 任意のキー
  dic = {key:s}

  # 保存
  with open(file_name, "w") as f:
    json.dump(dic, f, ensure_ascii=False) # ensure_ascii=False を削除すると日本語が文字コードとして出力される

  # 読込
  with open(file_name, "r") as f:
    dic = json.load(f)
    s = dic[key]

handle_json("Hoge/ふが\n#\tピヨ")
