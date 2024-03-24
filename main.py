import glob
import os
import datetime
import random

import env
import utils.video_edit as vt
import utils.file_utils as fu
import utils.speech_utils as su
import utils.video_utils as vu

ACCESSKEY = env.ACCESSKEY
ACCESS_SECRET = env.ACCESS_SECRET

JP_ID = env.JP_ID
EN_ID = env.EN_ID

BGMS = glob.glob("videoTemplate/BGM/*.mp3")

# 台本読み込み
file_path = "scripts/script.json"
data = fu.load_json_data(file_path)
fu.display_data(data)


def generate_sound(item: dict, temp_output_dir: str):
    # 英語文章の生成
    su.generate_speech(
        item["english"],
        EN_ID,
        ACCESSKEY,
        ACCESS_SECRET,
        os.path.join(temp_output_dir, f"{item['english']}.wav"),
    )
    print(f"英語の音声ファイルを生成しました。{item['english']}")

    # 英語文章の生成
    su.generate_speech(
        item["key_phrase"],
        EN_ID,
        ACCESSKEY,
        ACCESS_SECRET,
        os.path.join(temp_output_dir, f"{item['key_phrase']}.wav"),
    )
    print(f"キーフレーズの音声ファイルを生成しました。{item['key_phrase']}")

    # 日本語文章の生成
    su.generate_speech(
        item["japanese"],
        JP_ID,
        ACCESSKEY,
        ACCESS_SECRET,
        os.path.join(temp_output_dir, f"{item['japanese']}.wav"),
    )
    print(f"日本語の音声ファイルを生成しました。{item['japanese']}")

    # 日本語文章の生成
    su.generate_speech(
        item["situation_description"],
        JP_ID,
        ACCESSKEY,
        ACCESS_SECRET,
        os.path.join(temp_output_dir, f"{item['situation_description']}.wav"),
    )
    print(f"日本語の音声ファイルを生成しました。{item['situation_description']}")

    # 日本語文章の生成
    su.generate_speech(
        item["description"],
        JP_ID,
        ACCESSKEY,
        ACCESS_SECRET,
        os.path.join(temp_output_dir, f"{item['description'].replace("\n", "")}.wav"),
    )
    print(f"日本語の音声ファイルを生成しました。{item['description'].replace("\n", "")}")


for item in data:
    # 今日の日付を取得
    today = datetime.date.today()
    # todayをtextにする
    today = today.strftime("%Y%m%d")
    file_name = today + "-" + item["english"].replace(" ", "_")
    output_path: str = os.path.join("out", f"{file_name}.mp4")
    # すでにファイルが存在する場合はスキップ
    if os.path.exists(output_path):
        print(f"{output_path}はすでに存在します。スキップします。")
        continue
    temp_output_dir = "tempOutput"
    template_dir = "videoTemplate"
    print("--" * 10)
    print()
    print(file_name)

    con_video_list = []

    generate_sound(item, temp_output_dir)

    bubble_position_y = 0.35

    # Start
    output_video = os.path.join(temp_output_dir, "start.mp4")
    con_video_list.append(output_video)
    vt.speech_bubble_video(
        os.path.join(template_dir, "1_start.mp4"),
        os.path.join(temp_output_dir, f"{item['situation_description']}.wav"),
        output_video,
        "", # item["situation_description"],
        color="white",
        position_y=bubble_position_y,
    )
    print(f"{output_video}を生成しました。")

    # JP
    output_video = os.path.join(temp_output_dir, "2_jp.mp4")
    con_video_list.append(output_video)
    vt.speech_bubble_video(
        os.path.join(template_dir, "2_jp_read.mp4"),
        os.path.join(temp_output_dir, f"{item['japanese']}.wav"),
        output_video,
        item["japanese"] + "\nって言いたい。",
        color="black",
        after_time=0.5,
        position_y=bubble_position_y,
    )
    print(f"{output_video}を生成しました。")

    # EN
    output_video = os.path.join(temp_output_dir, "3_en.mp4")
    con_video_list.append(output_video)
    con_video_list.append(output_video)
    vt.speech_bubble_video(
        os.path.join(template_dir, "3_en_read.mp4"),
        os.path.join(temp_output_dir, f"{item['english']}.wav"),
        output_video,
        item["english"],
        color="black",
        after_time=0.5,
        position_y=bubble_position_y,
        english=True,
    )
    print(f"{output_video}を生成しました。")

    # Key Phrase main
    output_video = os.path.join(temp_output_dir, "4_key_phrase1.mp4")
    con_video_list.append(output_video)
    vt.introduction_key_phrase(
        os.path.join("videoTemplate/5_key_phrase.mp4"),
        os.path.join(template_dir, "todayKeyPhrase.wav"),
        output_video,
        item["key_phrase"],
        item["description"],
        color="white"
    )
    print(f"{output_video}を生成しました。")

    # Key Phrase main repeat
    output_video = os.path.join(temp_output_dir, "4_key_phrase2.mp4")
    con_video_list.append(output_video)
    con_video_list.append(output_video)
    # con_video_list.append(output_video)
    vt.introduction_key_phrase(
        os.path.join("videoTemplate/5_key_phrase2.mp4"),
        os.path.join(temp_output_dir, f"{item['key_phrase']}.wav"),
        output_video,
        item["key_phrase"],
        item["description"],
        color="white"
    )

    # Key Phrase main repeat
    output_video = os.path.join(temp_output_dir, "4_key_phrase3.mp4")
    con_video_list.append(output_video)
    # con_video_list.append(output_video)
    vt.introduction_key_phrase(
        os.path.join("videoTemplate/5_key_phrase2.mp4"),
        os.path.join(temp_output_dir, f"{item['description'].replace("\n", "")}.wav"),
        output_video,
        item["key_phrase"],
        item["description"],
        color="white"
    )

    print(f"{output_video}を生成しました。")

    # end
    output_video = os.path.join(temp_output_dir, "end.mp4")
    con_video_list.append(output_video)
    vt.copy_video(os.path.join("videoTemplate/end.mp4"), output_video)

    # すでにファイルが存在する場合は削除
    concat_path = os.path.join(temp_output_dir, "concat.mp4")
    if os.path.exists(concat_path):
        os.remove(concat_path)
    vu.concatenate_videos(con_video_list, concat_path)

    concat2_path = os.path.join(temp_output_dir, "concat2.mp4")
    vt.copy_video(concat_path, concat2_path)

    # BGMを追加
    if len(BGMS) > 0:
        print("BGMが見つかりませんでした。")
        bgm = random.choice(BGMS)
        vt.add_bgm_to_video(concat2_path, bgm, output_path)
        print(f"{output_path}を生成しました。")
    else:
        vt.copy_video(concat2_path, output_path)
        print(f"{output_path}を生成しました。")
