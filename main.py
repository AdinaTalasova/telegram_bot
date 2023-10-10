from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import (
    main_menu_keyboard,
    courses_menu_keyboard,
    python_menu_keyboard,
    java_menu_keyboard,
    js_menu_keyboard,
    qa_menu_keyboard,
    go_back_keyboard
)
from key_buttons import tele_button, courses

ABOUT = tele_button[0]
COURSES = tele_button[1]
PYTHON = courses[0]
JAVA = courses[1]
JS = courses[2]
QA = courses[3]
GO_BACK = courses[4]
ADDRESS = tele_button[2]

def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'добро пожаловать {update._effective_user.username}\nэто бот поможет вам с информацией о курсах',
        reply_markup=main_menu_keyboard()
    )

def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Преимуществав  обучения в Codify · Обучение с нуля до Junior. Пройди обучение по авторской программе Codify и стань Junior специалистом.\nsite:\nhttps://www.codifylab.com/'
    )

def reply_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose courses',
        reply_markup=courses_menu_keyboard()
    )

def python_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Python — это язык программирования, который широко используется в интернет-приложениях, разработке программного обеспечения, науке о данных и машинном обучении (ML).',
        reply_markup=courses_menu_keyboard()
    )

def java_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Java — строго типизированный объектно-ориентированный язык программирования общего назначения, разработанный компанией Sun Microsystems. Разработка ведётся сообществом, организованным через Java Community Process; язык и основные реализующие его технологии распространяются по лицензии GPL',
        reply_markup=courses_menu_keyboard()
    )

def js_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'JavaScript — мультипарадигменный язык программирования. Поддерживает объектно-ориентированный, императивный и функциональный стили. Является реализацией спецификации ECMAScript. JavaScript обычно используется как встраиваемый язык для программного доступа к объектам приложений.',
        reply_markup=courses_menu_keyboard()
    )

def qa_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Тестировщик — это специалист, который занимается тестированием программного обеспечения с целью выявления ошибок и недоработок.',
        reply_markup=courses_menu_keyboard()
    )

def go_back_menu(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Вы вернулись на главное меню',
        reply_markup=main_menu_keyboard()
    )

# def address(update:Update, context:CallbackContext):
#     update.message.reply_text(
#         f'Здесь наш адрес:\nsite:https://go.2gis.com/dpfcp'
#         )
    
def address(update:Update, context:CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of Codify'
    )
    update.message.reply_location(
        #42.82909025000069, 74.61687279022618
        longitude=74.61687279022618,
        latitude=42.82909025000069,
        reply_to_message_id=msg.message_id
    )


updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVA),
    java_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(QA),
    qa_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GO_BACK),
    go_back_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ADDRESS),
    address
))

updater.start_polling()
updater.idle()
