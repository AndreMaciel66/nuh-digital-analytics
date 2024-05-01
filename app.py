# %%

import pandas as pd
import folium

# read Anexo I
df_anexo_1 = pd.read_excel('./data/Anexo I - Lista de Escolas com atendimento fotovoltaico.xlsx', sheet_name='Anexo I', skiprows=2)
df_anexo_1.head(10)

# Cria um mapa centrado no Brasil
mapa = folium.Map(location=[-10.3333333, -53.2], zoom_start=5)

# Adiciona círculos para cada escola no DataFrame
for indice, linha in df_anexo_1.iterrows():
    # Escolhe a cor do marcador com base no valor de 'Atendo'
    cor_do_marcador = 'green' if linha['Atendo?'] == 'Atendo' else 'grey'

    folium.CircleMarker(
        location=[linha['Latitude'], linha['Longitude']],
        radius=2,  # Define o tamanho do marcador
        color=cor_do_marcador,
        fill=True,
        fill_color=cor_do_marcador,
        fill_opacity=0.7,
        popup=f"{linha['Nome da Escola']}<br>Velocidade DL: {linha['Velocidade DL (Mbps)']} Mbps<br>Solução: {linha['Solução proposta']}",
        tooltip=linha['Nome da Escola']
    ).add_to(mapa)

# Salva o mapa em um arquivo HTML
mapa.save('mapa_escolas.html')