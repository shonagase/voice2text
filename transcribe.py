import whisper
import argparse
from pathlib import Path
import csv
import json
from datetime import datetime

def transcribe_audio(file_path: str, model_name: str = "base") -> dict:
    """
    音声または動画ファイルをテキストに変換します。
    
    Args:
        file_path (str): 入力ファイルのパス
        model_name (str): Whisperモデルのサイズ（tiny, base, small, medium, large）
    
    Returns:
        dict: 変換結果（テキストとセグメント情報を含む）
    """
    # モデルの読み込み
    print(f"モデル {model_name} を読み込んでいます...")
    model = whisper.load_model(model_name)
    
    # ファイルの存在確認
    if not Path(file_path).exists():
        raise FileNotFoundError(f"ファイルが見つかりません: {file_path}")
    
    # 音声認識の実行
    print("音声認識を開始します...")
    result = model.transcribe(file_path)
    
    return result

def save_to_csv(result: dict, output_path: str):
    """
    認識結果をCSVファイルに保存します。
    
    Args:
        result (dict): Whisperの認識結果
        output_path (str): 出力CSVファイルのパス
    """
    # ファイル名から拡張子を除いた部分を取得
    base_name = Path(output_path).stem
    
    # タイムスタンプを生成
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # CSVファイル名を生成
    csv_filename = f"{base_name}_{timestamp}.csv"
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # ヘッダーを書き込み
        writer.writerow(['開始時間', '終了時間', 'テキスト'])
        
        # セグメントごとの情報を書き込み
        for segment in result['segments']:
            writer.writerow([
                f"{segment['start']:.2f}",
                f"{segment['end']:.2f}",
                segment['text'].strip()
            ])
    
    print(f"結果を {csv_filename} に保存しました")

def main():
    parser = argparse.ArgumentParser(description="音声・動画ファイルをテキストに変換します")
    parser.add_argument("file_path", help="入力ファイルのパス")
    parser.add_argument("--model", default="base", choices=["tiny", "base", "small", "medium", "large"],
                      help="使用するWhisperモデルのサイズ（デフォルト: base）")
    parser.add_argument("--output", help="出力CSVファイルのパス（指定しない場合は標準出力に表示）")
    
    args = parser.parse_args()
    
    try:
        # 音声認識の実行
        result = transcribe_audio(args.file_path, args.model)
        
        # 結果の出力
        if args.output:
            save_to_csv(result, args.output)
        else:
            # デフォルトの出力ファイル名を生成
            default_output = Path(args.file_path).stem + "_transcription"
            save_to_csv(result, default_output)
            
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main() 