# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       jp.rpy [日本語ソフトキーボード]
#                                                                                                       作成者:  Andrea Rubenstein
#                                                                                                       作成日 : 2011/10/15
#                                                                                                       更新日 : 2011/10/16
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

init -1 python:
    
##############################################################################
#       KEYS
##############################################################################     
    if persistent.lang == "jp":
        INPUT_VALUE_DEFAULT = "ビビアン"  
        INPUT_LABEL_DEFAULT = "名前を入力してください："  
        
        softkey_type = [{"hiragana" : "jp"}, {"katakana" : "jp"}, {"alphabet" : "en"}, {"symbols" : "en"}]
        
        main_buttons["default"] = "デフォルト"
        main_buttons["clear"] = "全削除"      
        main_buttons["confirm"] = "決定"

        input_nav_buttons["hiragana"] = "ひらがな"
        input_nav_buttons["katakana"] = "カタカナ"    
        input_nav_buttons["alphabet"] = "英文字"
        input_nav_buttons["symbols"] = "記号"    
    
    softkey["jp"] = {}        
    softkey["jp"]["hiragana"] = []
    softkey["jp"]["hiragana"].append([
        "あ","い","う","え","お",
        "か","き","く","け","こ",
        "さ","し","す","せ","そ",
        "た","ち","つ","て","と",
        "な","に","ぬ","ね","の",
        "は","ひ","ふ","へ","ほ",
        "ま","み","む","め","も"])
    
    softkey["jp"]["hiragana"].append([
        "や",None,"ゆ",None,"よ",
        "ら","り","る","れ","ろ",
        "わ",None,"を",None,"ん",
        None,None,None,None,None,
        "ー","～","、","。"])

    softkey["jp"]["katakana"] = []
    softkey["jp"]["katakana"].append([
        "ア","イ","ウ","エ","オ",
        "カ","キ","ク","ケ","コ",
        "サ","シ","ス","セ","ソ",
        "タ","チ","ツ","テ","ト",
        "ナ","ニ","ヌ","ネ","ノ",
        "ハ","ヒ","フ","ヘ","ホ",
        "マ","ミ","ム","メ","モ"])
    
    softkey["jp"]["katakana"].append([
        "ヤ",None,"ユ",None,"ヨ",
        "ラ","リ","ル","レ","ロ",
        "ワ",None,"ヲ",None,"ン",
        None,None,None,None,None,
        "ー","～","、","。"])


##############################################################################
#       SCREENS
############################################################################## 
if persistent.lang == "jp":
    screen input_special_type:
        tag input_special_type
        $col = key_col-2
        grid 1 col:
            if input_keyboard == "hiragana" or input_keyboard == "katakana":
                textbutton input_special["komoji"] action SetVariable("input_value", SwitchKomoji(input_value)) style "keyboard_button_special"
                textbutton input_special["dakuten"] action SetVariable("input_value", SwitchDakuten(input_value)) style "keyboard_button_special"
                textbutton input_special["handakuten"] action SetVariable("input_value", SwitchHandakuten(input_value)) style "keyboard_button_special"
                for i in range(3,col):
                    null
            elif input_keyboard == "alphabet":
                textbutton input_special["caps"] action [ToggleVariable("input_caps"),SetVariable("input_alphabet", SwitchCaps(input_alphabet,not input_caps))] style "keyboard_button_special"
                textbutton input_special["shift"] action [ToggleVariable("input_shift"),SetVariable("input_alphabet", SwitchCaps(input_alphabet,not input_shift))] style "keyboard_button_special"
                for i in range(2,col):
                    null                       
            else:
                for i in range(0,col):
                    null   
        
##############################################################################
#       FUNCTIONS
##############################################################################   
init -100 python:
    
