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

lien = input("Entrez le lien du webhook discord => ")
nomwebhook = input("Entrez le nom que tu veux donner au webhook => ")
titrewebhook = input("Entrez le titre de embed => ")
textwebhook = input("Entrez le texte que tu veux => ")
titre2 = input("Enter le deuxième titre => ")
textwebhook2 = input("Enter un deuxième texte => ")

webhook = DiscordWebhook(lien, username=nomwebhook)

embed = DiscordEmbed(title=titrewebhook)

embed.set_description(textwebhook)
embed.add_embed_field(name=titre2, value=titrewebhook)
embed.set_footer(text="by dragon_killl")
embed.set_timestamp()

webhook.add_embed(embed)
response = webhook.execute()

input("Votre webhook a été envoyé ")