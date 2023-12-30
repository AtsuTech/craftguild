from django.db import models
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel

# ---タグ実装---
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag as TaggitTag
# ---タグ実装---

#　管理画面でタグとカテゴリ編集
from wagtail.snippets.models import register_snippet





#コンテンツの一覧のページ
class ContentsSelectingPage(Page):

    template = "contents/contents_selecting_page.html"


    #ページのタイトル
    page_title = models.CharField(
        verbose_name="ページのタイトル(ここにはコンテンツの選択画面のページの名前を入力します)",
        max_length=100,
        blank=True,
        null=True,
    )


    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        #メンターのデータを取得しpostsに格納
        posts = ContentsDetailPage.objects.live().public()

        #postsを"contents"という名前で子ページで取り扱うようにする
        context["contents"] = posts
        
        return context
    

#コンテンツの詳細のページ
class ContentsDetailPage(Page):

    #template = "mentor/mentor_detail_page.html"

    #　コンテンツのタイトル
    contents_name = models.CharField(
        verbose_name="コンテンツのタイトル",
        max_length=100,
        blank=False,
        null=False,
    )

    #　コンテンツの紹介文
    explanation = RichTextField(
        verbose_name="コンテンツの説明",
        blank=True,
        null=True,
    )

    # カバー画像
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name="カバー写真",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )


    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("contents_name"),
        FieldPanel("explanation"),
        FieldPanel("cover_image"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        categories = TextCategory.objects
        # for category in categories:
        #     blogpages = TextPage.objects.filter(tags__name=category.name)
        texts = TextPage.objects
        #texts = TextPage.get_children(self)


        #postsを"contents"という名前で子ページで取り扱うようにする
        context["categories"] = categories
        context["texts"] = texts
        
        return context

# テキストのカテゴリ
@register_snippet
class TextCategory(models.Model):
    name = models.CharField(max_length=255)
    panels = [
        FieldPanel('name'),
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "カテゴリ"
        verbose_name_plural = "categories"

# テキストのタグ
class TextPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'TextPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

# テキスト
class TextPage(Page):

    #　テキストのタイトル
    text_name = models.CharField(
        verbose_name="テキストのタイトル",
        max_length=100,
        blank=False,
        null=False,
    )

    #　テキスト本文
    body = RichTextField(
        verbose_name="テキストの説明",
        blank=True,
        null=True,
    )

    # カバー画像
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name="カバー写真",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    #　タグ
    tags = ClusterTaggableManager(
        verbose_name="タグ",
        through=TextPageTag, 
        blank=True
    )

    #　カテゴリ
    categories = ParentalManyToManyField(
        'TextCategory',
        verbose_name="カテゴリ",
        blank=True
        )

    #管理画面で編集可能にするテーブルのカラム
    content_panels = Page.content_panels + [
        FieldPanel("text_name"),
        FieldPanel("body"),
        FieldPanel("cover_image"),
        FieldPanel('tags'),
        # MultiFieldPanel([
        #     FieldPanel('tags'),
        # ], heading="タグ"),
        FieldPanel("categories"),
    ]