##################################################
#　クラス名：SwitchKomoji
#　説　明　：小文字・大文字の変換処理
##################################################     
    def SwitchKomoji(base):
        if len(base) < 1:
            return base
        letter = base[-1]
        ######################
        # ひらがな
        ######################
        if letter == "あ":
            letter = "ぁ"
        elif letter == "ぁ":
            letter = "あ"
        elif letter == "い":
            letter = "ぃ"
        elif letter == "ぃ":
            letter = "い"
        elif letter == "う":
            letter = "ぅ"
        elif letter == "ぅ":
            letter = "う"
        elif letter == "え":
            letter = "ぇ"
        elif letter == "ぇ":
            letter = "え"
        elif letter == "お":
            letter = "ぉ"
        elif letter == "ぉ":
            letter = "お"            
        elif letter == "つ":
            letter = "っ"
        elif letter == "っ":
            letter = "つ"
        elif letter == "や":
            letter = "ゃ"
        elif letter == "ゃ":
            letter = "や"
        elif letter == "ゆ":
            letter = "ゅ"
        elif letter == "ゅ":
            letter = "ゆ"
        elif letter == "よ":
            letter = "ょ"
        elif letter == "ょ":
            letter = "よ"            
        elif letter == "わ":
            letter = "ゎ"
        elif letter == "ゎ":
            letter = "わ"
            
        ######################
        # カタカナ
        ######################
        if letter == "ア":
            letter = "ァ"
        elif letter == "ァ":
            letter = "ア"
        elif letter == "イ":
            letter = "ィ"
        elif letter == "ィ":
            letter = "イ"
        elif letter == "ウ":
            letter = "ゥ"
        elif letter == "ゥ":
            letter = "ウ"
        elif letter == "エ":
            letter = "ェ"
        elif letter == "ェ":
            letter = "エ"
        elif letter == "オ":
            letter = "ォ"
        elif letter == "ォ":
            letter = "オ"            
        elif letter == "ツ":
            letter = "ッ"
        elif letter == "ッ":
            letter = "ツ"
        elif letter == "ヤ":
            letter = "ャ"
        elif letter == "ャ":
            letter = "ヤ"
        elif letter == "ユ":
            letter = "ュ"
        elif letter == "ュ":
            letter = "ユ"
        elif letter == "ヨ":
            letter = "ョ"
        elif letter == "ョ":
            letter = "ヨ"            
        elif letter == "ワ":
            letter = "ヮ"
        elif letter == "ヮ":
            letter = "ワ"
            
        base = base[:-1] + letter
        
        return base

