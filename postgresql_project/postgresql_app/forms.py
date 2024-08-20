from django import forms


class CountElementsOnPageForm(forms.Form):
    count_elements_on_page = forms.IntegerField(max_value=100,
                                                min_value=1,
                                                label="Количество элементов на странице")
