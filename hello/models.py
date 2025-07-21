from django.db import models


class Message(models.Model):
    """
    メッセージを保存するモデル
    Hello, World!などのメッセージをデータベースに保存します
    """
    content = models.CharField(max_length=200, verbose_name="メッセージ内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    is_active = models.BooleanField(default=True, verbose_name="有効フラグ")

    class Meta:
        verbose_name = "メッセージ"
        verbose_name_plural = "メッセージ"
        ordering = ['-created_at']  # 作成日時の降順でソート

    def __str__(self):
        return self.content
