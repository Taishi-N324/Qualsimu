# Qualsimu

![スクリーンショット](images/logo.png) 

## 概要

Qualsimuは、量子コンピュータのデバイス周りの物理と量子力学を量子コンピュータで扱う方法についての学習帳として実現することを目指しています

公開サイト: [リンク](https://qualsimu.com/textbook/)

## 環境構築

```bash
git clone git@github.com:Taishi-N324/Qualsimu.git                   
cd Qualsimu 
pip install -r requirements.txt
```


## buildする方法
```Qualsimu```があるディレクトリから

```bash
make html
```
を実行します

```bash
cp -r source/animation/ build/html/animation
```

`build/html/index.html` をブラウザで開いてドキュメントを確認できます。

## 執筆者
本教材は未踏ターゲット事業のプロジェクトの一環として，作成されました．<br>
担当としては[鈴木泰雅](https://www.linkedin.com/in/taiga-suzuki-0a3a08251/)が第一章・第二章を担当しています．
[青木幸一](https://www.linkedin.com/in/koichi-aoki-462450276/)はまだ未公開である第三章を担当しており，[中村泰士](https://www.linkedin.com/in/taishi-nakamura/)は第三章のシミュレーションのツールの作成やサーバーの管理を行っています．

## ご質問やご意見等に関して
本教材に関してのお問い合わせはこちらの連絡先(<a href="mailto:qualsimu@gmail.com">qualsimu@gmail.com</a>)までお気軽にご連絡ください。<br>
また，本教材のアニメーションは鈴木が作成しており，[Manim](https://github.com/ManimCommunity/manim)というPythonのライブラリを用いてご要望に応じて高品質のアニメーションを作成することができます．アニメーション作成に関するご相談等は鈴木泰雅まで <a href="mailto:suzuki.t.ec@m.titech.ac.jp">こちら</a>からお気軽にご連絡ください．

## 謝辞
本サイトは, 
[IPA 2023年度未踏ターゲット事業](https://www.ipa.go.jp/jinzai/mitou/target/2023/gaiyou_ty-3.html)
の支援を受けて作成されました.
PM[徳永裕己様](https://www.rd.ntt/organization/researcher/special/s_023.html)
にプロジェクトのマネージと助言等をいただき，
TA[鈴木泰成様](https://researchmap.jp/yasunari_suzuki)
にプロジェクトの助言等に加えて教材の間違った表記等のご指摘や超伝導量子ビットに関する質問を多くさせていただきました．
また，Qiskit Advocateでおられる[Arthur Strauss様](https://www.linkedin.com/in/arthurostrauss/?locale=en_US)にコーディングに関して様々な助言をいただきました．ここに感謝の意を表します.

## ライセンス
この作品は以下のライセンスの下に提供されています:

- 文章および説明は, [クリエイティブ・コモンズ 表示 - 非営利 - 改変禁止 4.0 国際 ライセンス](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ja) の下に提供されています. 

- 作品中のコードセル部分およびアニメーションは, [MITライセンス](https://opensource.org/licenses/MIT) の下に提供されています. 

## 使用しているソフトウェアのライセンス情報
この作品には, 以下のオープンソースソフトウェアが使用されています:

- [Manim](https://github.com/ManimCommunity/manim): 数学的な図表やアニメーションを生成するためのPythonライブラリ. Manimは[MITライセンス](https://github.com/ManimCommunity/manim/blob/main/LICENSE)の下に提供されています. 

- [Manim Slides](https://github.com/jeertmans/manim-slides): Manimを使用してプレゼンテーションスライドを作成するためのツール. Manim Slidesも[MITライセンス](https://github.com/jeertmans/manim-slides/blob/main/LICENSE.md)の下に提供されています. 

- [Plotly.js](https://github.com/plotly/plotly.js): インタラクティブなグラフィックスをWeb上で作成するためのJavaScriptライブラリ. Plotly.jsは[MITライセンス](https://github.com/plotly/plotly.js/blob/master/LICENSE)の下に提供されています. 

これらのツールを使用することで, 私たちの作品で高品質なビジュアルコンテンツを提供することができました. これらのソフトウェアの開発者に感謝します. 
