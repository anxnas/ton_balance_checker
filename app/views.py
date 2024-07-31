import requests
from django.shortcuts import render
from .forms import WalletForm
from datetime import datetime


def get_wallet_balance(wallet_address: str):
    """
    Получает баланс кошелька и информацию о последней активности.

    :param wallet_address: Адрес кошелька TON
    :return: Словарь с балансом, последней активностью и статусом кошелька
    """
    # URL API TonCenter для получения информации о кошельке
    base_url = 'https://toncenter.com/api/v2/jsonRPC'
    params = {
        'id': 1,
        'jsonrpc': '2.0',
        'method': 'getAddressInformation',
        'params': {
            'address': wallet_address
        }
    }

    # Выполнение запроса к API TonCenter
    response = requests.post(base_url, json=params)

    if response.status_code == 200:
        data = response.json()
        if 'result' in data:
            balance = int(data['result']['balance'])
            status = 'active' if data['result']['state'] == 'active' else 'inactive'

            # Дополнительный запрос для получения последней транзакции
            tx_url = f'https://toncenter.com/api/v2/getTransactions?address={wallet_address}&limit=1&to_lt=0&archival=true'
            tx_response = requests.get(tx_url)

            if tx_response.status_code == 200:
                tx_data = tx_response.json()
                if 'result' in tx_data and len(tx_data['result']) > 0:
                    # Преобразование utime в формат ДД.ММ.ГГ ЧЧ.ММ
                    utime = tx_data['result'][0]['utime']
                    last_activity = datetime.fromtimestamp(utime).strftime('%d.%m.%Y %H:%M')
                else:
                    last_activity = 'Нет данных'
            else:
                last_activity = 'Ошибка получения транзакции'

            return {
                'balance': balance / 1_000_000_000,  # Конвертация nanoTON в TON
                'last_activity': last_activity,
                'status': status
            }
        else:
            raise Exception(f"Ошибка в ответе API: {data}")
    else:
        raise Exception(f"Ошибка запроса: {response.status_code}")


def index(request):
    """
    Обрабатывает запросы к главной странице, отображает форму и результаты.

    :param request: HTTP запрос
    :return: HTTP ответ с отрендеренным шаблоном
    """
    balance_info = None
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            wallet_address = form.cleaned_data['wallet_address']
            try:
                balance_info = get_wallet_balance(wallet_address)
                balance_info['wallet_address'] = wallet_address
            except Exception as e:
                balance_info = {'error': str(e)}
    else:
        form = WalletForm()

    return render(request, 'app/index.html', {'form': form, 'balance_info': balance_info})