from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8422964630:AAEOwkeCL1sbvaVagCGywyvqTXLMXm-pZ-c"
ADMIN_ID = 8351712593
CHAVE_PIX = "eduardojansen209@gmail.com"

PLANOS = {
    "semanal": 4.99,
    "mensal": 9.99,
    "vitalicio": 24.99
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        [InlineKeyboardButton("📅 Semanal — R$ 4,99", callback_data="plano_semanal")],
        [InlineKeyboardButton("📆 Mensal — R$ 9,99", callback_data="plano_mensal")],
        [InlineKeyboardButton("♾ Vitalício — R$ 24,99", callback_data="plano_vitalicio")]
    ]
    await update.message.reply_text(
        "🤖 *Bem-vindo ao Bot de Assinaturas*\nEscolha um plano abaixo:",
        reply_markup=InlineKeyboardMarkup(teclado),
        parse_mode="Markdown"
    )

async def escolher_plano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    plano = query.data.replace("plano_", "")
    valor = PLANOS[plano]
    await query.edit_message_text(
        f"🧾 Plano: {plano.upper()}\n💰 Valor: R$ {valor}\n💳 Pix: `{CHAVE_PIX}`",
        parse_mode="Markdown"
    )

async def painel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Acesso negado.")
        return
    await update.message.reply_text("📊 Painel do Administrador\n✅ Bot ativo")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("painel", painel))
    app.add_handler(CallbackQueryHandler(escolher_plano))
    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
