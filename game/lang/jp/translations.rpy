# 漢字コードは UTF-8 を使用してください。

# This file contains a list of all of the phrases you can translate
# from the Ren'Py common code.
# このファイルは、Ren'Pyの共通コードにある翻訳可能な全フレーズを含んでいます。（訳注：実際には中途です）

init:
    if persistent.lang == "jp":
        # 日本語フォント指定
        # 日本語TTFファイルを用意し、gameディレクトリー（このファイルと同じディレクトリー）に
        # 設置してください。
        # フリーの日本語TTFファイルとしてはVLゴシックフォントファミリ (http://dicey.org/vlgothic/) や
        # みかちゃんフォント (http://www001.upp.so-net.ne.jp/mikachan/) などがあります。
        $ style.default.font = "lang/jp/VL-PGothic-Regular.ttf"
        
        #  改行・禁則処理の日本語対応
        $ style.default.language = "eastasian"
    
init python:
    if persistent.lang == "jp":
        
        # メニューで言語を切り替える選択肢
        config.translations[u'Language'] = u'言語'
        
        # Translatable strings found in common/00developer.rpy
        # common/00developer.rpyの翻訳テーブル
    
        config.translations[u'Developer Menu'] = u'開発者用メニュー'
        config.translations[u'Return to the developer menu'] = u'開発者用メニューに戻る'
    
        # Translatable strings found in common/00library.rpy
        # common/00library.rpyの翻訳テーブル
    
        config.translations[u'Skip Mode'] = u'スキップモード'
        config.translations[u'Fast Skip Mode'] = u'高速スキップモード'
        config.translations[u"While Ren'Py games may be playable without the renpy module, some features may be disabled. For more information, read the module/README.txt file or go to http://www.bishoujo.us/renpy/."] = u"Ren'Pyを用いて作成されたゲームはrenpyモジュールなしでも実行することが可能ですが、一部の機能は使用することができません。詳細は module/README.txt を参照するか、http://www.bishoujo.us/renpy/ にアクセスしてください。"
        config.translations[u'renpy module not found.'] = u'renpyモジュールが見つかりません。'
        config.translations[u'The renpy module could not be loaded on your system.'] = u'renpyモジュールをロードすることができませんでした。'
        config.translations[u'Old renpy module found.'] = u'古いrenpyモジュールが見つかりました。'
        config.translations[u"An old version (%d) of the Ren'Py module was found on your system, while this game requires version %d."] = u"Ren'Pyモジュールの古いバージョン (%d) が見つかりましたが、このゲームが使用するバージョンは %d です。"
        config.translations[u'Please click to continue.'] = u'クリックして続けてください。'
    
        # Translatable strings found in common/00menus.rpy
        # common/00menus.rpyの翻訳テーブル
    
        config.translations[u'Start Game'] = u'はじめから'
        config.translations[u'Load Game'] = u'続きから'
        config.translations[u'Preferences'] = u'環境設定'
        config.translations[u'Help'] = u'ヘルプ'
        config.translations[u'Quit'] = u'終了'
        config.translations[u'Return'] = u'戻る'
        config.translations[u'Save Game'] = u'セーブ'
        config.translations[u'Main Menu'] = u'メインメニュー'
        config.translations[u'Are you sure you want to quit?'] = u'本当に終了しますか？'
        config.translations[u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'] = u'本当にメインメニューに戻りますか？\n未セーブのデータが失われてしまいます'
    
        # Translatable strings found in common/_layout/one_column_preferences.rpym
        # common/_layout/one_column_preferences.rpymの翻訳テーブル
    
        config.translations[u'Display'] = u'表示'
        config.translations[u'Transitions'] = u'切り替え'
        config.translations[u'Skip'] = u'メッセージスキップ'
        config.translations[u'Begin Skipping'] = u'スキップ開始'
        config.translations[u'After Choices'] = u'選択肢の後'
        config.translations[u'Text Speed'] = u'メッセージ表示速度'
        config.translations[u'Auto-Forward Time'] = u'自動進行速度'
        config.translations[u'Music Volume'] = u'BGMボリューム'
        config.translations[u'Sound Volume'] = u'効果音ボリューム'
        config.translations[u'Voice Volume'] = u'音声ボリューム'
        config.translations[u'Joystick...'] = u'ジョイスティック...'
    
        # Translatable strings found in common/_layout/classic_yesno_prompt.rpym
        # common/_layout/classic_yesno_prompt.rpymの翻訳テーブル
    
        config.translations[u'Yes'] = u'はい'
        config.translations[u'No'] = u'いいえ'
    
        # Translatable strings found in common/_layout/scrolling_load_save.rpym
        # common/_layout/scrolling_load_save.rpymの翻訳テーブル
    
        config.translations[u'Empty Slot.'] = u'空きスロット'
        config.translations[u'Are you sure you want to overwrite your save?'] = u'セーブデータを上書きしますか？'
        config.translations[u'Loading will lose unsaved progress.\nAre you sure you want to do this?'] = u'未セーブのデータが破棄されます。\nデータをロードしますか？'
        config.translations[u'q'] = u'q'
        config.translations[u'a'] = u'a'
    
        # Translatable strings found in common/_layout/classic_joystick_preferences.rpym
        # common/_layout/classic_joystick_preferences.rpymの翻訳テーブル
    
        config.translations[u'Not Assigned'] = u'未割り当て'
        config.translations[u'Joystick Mapping'] = u'ジョイスティック割り当て'
        config.translations[u'Left'] = u'左'
        config.translations[u'Right'] = u'右'
        config.translations[u'Up'] = u'上'
        config.translations[u'Down'] = u'下'
        config.translations[u'Select/Dismiss'] = u'Select/Dismiss'
        config.translations[u'Rollback'] = u'表示済みメッセージを見る'
        config.translations[u'Hold to Skip'] = u'スキップ'
        config.translations[u'Toggle Skip'] = u'スキップモードに切り替え'
        config.translations[u'Hide Text'] = u'メッセージをを隠す'
        config.translations[u'Menu'] = u'メニュー'
        config.translations[u'Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping.'] = u'ジョイスティックの押したボタンに割り当て。マウスクリックで解除'
    
        # Translatable strings found in common/_layout/classic_preferences_common.rpym
        # common/_layout/classic_preferences_common.rpymの翻訳テーブル
    
        config.translations[u'Test'] = u'テスト'
        config.translations[u'Window'] = u'ウィンドウ表示'
        config.translations[u'Fullscreen'] = u'全画面表示'
        config.translations[u'All'] = u'全て'
        config.translations[u'Some'] = u'一部'
        config.translations[u'None'] = u'なし'
        config.translations[u'Seen Messages'] = u'表示済みメッセージ'
        config.translations[u'All Messages'] = u'全メッセージ'
        config.translations[u'Stop Skipping'] = u'スキップモード中止'
        config.translations[u'Keep Skipping'] = u'スキップモード継続'
    
        # Translatable strings found in common/_layout/classic_load_save.rpym
        # common/_layout/classic_load_save.rpymの翻訳テーブル
    
        config.translations[u'Auto'] = u'自動'
        config.translations[u'Quick'] = u'クイックセーブ'
        config.translations[u'Previous'] = u'前へ'
        config.translations[u'Next'] = u'次へ'
    
        # Translatable strings found in common/_compat/gamemenu.rpym
        # common/_compat/gamemenu.rpymの翻訳テーブル
    
        config.translations[u'The error message was:'] = u'エラーは以下のとおりです:'
        config.translations[u'You may want to try saving in a different slot, or playing for a while and trying again later.'] = u'異なるスロットにセーブするか、またしばらくした後に試してください'
        config.translations[u'Save Failed.'] = u'セーブに失敗しました'
    
        # Translatable strings found in common/_compat/preferences.rpym
        # common/_compat/preferences.rpymの翻訳テーブル
    
        config.translations[u'Joystick Configuration'] = u'ジョイスティックの設定'
    
        # Translatable strings found in common/_compat/mainmenu.rpym
        # common/_compat/mainmenu.rpymの翻訳テーブル
    
        config.translations[u'Continue Game'] = u'ゲームを続ける'