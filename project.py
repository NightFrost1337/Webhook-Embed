from discord_webhook import DiscordWebhook, DiscordEmbed

print("""                               ▄▄        ▄▄                                    
▀████▀     █     ▀███▀        ▄██       ███                         ▀███       
  ▀██     ▄██     ▄█           ██        ██                           ██       
   ██▄   ▄███▄   ▄█    ▄▄█▀██  ██▄████▄  ███████▄   ▄██▀██▄  ▄██▀██▄  ██  ▄██▀ 
    ██▄  █▀ ██▄  █▀   ▄█▀   ██ ██    ▀██ ██    ██  ██▀   ▀████▀   ▀██ ██ ▄█    
    ▀██ █▀  ▀██ █▀    ██▀▀▀▀▀▀ ██     ██ ██    ██  ██     ████     ██ ██▄██    
     ▄██▄    ▄██▄     ██▄    ▄ ██▄   ▄██ ██    ██  ██▄   ▄████▄   ▄██ ██ ▀██▄  
      ██      ██       ▀█████▀ █▀█████▀ ████  ████▄ ▀█████▀  ▀█████▀▄████▄ ██▄▄""")

print("")
print("By NightFrost#0001")
print("")
print("")

lien = input("Entrez le lien du webhook Discord: ")
nomwebhook = input("Entrez le nom du webhook: ")
titrewebhook = input("Entrez le titre de l'embed: ")
textwebhook = input("Entrez le texte du webhook: ")
titre2 = input("Enter le deuxième titre (facultatif): ")
textwebhook2 = input("Enter un deuxième texte (facultatif: ")

webhook = DiscordWebhook(lien, username=nomwebhook)

embed = DiscordEmbed(title=titrewebhook)

embed.set_description(textwebhook)
embed.add_embed_field(name=titre2, value=titrewebhook)
embed.set_footer(text="by NightFrost#0001 (veuillez laissez le crédit)")
embed.set_timestamp()

webhook.add_embed(embed)
response = webhook.execute()

input("Votre embed a été envoyé avec succès au webhook !")