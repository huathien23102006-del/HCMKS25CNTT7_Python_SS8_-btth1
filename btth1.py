username = ""
title = ""
description = ""
hashtags = ""

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK =====")
    print("1. Nhập và phân tích thông tin video")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra tính hợp lệ của hashtag")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")

    choice = input("\nMời bạn chọn chức năng (1-5): ")

    # Bẫy 4
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    # Bẫy 3
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    # ==========================
    # Chức năng 1
    # ==========================
    if choice == 1:

        username = input("Nhập tên tài khoản: ")

        # Bẫy 1
        if username.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        title = input("Nhập tiêu đề video: ")

        description = input("Nhập mô tả video: ")

        # Bẫy 2
        if description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        hashtags = input(
            "Nhập danh sách hashtag (cách nhau bởi dấu phẩy): "
        )

        username = username.strip()
        title = title.strip().title()
        description = description.strip()
        hashtags = hashtags.strip()

        print("\n===== BÁO CÁO THỐNG KÊ =====")

        print("Tên tài khoản:", username)

        print("Tiêu đề:", title)

        print("Mô tả:", description)

        print("Độ dài mô tả video:", len(description))

        print("Số lượng từ trong mô tả:",
              len(description.split()))

        print("Danh sách hashtag:",
              hashtags)

        if hashtags == "":
            print("Số lượng hashtag: 0")
        else:
            print("Số lượng hashtag:",
                  hashtags.count(",") + 1)

        print("Mô tả chữ thường:")
        print(description.lower())

        print("Mô tả chữ hoa:")
        print(description.upper())

    # ==========================
    # Chức năng 2
    # ==========================
    elif choice == 2:

        if username == "":
            username = input("Nhập tên tài khoản: ")

        print("Tên tài khoản ban đầu:", username)

        new_username = username.strip().lower()

        if not new_username.startswith("@"):
            new_username = "@" + new_username

        print("Tên tài khoản sau chuẩn hóa:",
              new_username)

    # ==========================
    # Chức năng 3
    # ==========================
    elif choice == 3:

        hashtag = input(
            "Nhập hashtag cần kiểm tra: "
        ).strip()

        if hashtag == "":
            print("Hashtag không được rỗng")

        elif not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")

        elif " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")

        elif len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")

        elif not hashtag[1:].replace("_", "").isalnum():
            print("Hashtag chỉ được chứa chữ cái, chữ số hoặc dấu gạch dưới")

        else:
            print("Hashtag hợp lệ")

            if hashtags == "":
                hashtags = hashtag
            else:
                hashtags = hashtags + "," + hashtag

            print("Đã thêm hashtag vào danh sách hiện tại")

    # ==========================
    # Chức năng 4
    # ==========================
    elif choice == 4:

        if description == "":
            print("Chưa có mô tả video để tìm kiếm")
            continue

        keyword = input(
            "Nhập từ khóa cần tìm: "
        )

        replacement = input(
            "Nhập từ khóa thay thế: "
        )

        count = description.count(keyword)

        if count > 0:

            description = description.replace(
                keyword,
                replacement
            )

            print("Số lần xuất hiện:",
                  count)

            print("Mô tả sau khi thay thế:")
            print(description)

        else:
            print("Không tìm thấy từ khóa trong mô tả video")

    # ==========================
    # Chức năng 5
    # ==========================
    elif choice == 5:
        print("Thoát chương trình")
        break