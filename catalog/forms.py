from django import forms
from django.core.exceptions import ValidationError
from .models import Product
import imghdr

BANNED_WORDS = (
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
)

MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_IMAGE_FORMATS = ("jpeg", "png", "jpg")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "category": forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css = "form-control"
            if isinstance(field.widget, (forms.CheckboxInput,)):
                css = "form-check-input"
                field.widget.attrs["class"] = css
            else:
                field.widget.attrs["class"] = css
        if "price" in self.fields:
            self.fields["price"].widget.attrs.update({"placeholder": "0.00", "step": "0.01"})

    def _check_banned_words(self, value, field_label):
        if not value:
            return
        lower = value.lower()
        found = [w for w in BANNED_WORDS if w in lower]
        if found:
            raise ValidationError(
                f"Поле '{field_label}' содержит запрещённые слова: {', '.join(found)}."
            )

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        self._check_banned_words(name, "Название")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        self._check_banned_words(description, "Описание")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None:
            return price
        try:
            if price < 0:
                raise ValidationError("Цена не может быть отрицательной.")
        except TypeError:
            raise ValidationError("Некорректное значение цены.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image
        if hasattr(image, "size") and image.size > MAX_IMAGE_SIZE:
            raise ValidationError("Файл изображения слишком большой (макс. 5 МБ).")
        try:
            image.open()
            header = image.read(512)
            image.seek(0)
            fmt = imghdr.what(None, h=header)
        except Exception:
            fmt = None
        if fmt is None:
            content_type = getattr(image, "content_type", "")
            if "jpeg" in content_type or "jpg" in content_type:
                fmt = "jpeg"
            elif "png" in content_type:
                fmt = "png"
        if fmt not in ALLOWED_IMAGE_FORMATS:
            raise ValidationError("Поддерживаются только форматы JPEG и PNG.")
        return image
