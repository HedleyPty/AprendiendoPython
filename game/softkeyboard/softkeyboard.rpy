# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       softkeyboard.rpy [ソフトキーボード関数]
#                                                                                                       作成者:  Andrea Rubenstein
#                                                                                                       作成日 : 2011/10/15
#                                                                                                       更新日: 2011/10/16
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  
init -100 python:

##############################################################################
#       関数
##############################################################################      
       
    # Alphabets for soft keyboard
    softkey = {}
    
##################################################
#　クラス名：SetAlphabet
#　説　明　：入力するアルファベットを設定する処理
##################################################     
    def SetAlphabet(type,lang=persistent.lang):
        alphabet = []
        for column in softkey[lang][type]:
            alphabet.append(column)
        
        return alphabet
        
##################################################
#　クラス名：SwithCapsSingle
#　説　明　：アルファベットの大文字と小文字の変換処理
##################################################     
    def SwitchCapsSingle(base,upper):
        switched = []
        for letter in base:
            if letter is not None:
                if upper:
                    switched.append(letter.upper())
                else:
                    switched.append(letter.lower())
                    
        return switched
        
##################################################
#　クラス名：SwitchCaps
#　説　明　：アルファベットの大文字と小文字の変換処理
##################################################     
    def SwitchCaps(base,upper):
        switched = []
        for array in base:
            switched.append(SwitchCapsSingle(array,upper))
            
        return switched
        
##################################################
#　クラス名：AddLetter
#　説　明　：文字を文字配列に入れる処理
##################################################     
    def AddLetter(base,letter):
        base = base + letter
        if len(base) > INPUT_MAX:
            base = base[:-1]
            
        return base
  
  
##################################################
#　クラス名：ShiftDown
#　説　明　：小文字にする処理
##################################################     
    def ShiftDown(base):
        if input_shift:
            return SwitchCaps(base,False)
        else:
            return base
        
#EOF
