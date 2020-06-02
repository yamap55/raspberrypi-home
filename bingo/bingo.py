import random
import subprocess

JSAY_PATH = "/home/yamap55/raspberrypi-home/script/util/jsay.sh"


def get_column_name(n: int):
    return "BINGO"[n // 15]


def say(message: str):
    r = subprocess.run([JSAY_PATH, message])
    print()  # jsayは改行されないので可読性のため改行を入れる
    return r


target_list = random.sample(range(1, 76), 75)
output_list = []
while target_list:
    input_ = input('エンターで次の数値、"a"で出た数値を表示、数値で出たか確認')
    if input_ == "a":
        sorted_list = sorted(output_list, key=lambda x: int(x))
        print(sorted_list)
        say(" ".join(sorted_list))
    if input_ == "end":
        say("ビンゴ終わり！おめでとうございます。")
        break
    elif input_.isdigit():
        a = "でています" if input_ in output_list else "でていません"
        say(f"{input_} は {a}")
    else:
        num = target_list.pop()
        output_list.append(str(num))
        message = f"{str(get_column_name(num))} の {str(num)}"

        say(message)
        say(message)
