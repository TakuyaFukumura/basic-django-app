# Django Hello World アプリ

Djangoを使用してデータベースから「Hello, World!」メッセージを取得して表示するシンプルなWebアプリケーションです。

## 概要

このアプリケーションは以下の機能を提供します：

- データベースからメッセージを取得して画面に表示
- データベースからメッセージを取得できない場合は「Error」を表示
- シンプルで拡張しやすい構造
- 日本語対応

## 機能

### 🎯 主要機能
- **メッセージ表示**: データベースから取得したメッセージを画面に表示
- **エラーハンドリング**: データベースエラー時に適切なエラーメッセージを表示
- **管理画面**: Django管理画面でメッセージの追加・編集・削除が可能

### 📱 動作例

**成功時の表示:**

![Hello World 成功時](https://github.com/user-attachments/assets/4304d1b2-79e9-4a24-9ea1-560076a8240b)

**エラー時の表示:**

![Hello World エラー時](https://github.com/user-attachments/assets/45e54753-9d2f-4952-8003-b3f74ee3325f)

## セットアップ

### 前提条件
- Python 3.8以上
- pip

### インストール手順

1. **リポジトリのクローン**
   ```bash
   git clone <repository-url>
   cd basic-django-app
   ```

2. **依存関係のインストール**
   ```bash
   pip install -r requirements.txt
   ```

3. **データベースのマイグレーション**
   ```bash
   python manage.py migrate
   ```

4. **初期データの作成**
   ```bash
   python manage.py create_initial_data
   ```

5. **開発サーバーの起動**
   ```bash
   python manage.py runserver
   ```

6. **ブラウザでアクセス**
   http://localhost:8000 にアクセスしてアプリケーションを確認

## 使用方法

### 基本操作

1. **メッセージの表示**: ルートURL（http://localhost:8000）にアクセス
2. **管理画面**: http://localhost:8000/admin でメッセージの管理が可能（管理者ユーザーが必要）

### 管理者ユーザーの作成

```bash
python manage.py createsuperuser
```

### カスタムコマンド

- `python manage.py create_initial_data`: 初期データ（Hello, World!メッセージ）を作成

## プロジェクト構造

```
basic-django-app/
├── helloworld_project/         # Djangoプロジェクト設定
│   ├── __init__.py
│   ├── settings.py            # プロジェクト設定
│   ├── urls.py               # メインURL設定
│   ├── wsgi.py
│   └── asgi.py
├── hello/                     # Helloアプリ
│   ├── models.py             # Messageモデル
│   ├── views.py              # ビューロジック
│   ├── urls.py               # アプリURL設定
│   ├── admin.py              # 管理画面設定
│   ├── templates/hello/      # テンプレート
│   │   └── index.html
│   ├── management/commands/   # カスタムコマンド
│   │   └── create_initial_data.py
│   └── migrations/           # データベースマイグレーション
├── manage.py                 # Django管理コマンド
├── requirements.txt          # Python依存関係
└── README.md                # このファイル
```

## 技術仕様

- **Framework**: Django 5.1.4
- **Database**: SQLite（開発環境）
- **Python**: 3.8+
- **Language**: 日本語対応

## 拡張可能性

このアプリケーションは以下のような拡張が容易に行えるよう設計されています：

- **新しいメッセージタイプの追加**: Messageモデルにフィールドを追加
- **認証機能の追加**: Django標準の認証システムを利用
- **API機能の追加**: Django REST Frameworkを使用してRESTful APIを構築
- **フロントエンドの強化**: React/Vue.jsなどとの連携
- **データベースの変更**: PostgreSQL、MySQL等への変更

## ライセンス

このプロジェクトは教育目的で作成されています。

## バージョン

- v1.0.0: 初期リリース - Django Hello Worldアプリケーションの基本機能実装
