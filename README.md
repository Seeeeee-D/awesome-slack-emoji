# awesome-slacke-emoji
いろんなワークスペースに登録したいカスタムスタンプの置き場

## リポジトリに追加
### 手動で追加する場合
emoji/* に登録したいカスタムスタンプ(スタンプ:*.png or *.gif と 登録名: :foo:)を入れる!

### 自動で追加する場合

半自動でカスタム絵文字をダウンロードする方法を紹介する
1. `https://(workspace).slack.com/customize/emoji` を開き，ブラウザの開発者ツール>Network>XHRにある`emoji.adminList?...`を選択する.
2. 選択した`emoji.adminList?...`を右クリック>Copy>Copy response でコピーをする.

![img](docs/1.png)

3.  2でコピーしたものを`jsons/<folder_name>.json`として保存.
4. `python download.py --folder_name <folder_name>`を実行する
5. `emoji/<folder_name>`に保存される!!

## slackに追加
[Slack絵文字を一気に追加](https://qiita.com/mash76/items/88f396988278806db816)

1. GoogleChromeの拡張 「[Neutral Slack Emoji Tools](https://chrome.google.com/webstore/detail/neutral-face-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej?hl=ja)」を追加
2. 登録したいやつを一気にドーーン! (1つも追加していないと使えないから，　1つは手動で入れる)
3. 登録して欲しくないやつは×ボタンで削除
4. 登録されるよ!!

## アイコンを作りたい

1. [絵文字ジェネレーター](https://emoji-gen.ninja/)
  - 正統派アイコンジェネレータ
2. [MEGAMOJI](https://zk-phi.github.io/MEGAMOJI/)
  - 治安が悪くなりそうなジェネレータ
