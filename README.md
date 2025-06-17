# Voice2Text

音声をテキストに変換するプロジェクトです。OpenAIのWhisperを使用して音声認識を行います。

## セットアップ

1. 仮想環境の作成と有効化:
```bash
python -m venv venv
source venv/bin/activate  # macOSの場合
```

2. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

## 使用方法

### 基本的な使い方

```bash
python transcribe.py 音声ファイルのパス
```

### オプション

- `--model`: 使用するWhisperモデルのサイズを指定
  - 選択肢: tiny, base, small, medium, large
  - デフォルト: base
  - 例: `--model small`

- `--output`: 出力CSVファイルのパスを指定
  - 指定しない場合は標準出力に表示
  - 例: `--output result.txt`

### 使用例

1. 基本的な使用:
```bash
python transcribe.py input.mp3
```

2. より高精度なモデルを使用:
```bash
python transcribe.py input.mp3 --model medium
```

3. 結果をファイルに保存:
```bash
python transcribe.py input.mp3 --output result.txt
```

## 対応フォーマット

- 音声ファイル: .mp3, .wav, .m4a など
- 動画ファイル: .mp4, .avi, .mov など

## 環境

- Python 3.x
- OpenAI Whisper
- その他必要な依存関係は `requirements.txt` に記載されています 