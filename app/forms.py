from django import forms

class WalletForm(forms.Form):
    """
    Форма для ввода адреса кошелька TON.
    """
    wallet_address = forms.CharField(
        label='Введите адрес кошелька',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите адрес кошелька...'})
    )