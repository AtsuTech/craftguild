from django.shortcuts import render,redirect
from .forms import PostContactForm
from .models import ContactCategory
from django.core.mail import send_mail #メール送信処理
from django.template.loader import render_to_string #メール送信の際、txtファイルの内容を読み込みメール本文として出力

# フォームの送信処理
def post_cotact_form(request):

    if request.method == 'POST':
        form = PostContactForm(request.POST)

        if form.is_valid():

            form.save()

            #メールに送信するお問い合わせ内容のテキストを取得
            category = ContactCategory.objects.get(id=form.cleaned_data['contact_category'].id)

            """題名"""
            subject = "題名"
            
            #【本文】txtファイルを読み込み、本文として出力する
            message=render_to_string(
                "mail/mail_message.txt", 
                {
                    "child_name1":form.cleaned_data['child_name1'],
                    "child_name2":form.cleaned_data['child_name2'],
                    "parent_name1":form.cleaned_data['parent_name1'],
                    "parent_name2":form.cleaned_data['parent_name2'],
                    "email":form.cleaned_data['email'],
                    "phone_number":form.cleaned_data['phone_number'],
                    "category":category.option,
                    "comment":form.cleaned_data['comment'],
                }
            )

            """送信元メールアドレス"""
            from_email = "example@example.com"
            """宛先メールアドレス"""
            recipient_list = [
                form.cleaned_data['email']
            ]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)


            return redirect('/contact/complete')  # 保存後、一覧ページにリダイレクトするように変更

    else:
        form = PostContactForm()

    #ここは、エラーの時の処理
    request.session['post_error2'] = True
    return redirect('/contact')
    


# 送信完了画面
def post_complete(request):
    return render(request, 'contact_form/contact_complete.html')