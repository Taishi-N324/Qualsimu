```{image} images/表紙.png
:width: 80%
:align: center
```
<br>

```{admonition} 注意点
:class: warning

説明が不足している箇所・誤って記載している箇所等が存在する可能性がありますのでご了承ください．
```

# はじめに
量子コンピュータが様々な産業で応用され始めています．それにともないより多くの分野の方にとって量子コンピュータを学ぶ需要が高まっています．しかし，量子コンピュータを学び，実際に応用できるようになることはそう簡単ではありません．<br>
量子コンピュータを深く理解して実際に応用ができるレベルまで達するためには
- 量子コンピュータの仕組み
- 量子コンピュータの情報処理としての応用

を学ぶ必要があります．仮にどちらかの知識が抜けてしまうと

- (物理に慣れ親しんだ方)「そもそもこんなもの制御できるのか？」
- (情報に慣れ親しんだ方)「そもそもビットという情報の**概念**が**重ね合わせられる**とはどういうこと？」

といった疑問が生じることでしょう．そこで我々はより理解がしやすいようにビジュアル・アニメーションなどを豊富に設置し量子コンピュータの情報と物理との橋渡しができるような教材を作成しました．<br>

また，量子コンピュータの仕組みをより深く理解するには量子力学全般の知識が必要になります．我々は逆に量子コンピュータを使うことで新しい量子力学の学び方が提案できるのではないか？と考えています．

量子コンピュータは量子力学の性質を利用したコンピュータです．我々はこの量子コンピュータで量子力学をシミュレーションして見せることで，読者が「量子力学を量子力学で実験している」体験ができ，より量子力学を身近に，受け入れやすく感じられるでしょう．<br>
そこで我々はこの考えのもと，本教材の第三章にて量子力学を量子コンピュータで実験をする「量子ダイナミクスシミュレーション」の章を設けています．

## 表記
本教材は以下のルールで表記を分けています．
```{admonition} 初学者がひっかかりやすいポイント
:class: tip, dropdown

この中を見ると初学者が躓きやすいポイントやその解説が書かれています．
```

```{admonition} もっと知りたい人のために
:class: dropdown

こちらにはややアドバンストなことが書いてあります．
```

```{admonition} 概念
:class: note

こちらには重要な概念や事項をまとめています．
```

他にも「重要」マークや「注釈」マークがあります．

## 前提とする知識

線形代数の知識を必要とし，量子力学の理解があるとより深く理解ができます.              

それに伴い，この教材の対象ユーザーは，
**学部1,2年の物理学徒と情報学徒，また，少しでも量子コンピュータの原理に興味がある方**
になっています．

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


## 関連する量子教材とコンテスト
本教材以外にも量子コンピュータの学習と発展に貢献する未踏ターゲット事業の成果が発表されています．その例として以下があります．

- [QCoder-2023年度IPA未踏ターゲット事業](https://www.qcoder.jp/)
- [QookBook-2023年度IPA未踏ターゲット事業](https://www.qookbook.net/)

## 目次

```{toctree}
:maxdepth: 1
:caption: 第1章 量子コンピュータの基礎

notebooks/section1/basics
notebooks/section1/Quantum_Mechanics/index
notebooks/section1/Quantum_information/index
```

```{toctree}
:maxdepth: 1
:caption: 第2章 超伝導量子コンピューターが動く仕組み
notebooks/section2/superconducting2
notebooks/section2/0_1_representation/index
notebooks/section2/quantum_gate/index

```

```{toctree}
:maxdepth: 3
notebooks/references
```