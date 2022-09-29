from django import forms

#商品IDの種類
IS_FINISHED_CHOICES ={
    (False, "未"),
    (True, "済"),
}

class todo_form(forms.Form):
    todo = forms.CharField(label="todo")