import logging
import os


logger = logging.getLogger(__name__)
if os.path.exists("masks.log"):
    os.unlink("masks.log")
file_handler = logging.FileHandler("masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_hide(card: str) -> str:
    """
    Функция получает номер карты, маскируя все символы, кроме первых 6 и последних 4.
    :param card: Номер карты
    :return: Отформатированную строку
    """
    mask_logger = logging.getLogger(__name__)
    if len(card.replace(" ", "")) != 16:
        mask_logger.error("Введенная карта не соответствует стандарту")
        return "Некорректно введенные данные"
    mask_logger.info(f"{card[:4]} {card[4:6]}** **** {card[-4:]}")
    return f"{card[:4]} {card[4:6]}** **** {card[-4:]}"


def get_bill(bill: str) -> str:
    """
    Функция получает номер счета, макскируя все символы, кроме последних 4
    :param bill: Номер счета
    :return: Отформатированную строку с маскировкой
    """
    if len(bill.replace(" ", "")) != 20:
        logger.error("Введенный счет не соответствует стандарту")
        return "Некорректно введенные данные"
    logger.info(f"**{bill[-4:]}")
    return f"**{bill[-4:]}"
