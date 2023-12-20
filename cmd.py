#!/usr/bin/env python3

import os
import subprocess

def welcome_message():
    print("made in Earth. nobuyoshi-liu")
    print("Linux commandの検索エンジンを目指して作成しました。")
    print("このプログラムは、Linuxのコマンドを検索してマニュアルを表示します。")
    print("検索したコマンドの一文字でもキーワードに入れると、後に表示される表から選択します。")
    print("プログラムの終了: Ctrl+C\n")

def search_commands(keyword):
    command_list = [command for command in os.listdir('/usr/bin') if keyword.lower() in command.lower()]
    return command_list

def display_commands(commands):
    if not commands:
        print("コマンドが見つかりませんでした。")
        return

    print("検索結果:")
    for i, command in enumerate(commands, start=1):
        print(f"{i}. {command}")
    
    print()

def show_manual(command):
    os.environ['LANG'] = 'ja_JP.UTF-8'
    try:
        subprocess.run(["man", command], check=True)
    except subprocess.CalledProcessError:
        print(f"コマンド '{command}' のマニュアルが見つかりませんでした。")

def main():
    welcome_message()
    keyword = input("検索キーワードを入力してください: ")

    commands = search_commands(keyword)

    if len(commands) == 1:
        selected_command = commands[0]
        print(f"\n直接マニュアルを表示: {selected_command}\n")
        show_manual(selected_command)
        return

    display_commands(commands)

    try:
        choice = int(input("\n選択したいコマンドの番号を入力してください: "))
        selected_command = commands[choice - 1]

        print(f"\n選択したコマンド: {selected_command}")

        print("\nマニュアルの閲覧中の操作 ")
        print("↓キー: 下にスクロール, ↑キー: 上にスクロール,")
        print("/: マニュアル内でのキーワード検索.Enterで検索開始")
        print("n: 次の一致,N: 前の一致, q: 検索終了")
        print('終了する場合はqで完全に終了します。')
        input("Press Enter to continue...")

        show_manual(selected_command)

    except (ValueError, IndexError):
        print("無効な選択です。プログラムを終了します。")

if __name__ == "__main__":
    main()

