from aiogram import Dispatcher
from handlers import start, balance, transactions, wallet


def register_all_handlers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(balance.router)
    dp.include_router(transactions.router)
    dp.include_router(wallet.router)
