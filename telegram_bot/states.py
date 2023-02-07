from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    start = State()
    language = State()
    contact = State()
    verification = State()
    main_menu = State()
    settings = State()
    change_language = State()
    contact_us = State()
    write_consultant = State()
    
