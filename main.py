import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Lezen", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Nu lezen", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Nu lezen", url="https://www.nrc.nl")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"))
    text = ("📰 *Welkom bij Dagelijkse Thema's.*\n\n"
        "Elke dag een selectie van cultuur, reizen, "
        "keuken, wetenschap en technologie — "
        "rustig lezen in de chat.\n\n"
        "Tik op *Onderwerpen van de dag* "
        "om te beginnen.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Cultuur — herfsttentoonstellingen", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Keuken — Nederlandse recepten", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Reizen — vijf dorpen", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"))
    text = ("📋 *Onderwerpen van de dag*\n\n"
        "Drie verhalen voor vandaag. "
        "Elk volledig te lezen in de chat.\n\n"
        "*Cultuur* — herfsttentoonstellingen: vijf "
        "afspraken in Nederlandse musea.\n\n"
        "*Keuken* — Nederlandse klassiekers: vier "
        "traditionele recepten.\n\n"
        "*Reizen* — vijf Nederlandse dorpen "
        "voor een herfstig weekend.\n\n"
        "Tik op een titel om het artikel te openen.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"))
    text = ("🎨 *Herfsttentoonstellingen: vijf afspraken "
        "in Nederlandse musea*\n\n"
        "De musea openen het nieuwe seizoen.\n\n"
        "*Amsterdam — Rijksmuseum*\n"
        "Een grote tentoonstelling over de Gouden "
        "Eeuw met zelden vertoonde werken uit "
        "particuliere collecties. Archiefmateriaal "
        "en onuitgegeven brieven.\n\n"
        "*Amsterdam — Van Gogh Museum*\n"
        "De vroege werken van Van Gogh naast "
        "tijdgenoten. Nieuwe inzichten door "
        "moderne restauratietechnieken.\n\n"
        "*Rotterdam — Museum Boijmans*\n"
        "Hedendaagse fotografie uit de Randstad. "
        "Zwart-witreportages over het naoorlogse "
        "Rotterdam. Documentair en poetisch.\n\n"
        "*Den Haag — Mauritshuis*\n"
        "Vermeer en zijn tijdgenoten in een "
        "nieuw licht. Gerestaureerde meesterwerken "
        "met details die eeuwenlang onzichtbaar waren.\n\n"
        "*Utrecht — Centraal Museum*\n"
        "Design en architectuur van Nederlandse "
        "bodem. Zestig jaar alledaagse voorwerpen "
        "opnieuw bekeken.\n\n"
        "_Openingstijden op de museumwebsites._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"))
    text = ("🍳 *Nederlandse klassiekers: vier "
        "traditionele recepten*\n\n"
        "De Nederlandse keuken is eerlijk "
        "en hartverwarmend.\n\n"
        "*Stamppot boerenkool*\n"
        "Aardappelen, boerenkool, rookworst "
        "en een klontje boter. Stampen tot "
        "een grove puree. Het ultieme "
        "wintergerecht.\n\n"
        "*Erwtensoep (snert)*\n"
        "Spliterwten, rookworst, selderij, "
        "prei en spek. Uren koken tot de "
        "lepel erin blijft staan. Serveren "
        "met roggebrood.\n\n"
        "*Bitterballen*\n"
        "Ragout van rundvlees, gepaneerd "
        "en gefrituurd tot goudbruin. Serveren "
        "met mosterd. De ideale borrelsnack.\n\n"
        "*Appeltaart*\n"
        "Zanddeeg, Goudreinetten, kaneel, "
        "rozijnen en een vleugje citroensap. "
        "Gouden korst, warm uit de oven. "
        "Met slagroom.\n\n"
        "_Hoeveelheden naar eigen smaak._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"))
    text = ("🏠 *Vijf Nederlandse dorpen "
        "voor de herfst*\n\n"
        "*Giethoorn (Overijssel)*\n"
        "Het Venetie van het Noorden. Geen "
        "wegen, alleen water en bruggetjes. "
        "In de herfst rustig en betoverend.\n\n"
        "*Veere (Zeeland)*\n"
        "Historisch stadje aan het Veerse Meer. "
        "Gotisch stadhuis, jachthaven en de "
        "mooiste lucht van Nederland.\n\n"
        "*Bourtange (Groningen)*\n"
        "Stervormig vestingdorp uit 1593. "
        "Grachten, kanonnen en kasseien. "
        "Een stap terug in de tijd.\n\n"
        "*Elburg (Gelderland)*\n"
        "Middeleeuws vissersdorp met intacte "
        "stadsmuur. Smalle straatjes, ambachtelijke "
        "winkels en uitzicht over het Veluwemeer.\n\n"
        "*Orvelte (Drenthe)*\n"
        "Openluchtmuseum en levend dorp tegelijk. "
        "Saksische boerderijen, ambachten en "
        "wandelpaden door het Drentse landschap.\n\n"
        "_Verblijf vooraf boeken._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Woordenlijst", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Veelgestelde vragen", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Over ons", callback_data="about"))
    text = ("🏛 *Overzicht*\n\n"
        "Vanuit dit menu kunt u:\n\n"
        "• De *onderwerpen van de dag* lezen.\n"
        "• Rubrieken bekijken: Cultuur, "
        "Reizen, Keuken, Wetenschap.\n"
        "• De woordenlijst en veelgestelde vragen raadplegen.\n"
        "• Over ons lezen en contact opnemen.\n\n"
        "Voor de volledige uitgave "
        "gebruikt u de knop hieronder.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"))
    text = ("📖 *Korte woordenlijst*\n\n"
        "*Redactie* — het team dat teksten "
        "selecteert en voorbereidt.\n\n"
        "*Hoofdartikel* — opiniestuk dat "
        "een rubriek opent.\n\n"
        "*Fotoreportage* — journalistiek verhaal "
        "opgebouwd rond foto's.\n\n"
        "*Tijdloze inhoud* — tekst waarvan de "
        "relevantie niet afhangt van het "
        "dagelijkse nieuws.\n\n"
        "*Correspondent* — journalist die "
        "ter plaatse verslag doet.\n\n"
        "*Rubriek* — vaste afdeling gewijd "
        "aan een bepaald thema.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"))
    text = ("❓ *Veelgestelde vragen*\n\n"
        "*Is deze bot officieel?*\n"
        "Dagelijkse Thema's is een onafhankelijk "
        "redactioneel project.\n\n"
        "*Hoe vaak wordt er bijgewerkt?*\n"
        "De selectie wordt seizoensmatig vernieuwd.\n\n"
        "*Hoe zet ik meldingen uit?*\n"
        "Via de Telegram-chatinstellingen.\n\n"
        "*Kan ik een artikel delen?*\n"
        "Ja, via de deelfunctie van Telegram.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Over ons", callback_data="about"))
    text = ("✏️ *Contact*\n\n"
        "Voor redactionele correspondentie:\n"
        "• E-mail: redactie@dagelijksethemas.nl\n\n"
        "*Uitgever*\n"
        "Dagelijkse Thema's B.V.\n"
        "Herengracht 182\n"
        "1016 BR Amsterdam\n"
        "Nederland\n\n"
        "Reacties van lezers op werkdagen.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Overzicht", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))
    text = ("🏛 *Over Dagelijkse Thema's*\n\n"
        "Dagelijkse Thema's is een onafhankelijk "
        "redactioneel project gewijd aan cultuur, "
        "reizen, keuken en technologie.\n\n"
        "De redactie selecteert dagelijks "
        "kwalitatieve inhoud voor een "
        "geinformeerde pauze.\n\n"
        "Deze Telegram-uitgave is ontworpen "
        "voor comfortabel lezen in de chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Onderwerpen van de dag", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Welkom! Tik op *Onderwerpen van de dag* om te beginnen.", parse_mode="Markdown", reply_markup=markup)


print("Dagelijkse Thema's Bot is running...")
bot.infinity_polling()
