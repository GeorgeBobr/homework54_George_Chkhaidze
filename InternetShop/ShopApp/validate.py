def product_validate(title, price, category, image):
    errors = {}
    if not title:
        errors["title"] = "Поле обязательное"
    elif len(title) > 50:
        errors["title"] = "Максимальная длина 50 символов"

    if not price:
        errors["price"] = "Поле обязательное"
    elif len(price) > 20:
        errors["price"] = "Максимальная длина 2000 символов"

    if not category:
        errors["category"] = "Поле обязательное"
    elif len(category) > 2000:
        errors["category"] = "Максимальная длина 50 символов"

    if not image:
        errors["image"] = "Поле обязательное"
    elif len(image) > 2000:
        errors["image"] = "Максимальная длина 50 символов"

    return errors