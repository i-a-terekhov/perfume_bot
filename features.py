# Попытка обрисовать архитектуру, добавление задач, отметка о закрытии задач, реформат и т.д.

# Каждый юзер, нажавший start заносятся в БД, одновременно статус "ожидание регистрации владельца/сотрудника":
TABLE_NAME = 'users'
REGISTRATION_TABLE = ('telegram_id', 'telegram_username', 'user_role', 'state_in_bot', 'salesperson_comment')
# 'user_role' - используется для разделения владельца, сотрудника и покупателя

# Если после приветственного сообщения бота юзер введет секретную фразу (пароль):
# обнулится его статус и юзер получит роль
# Если введенная юзером секретная фраза не соответствует ни владельцу, ни сотруднику,
# юзер снимет статус и получит роль покупателя и откроет
# # для себя меню покупателя.

# В приветственном сообщении будет кнопка, нажав на которую,
# юзер снимет статус и получит роль покупателя и откроет
# для себя меню покупателя.
# Если юзер уже зарегистрован как сотрудник, он попадет в меню выбора:
# открыть меню покупателя или открыть меню сотрудника
# Если юзер уже зарегистрован как владелец, он попадет в меню выбора:
# открыть меню покупателя, открыть меню сотрудника, или открыть меню владельца

