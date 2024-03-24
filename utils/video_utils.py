import os
import subprocess


def concatenate_videos(video_files, output_file):
    # 一時的なテキストファイルを作成し、動画ファイルのリストを書き込む
    with open("video_list.txt", "w") as file:
        for video in video_files:
            file.write(f"file '{video}'\n")

    # ffmpegコマンドを実行して動画を結合
    subprocess.call(
        [
            "ffmpeg",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            "video_list.txt",
            "-c",
            "copy",
            output_file,
        ]
    )

    # 一時的なテキストファイルを削除
    os.remove("video_list.txt")

    print(f"動画の結合が完了しました。出力ファイル: {output_file}")


if __name__ == "__main__":
    # 使用例
    video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]
    output_file = "output.mp4"
    concatenate_videos(video_files, output_file)
