import telebot
from PIL import Image, ImageOps, ImageFilter
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o token API da variável de ambiente
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Substitua pelo seu token API
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Baixa a foto enviada pelo usuário
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Salva a foto em um arquivo temporário
    src = 'photo.jpg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Abre a foto e o avatar
    img = Image.open(src)
    avatar = Image.open('assets/avatar.png')

    # Redimensiona a foto para se ajustar ao tamanho do avatar, mantendo a proporção original
    img.thumbnail((avatar.size[0], avatar.size[1]), Image.LANCZOS)

    # Cria uma nova imagem com o tamanho do avatar e aplica um desfoque
    background = img.copy()
    background = background.resize((avatar.size[0], avatar.size[1]), Image.LANCZOS)
    background = background.filter(ImageFilter.GaussianBlur(15))

    # Coloca a imagem redimensionada sobre a imagem desfocada
    offset = ((background.size[0] - img.size[0]) // 2, (background.size[1] - img.size[1]) // 2)
    background.paste(img, offset)

    # Ajusta o tamanho do avatar e coloca sobre a imagem combinada
    avatar = avatar.resize((background.size[0], background.size[1]), Image.LANCZOS)
    background.paste(avatar, (0, 0), avatar)

    # Salva a imagem com o avatar
    result_path = 'result.jpg'
    background.save(result_path)

    # Envia a imagem de volta para o usuário
    bot.send_photo(message.chat.id, open(result_path, 'rb'))

    # Remove os arquivos temporários
    os.remove(src)
    os.remove(result_path)

# Inicia o bot
bot.polling()