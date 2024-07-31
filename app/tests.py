from django.test import TestCase, Client
from django.urls import reverse
from .forms import WalletForm
from unittest.mock import patch

class WalletFormTest(TestCase):
    def test_wallet_form_valid(self):
        """
        Тестирование формы с валидными данными.
        """
        form_data = {'wallet_address': 'EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG'}
        form = WalletForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_wallet_form_invalid(self):
        """
        Тестирование формы с невалидными данными.
        """
        form_data = {'wallet_address': ''}
        form = WalletForm(data=form_data)
        self.assertFalse(form.is_valid())

class WalletBalanceViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    @patch('app.views.get_wallet_balance')
    def test_index_view_get(self, mock_get_wallet_balance):
        """
        Тестирование GET запроса к представлению.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
        self.assertContains(response, 'Введите адрес кошелька')

    @patch('app.views.get_wallet_balance')
    def test_index_view_post_valid(self, mock_get_wallet_balance):
        """
        Тестирование POST запроса с валидными данными.
        """
        mock_get_wallet_balance.return_value = {
            'balance': 41.24,
            'last_activity': '26.09.2024 14:24',
            'status': 'active',
            'wallet_address': 'EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG'
        }
        form_data = {'wallet_address': 'EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
        self.assertContains(response, 'Баланс: 41.24 TON')
        self.assertContains(response, 'Последняя активность: 26.09.2024 14:24')
        self.assertContains(response, 'Статус: active')

    @patch('app.views.get_wallet_balance')
    def test_index_view_post_valid(self, mock_get_wallet_balance):
        """
        Тестирование POST запроса с валидными данными.
        """
        mock_get_wallet_balance.return_value = {
            'balance': 41.24,
            'last_activity': '26.09.2024 14:24',
            'status': 'active',
            'wallet_address': 'EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG'
        }
        form_data = {'wallet_address': 'EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
        self.assertContains(response, 'Баланс: 41.24 TON')
        self.assertContains(response, 'Последняя активность: 26.09.2024 14:24')
        self.assertContains(response, '<span class="badge badge-success">active</span>', html=True)

    @patch('app.views.get_wallet_balance')
    def test_index_view_post_api_error(self, mock_get_wallet_balance):
        """
        Тестирование POST запроса с ошибкой API.
        """
        mock_get_wallet_balance.side_effect = Exception('Ошибка API')
        form_data = {'wallet_address': 'EQBvW8Z5huBkMJYdnfAEM5JqTNkuWX3diqYENkWsIL0XggGG'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
        self.assertContains(response, 'Ошибка API')