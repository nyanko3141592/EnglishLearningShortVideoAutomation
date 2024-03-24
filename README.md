## 自動ショート動画作成プログラム

この Python プログラムは、与えられた JSON ファイルから情報を取り出し、自動的にショート動画を生成します。テキストから音声合成を行い、それを動画として出力します。

### 使い方

1. **依存関係のインストール**

   このプログラムを実行する前に、以下の依存関係をインストールしてください。

   ```bash
   pip install -r requirements.txt
   ```

2. **実行**

   `main.py` を実行することでプログラムを起動します。

   ```bash
   python main.py
   ```

   実行時にはコマンドライン引数は必要ありません。プログラムは `script.json` という名前の JSON ファイルを探し、それを使用して動画を生成します。

3. **JSON ファイルの準備**

   プログラムは `script.json` という名前の JSON ファイルを想定しています。このファイルには以下のような情報が含まれている必要があります。

   ```json
   [
     {
       "japanese": "君の瞳に吸い込まれそうだ",
       "english": "I feel like I'm being drawn into your eyes",
       "key_phrase": "drawn into",
       "description": "強く引きつけられる感覚"
     }
   ]
   ```

   - `japanese`: 英文の和訳
   - `english`: 英文
   - `key_phrase`: キーフレーズ
   - `description`: キーフレーズの説明

4. **BGM ファイルの準備**

   VideoTemplate 以下の BGM フォルダに BGM ファイルを配置してください。

5. **env ファイルの準備**

   プログラムは `env.py` という名前の 環境変数を設定するファイルを用意しています。

   ```python
   ACCESSKEY = ""
   ACCESS_SECRET = ""

   # CoeFont ID
   JP_ID = ""
   EN_ID = ""
   ```

```

### 注意事項

- プログラムは音声合成に使用するテキストと動画の情報が含まれる JSON ファイルを `script.json` として想定しています。ファイル名や形式を変更する場合は、プログラム内の適切な箇所を変更してください。
- このプログラムはテキストから音声合成を行い、それを動画として出力します。しかし、動画のデザインやアニメーションなどは含まれていません。必要に応じて拡張・改良してください。

### 依存関係

- `ffmpeg`: 動画生成に使用されます。
- `MovieMagic`: 動画生成に使用されます。
- `coefont`: テキストから音声合成に使用されます。

### ライセンス

MIT License

### 作者

Naoki TAKAHASHI
```
