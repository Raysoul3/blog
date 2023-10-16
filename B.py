blog_posts = []


def add_post(title, content):
    post = {"title": title, "content": content}
    blog_posts.append(post)
    print("ブログ投稿が追加されました")


def show_posts():
    if not blog_posts:
        print("現在のブログ投稿がありません")
    else:
        for i, post in enumerate(blog_posts, 1):
            print(f"投稿番号:{i}")
            print(f"タイトル:{post['title']}")
            print(f"内容:{post['content']}")


def delete_post(post_number):
    if post_number >= 1 and post_number <= len(blog_posts):
        deleted_post = blog_posts.pop(post_number - 1)
        print("ブログ投稿が削除されました")
    else:
        print("無効な投稿番号")


while True:
    print("\n操作を選択してください:")
    print("1.ブログ投稿を追加")
    print("2.ブログ投稿を表示")
    print("3.ブログ投稿を削除")
    print("4.終了")

    choice = input("選択:")

    if choice == "1":
        title = input("タイトルを入力:")
        content = input("内容を入力:")
        add_post(title, content)

    elif choice == "2":
        show_posts()

    elif choice == "3":
        post_number = int(input("削除する投稿番号を入力:"))
        delete_post(post_number)

    elif choice == "4":
        print("アプリケーションを終了します。")

    else:
        print("無効な選択です。")
