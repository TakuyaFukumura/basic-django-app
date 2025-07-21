from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
import logging

# ログの設定
logger = logging.getLogger(__name__)


def index(request):
    """
    メインページのビュー
    データベースからメッセージを取得して表示します
    取得できない場合は「Error」を表示します
    """
    try:
        # データベースから有効なメッセージを取得（最新のものを1つ）
        message = Message.objects.filter(is_active=True).first()
        
        if message:
            # メッセージが見つかった場合
            context = {
                'message': message.content,
                'status': 'success'
            }
            logger.info(f"メッセージを正常に取得しました: {message.content}")
        else:
            # メッセージが見つからない場合
            context = {
                'message': 'Error',
                'status': 'error'
            }
            logger.warning("データベースにメッセージが見つかりませんでした")
    
    except Exception as e:
        # データベースエラーが発生した場合
        context = {
            'message': 'Error',
            'status': 'error'
        }
        logger.error(f"データベースエラーが発生しました: {str(e)}")
    
    return render(request, 'hello/index.html', context)
