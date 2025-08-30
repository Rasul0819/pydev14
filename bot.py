from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command

from my_btns import main_menu,reg_menu

from datas import save_user,show_users

api = '7701095707:AAF2vlJl3TXnob7UDh8RfKfsPhtu31tbWto'
proxy_url =  "http://proxy.server:3128/"
bot = Bot(api,proxy=proxy_url)
dp=Dispatcher()


class RegState(StatesGroup):
    ati = State()
    phone_num = State()
    adress = State()


@dp.message(Command('start'))
async def send_hi(sms:types.Message):
    users = await show_users()
    for i in users:
        if sms.from_user.id in i:
            await sms.answer(text='OO jora qalay.',
                             reply_markup=main_menu)
            break
    else:   
        await sms.answer(text='Salem',
                        reply_markup=reg_menu
                        )

@dp.message(F.text=='Registration')
async def start_reg(sms:types.Message,state:FSMContext):
    await sms.answer(text='OOO, jana qollaniwshi. bizge atinizdi jazin:')
    await state.set_state(RegState.ati)

@dp.message(RegState.ati)
async def save_name(sms:types.Message,state:FSMContext):
    await state.update_data(ati=sms.text)
    await sms.answer(text='Zor, endi bizge telefon nomerinizdi jazip qaldirin:')
    await state.set_state(RegState.phone_num)

@dp.message(RegState.phone_num)
async def save_phon(sms:types.Message,state:FSMContext):
    if  not sms.text.isdigit() or len(sms.text)<9:
        await sms.answer(text='Siz qate jazdiniz')
        await sms.answer(text='Jane bir urinip korin')
    else:
        await state.update_data(phone=sms.text)
        await sms.answer(text='Aqirgisi, endi bizge adresinizdi jazip qaldirin:')
        await state.set_state(RegState.adress)

@dp.message(RegState.adress)
async def save_adress(sms:types.Message,state:FSMContext):
    await state.update_data(adress=sms.text)
    datas = await state.get_data()
    print(datas)
    await save_user(
        id=sms.from_user.id,
        name=datas['ati'],
        phone_num=datas['phone'],
        adres=datas['adress'],
    )

    await state.clear()



async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