##################################################
#　クラス名：SwitchDakuten
#　説　明　：゛の変換処理
##################################################     
    def SwitchDakuten(base):
        if len(base) < 1:
            return base
        letter = base[-1]
        ######################
        # ひらがな
        ######################
        if letter == "か":
            letter = "が"
        elif letter == "が":
            letter = "か"
        elif letter == "き":
            letter = "ぎ"
        elif letter == "ぎ":
            letter = "き"
        elif letter == "く":
            letter = "ぐ"
        elif letter == "ぐ":
            letter = "く"
        elif letter == "け":
            letter = "げ"
        elif letter == "げ":
            letter = "け"
        elif letter == "こ":
            letter = "ご"
        elif letter == "ご":
            letter = "こ"            
        elif letter == "さ":
            letter = "ざ"
        elif letter == "ざ":
            letter = "さ"
        elif letter == "し":
            letter = "じ"
        elif letter == "じ":
            letter = "し"
        elif letter == "す":
            letter = "ず"
        elif letter == "ず":
            letter = "す"
        elif letter == "せ":
            letter = "ぜ"
        elif letter == "ぜ":
            letter = "せ"            
        elif letter == "そ":
            letter = "ぞ"
        elif letter == "ぞ":
            letter = "そ"
        if letter == "た":
            letter = "だ"
        elif letter == "だ":
            letter = "た"
        elif letter == "ち":
            letter = "ぢ"
        elif letter == "ぢ":
            letter = "ち"
        elif letter == "つ":
            letter = "づ"
        elif letter == "づ":
            letter = "つ"
        elif letter == "て":
            letter = "で"
        elif letter == "で":
            letter = "て"
        elif letter == "と":
            letter = "ど"
        elif letter == "ど":
            letter = "と"            
        elif letter == "は":
            letter = "ば"
        elif letter == "ば":
            letter = "は"
        elif letter == "ひ":
            letter = "び"
        elif letter == "び":
            letter = "ひ"            
        elif letter == "ふ":
            letter = "ぶ"
        elif letter == "ぶ":
            letter = "ふ"     
        elif letter == "へ":
            letter = "べ"
        elif letter == "べ":
            letter = "へ"              
        elif letter == "ほ":
            letter = "ぼ"
        elif letter == "ぼ":
            letter = "ほ"            
            
        ######################
        # カタカナ
        ######################
        if letter == "カ":
            letter = "ガ"
        elif letter == "ガ":
            letter = "カ"
        elif letter == "キ":
            letter = "ギ"
        elif letter == "ギ":
            letter = "キ"
        elif letter == "ク":
            letter = "グ"
        elif letter == "グ":
            letter = "ク"
        elif letter == "ケ":
            letter = "ゲ"
        elif letter == "ゲ":
            letter = "ケ"
        elif letter == "コ":
            letter = "ゴ"
        elif letter == "ゴ":
            letter = "コ"            
        elif letter == "サ":
            letter = "ザ"
        elif letter == "ザ":
            letter = "サ"
        elif letter == "シ":
            letter = "ジ"
        elif letter == "ジ":
            letter = "シ"
        elif letter == "ス":
            letter = "ズ"
        elif letter == "ズ":
            letter = "ス"
        elif letter == "セ":
            letter = "ゼ"
        elif letter == "ゼ":
            letter = "セ"            
        elif letter == "ソ":
            letter = "ゾ"
        elif letter == "ゾ":
            letter = "ソ"
        if letter == "タ":
            letter = "ダ"
        elif letter == "ダ":
            letter = "タ"
        elif letter == "チ":
            letter = "ヂ"
        elif letter == "ヂ":
            letter = "チ"
        elif letter == "ツ":
            letter = "ヅ"
        elif letter == "ヅ":
            letter = "ツ"
        elif letter == "テ":
            letter = "デ"
        elif letter == "デ":
            letter = "テ"
        elif letter == "ト":
            letter = "ド"
        elif letter == "ド":
            letter = "ト"            
        elif letter == "ハ":
            letter = "バ"
        elif letter == "バ":
            letter = "ハ"
        elif letter == "ヒ":
            letter = "ビ"
        elif letter == "ビ":
            letter = "ヒ"            
        elif letter == "フ":
            letter = "ブ"
        elif letter == "ブ":
            letter = "フ"    
        elif letter == "ヘ":
            letter = "ベ"
        elif letter == "ベ":
            letter = "ヘ"               
        elif letter == "ホ":
            letter = "ボ" 
        elif letter == "ボ":
            letter = "ホ"             
            
        base = base[:-1] + letter
        
        return base
        
 ##################################################
#　クラス名：SwitchHandakuten
#　説　明　：゛の変換処理
##################################################     
    def SwitchHandakuten(base):
        if len(base) < 1:
            return base
        letter = base[-1]
        ######################
        # ひらがな
        ######################      
        if letter == "は":
            letter = "ぱ"
        elif letter == "ぱ":
            letter = "は"
        elif letter == "ひ":
            letter = "ぴ"
        elif letter == "ぴ":
            letter = "ひ"            
        elif letter == "ふ":
            letter = "ぷ"
        elif letter == "ぷ":
            letter = "ふ"     
        elif letter == "へ":
            letter = "ぺ"
        elif letter == "ぺ":
            letter = "へ"              
        elif letter == "ほ":
            letter = "ぽ"
        elif letter == "ぽ":
            letter = "ほ"            
            
        ######################
        # カタカナ
        ######################
        if letter == "ハ":
            letter = "パ"
        elif letter == "パ":
            letter = "ハ"
        elif letter == "ヒ":
            letter = "ピ"
        elif letter == "ピ":
            letter = "ヒ"            
        elif letter == "フ":
            letter = "プ"
        elif letter == "プ":
            letter = "フ"     
        elif letter == "ヘ":
            letter = "ペ"
        elif letter == "ペ":
            letter = "ヘ"              
        elif letter == "ホ":
            letter = "ポ"
        elif letter == "ポ":
            letter = "ホ"            
            
        base = base[:-1] + letter
        
        return base
        
#EOF
