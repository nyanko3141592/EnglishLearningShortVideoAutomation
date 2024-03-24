from typing import List
from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    CompositeAudioClip,
    CompositeAudioClip,
    concatenate_videoclips,
    concatenate_audioclips,
)
import os
import subprocess


def speech_bubble_video(
    input_video,
    input_audio,
    output_video,
    text,
    english=False,
    color="black",
    after_time=0.3,
    position_y=0.5,
    font_path="/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
):
    texts = text.split("\n")
    max_text = max(texts, key=len)

    audio = AudioFileClip(input_audio)
    video = VideoFileClip(input_video)
    time = audio.duration + after_time
    if time > video.duration:
        time = video.duration
    video = video.set_duration(time)
    video_width, video_height = video.size

    fontsize = 100
    max_char = 10
    if english:
        # 英語の場合はフォントサイズを大きくする
        fontsize = 80
        max_char = 20

    enter_count = len(texts)

    text_clip = TextClip(
        text + "\n",
        fontsize=fontsize,
        color=color,
        font=font_path,
        method="caption",
        size=(video_width - 200, None),
    )
    text_clip = text_clip.set_position(
        lambda t: (
            "center",
            video_height * position_y - fontsize * enter_count / 2,
        )
    )

    text_clip = text_clip.set_start(0).set_duration(time)

    video_with_text = CompositeVideoClip([video, text_clip])

    final_audio = CompositeAudioClip([video.audio, audio])

    final_clip = video_with_text.set_audio(final_audio)

    final_clip.write_videofile(output_video)


def comb_movie(movie_files, out_path):
    # 動画クリップのリストを作成
    clips = [VideoFileClip(movie) for movie in movie_files]

    # 動画クリップを結合
    final_clip = concatenate_videoclips(clips, method="compose")

    # 結合した動画を書き出し
    final_clip.write_videofile(out_path, codec="libx264", audio_codec="aac")


def introduction_key_phrase(
    input_video: str,
    input_audio: str,
    output_video: str,
    phrase: str,
    description: str,
    color: str = "black",
    after_time: int = 0.3,
    position_y: float = 0.3,
    descri_position_y: float = 0.45,
    font_path: str = "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
):
    texts = phrase

    audio = AudioFileClip(input_audio)
    video = VideoFileClip(input_video)
    time = audio.duration + after_time
    if time > video.duration:
        time = video.duration
    video = video.set_duration(time)
    video_width, video_height = video.size

    en_fontsize = 100
    description_fontsize = 80

    text_clip = TextClip(
        phrase + "\n",
        fontsize=en_fontsize,
        color=color,
        font=font_path,
        method="caption",
        size=(video_width - 100, None),
    )
    text_clip = text_clip.set_position(
        lambda t: (
            "center",
            video_height * position_y,
        )
    )
    text_clip = text_clip.set_start(0).set_duration(time)

    text_clip2 = TextClip(
        description + "\n",
        fontsize=description_fontsize,
        color=color,
        font=font_path,
        method="caption",
        size=(video_width - 100, None),
    )
    text_clip2 = text_clip2.set_position(
        lambda t: (
            "center",
            video_height * descri_position_y,
        )
    )

    text_clip2 = text_clip2.set_start(0).set_duration(time)

    video_with_text = CompositeVideoClip([video, text_clip, text_clip2])

    final_audio = CompositeAudioClip([video.audio, audio])

    final_clip = video_with_text.set_audio(final_audio)

    final_clip.write_videofile(output_video)


def copy_video(
    input_video: str,
    output_video: str,
):
    video = VideoFileClip(input_video)
    video = video.set_duration(video.duration)

    final_audio = CompositeAudioClip([video.audio])

    final_clip = video.set_audio(final_audio)

    final_clip.write_videofile(output_video)


def add_bgm_to_video(video_file, bgm_file, output_file, bgm_volume=0.1):
    # 動画ファイルとBGMファイルを読み込む
    video = VideoFileClip(video_file)
    audio = AudioFileClip(bgm_file)

    # BGMの長さを動画の長さに合わせる
    audio = audio.subclip(0, video.duration)

    # 元の動画の音声を取得し、BGMの音量を調整する
    original_audio = video.audio
    composite_audio = CompositeAudioClip([original_audio, audio.volumex(bgm_volume)])

    # 調整したBGMを動画に設定する
    final_video = video.set_audio(composite_audio)

    # 新しい動画ファイルを書き出す
    final_video.write_videofile(output_file)
