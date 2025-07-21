"""
初期データを作成するDjangoコマンド
"""
from django.core.management.base import BaseCommand
from hello.models import Message


class Command(BaseCommand):
    help = 'データベースに初期メッセージを作成します'

    def handle(self, *args, **options):
        # 既存のメッセージを確認
        existing_message = Message.objects.filter(content="Hello, World!").first()
        
        if not existing_message:
            # Hello, World!メッセージを作成
            message = Message.objects.create(
                content="Hello, World!",
                is_active=True
            )
            self.stdout.write(
                self.style.SUCCESS(f'メッセージ「{message.content}」を正常に作成しました')
            )
        else:
            self.stdout.write(
                self.style.WARNING('メッセージ「Hello, World!」は既に存在します')
            )
