#戻り値："グー","チョキ","パー"
def player_pon():
    hands_dic = {1: "グー", 2: "チョキ", 3: "パー"}
    print("1. グー  2. チョキ  3. パー")
    player_hand = int(input("グー、チョキ、パーの番号を入力してください："))
    while player_hand not in hands_dic.keys():
        print("不正な入力です。もう一度入力してください。")
        player_hand = int(input("グー、チョキ、パーの番号を入力してください："))

    return hands_dic[player_hand]
