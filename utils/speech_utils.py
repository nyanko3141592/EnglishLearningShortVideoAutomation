import hmac
import requests
import hashlib
import json
from datetime import datetime, timezone


def generate_speech(
    text: str, speaker_id: str, access_key: str, access_secret: str, output_path: str
) -> None:
    """
    指定されたテキストを音声に変換し、WAVファイルとして保存する関数

    Args:
        text (str): 音声に変換するテキスト
        speaker_id (str): 使用する話者のID
        access_key (str): CoefontのアクセスキーID
        access_secret (str): CoefontのアクセスシークレットキーID
        output_path (str): 保存するWAVファイルのパス

    Returns:
        None
    """
    date: str = str(int(datetime.utcnow().replace(tzinfo=timezone.utc).timestamp()))
    data: str = json.dumps({"coefont": speaker_id, "text": text})
    signature = hmac.new(
        bytes(access_secret, "utf-8"), (date + data).encode("utf-8"), hashlib.sha256
    ).hexdigest()

    response = requests.post(
        "https://api.coefont.cloud/v2/text2speech",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": access_key,
            "X-Coefont-Date": date,
            "X-Coefont-Content": signature,
        },
    )

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
    else:
        print(response.json())
