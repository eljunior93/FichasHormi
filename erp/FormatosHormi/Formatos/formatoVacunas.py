from fpdf import FPDF
import json
import os
import subprocess
from referencias import *

# Lee datos desde el archivo JSON
with open("postVacunas.json", "r") as json_file:
    data = json.load(json_file)

class PDF(FPDF):
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

pdf = PDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.alias_nb_pages()

pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 6) 


# 1er encabezado ----

bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'A. DATOS DEL ESTABLECIMIENTO - EMPRESA Y USUARIO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

bcol_set(pdf, 'green')
tfont_size(pdf,4.8)
tfont(pdf,'B')
pdf.cell(w = 54, h = 6, txt = 'INSTITUCIÓN DEL SISTEMA O NOMBRE DE LA EMPRESA', border = 1,ln = 2, align = 'L', fill = 1)
tfont(pdf,'')

# Casilla de texto en blanco
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=54, h=5, txt=data['nombre_empresa_vacuna'], border=1, ln=2, align='C', fill=1)  # Casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(60, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=22, h=6, txt='RUC', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(60)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=22, h=5, txt=data['ruc'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(81, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=20, h=6, txt='CIIU', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(81)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=20, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(101, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=45, h=6, txt='ESTABLECIMIENTO DE SALUD', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(101)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(146, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=27, h=6, txt='NÚMERO DE HISTORIA \nCLÍNICA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(146)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=27, h=5, txt=data['historia_clinica'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(173, 13)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=27, h=6, txt='NÚMERO DE ARCHIVO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=27, h=5, txt=data['numero_archivo'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_y(24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=6, txt='PRIMER APELLIDO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
#pdf.set_x(25)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt=data['primer_apellido'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(38, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=27, h=6, txt='SEGUNDO APELLIDO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(38)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=27, h=5, txt=data['segundo_apellido'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(65, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=27, h=6, txt='PRIMER NOMBRE', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(65)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=27, h=5, txt=data['primer_nombre'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(92, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=27, h=6, txt='SEGUNDO NOMBRE', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(92)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=27, h=5, txt=data['segundo_nombre'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(119, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=17, h=6, txt='SEXO', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(119)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=17, h=5, txt=data['sexo'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(136, 24)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=64, h=6, txt='CARGO / OCUPACIÓN', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto en blanco a la derecha
pdf.set_x(136)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=64, h=5, txt=data['ocupacion'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# 2do encabezado ----

pdf.set_y(38)
bcol_set(pdf, 'blue')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 3, txt = 'B. INMUNIZACIONES', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

# Casilla de texto vacunas
pdf.set_y(41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=7, txt='VACUNAS', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul tetanos
pdf.set_y(48)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=25, txt='TÉTANOS - DIFTERIA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul hepatits a
pdf.set_y(73)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=15, txt='HEPATITIS A', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul HEPATITIS B
pdf.set_y(88)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=15, txt='HEPATITIS B', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul INFLUENZA
pdf.set_y(103)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=5, txt='INFLUENZA ESTACIONARIA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul AMARILLA
pdf.set_y(108)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=5, txt='FIEBRE AMARILLA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul SARAMPION
pdf.set_y(113)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=10, txt='SARAMPIÓN - RUBEOLA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul ADICIONAL 1
pdf.set_y(128)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=25, txt='', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul ADICIONAL 2
pdf.set_y(153)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=25, txt='', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul ADICIONAL 3
pdf.set_y(178)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=25, txt='', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul ADICIONAL 4
pdf.set_y(203)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=28, h=25, txt='', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto dosis
pdf.set_xy(38,41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=7, txt='DOSIS', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
######DOSIS TETANO
# Casilla de texto azul
pdf.set_xy(38,48)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul
pdf.set_xy(38,53)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul
pdf.set_xy(38,58)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='3°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul
pdf.set_xy(38,63)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='4°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul
pdf.set_xy(38,68)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='5°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

#######DOSIS HEPATITIS A
# Casilla de texto azul
pdf.set_xy(38,73)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul
pdf.set_xy(38,78)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
# Casilla de texto azul
pdf.set_xy(38,83)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='3°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

#######DOSIS HEPATITIS B
# Casilla de texto azul
pdf.set_xy(38,88)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,93)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,98)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='3°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

#######DOSIS INFLUENZA
pdf.set_xy(38,103)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='ÚNICA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

######DOSIS AMARILLA
pdf.set_xy(38,108)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='ÚNICA', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

######DOSIS SARAMPION
pdf.set_xy(38,113)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,118)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

######DOSIS ADICIONAL 1
pdf.set_xy(38,128)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,133)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,138)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='3°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,143)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='4°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,148)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='5°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

######DOSIS ADICIONAL 2
pdf.set_xy(38,153)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,158)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,163)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='3°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,168)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='4°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,173)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='5°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

######DOSIS ADICIONAL 3
pdf.set_xy(38,178)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,183)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,188)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='3°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,193)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='4°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,198)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='5°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

######DOSIS ADICIONAL 4
pdf.set_xy(38,203)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='1°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,208)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='2°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,213)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='3°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,218)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='4°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
pdf.set_xy(38,223)
bcol_set(pdf, 'blue')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=7, h=5, txt='5°', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

# Casilla de texto fechas
pdf.set_xy(45,41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=18, h=7, txt='FECHA (aaaa/mm/dd)', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
########FECHAS TETANO
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,48)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt=data['fecha_tetano'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,53)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,58)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,63)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,68)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS HEPATITS A
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,73)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,78)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,83)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS HEPATITS B
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,88)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS INFLUENZA 
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS AMARILLA
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS SARAMPION
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS ADICIONAL 1
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,133)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,138)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,143)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,148)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS ADICIONAL 2
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,153)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,158)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,163)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS ADICIONAL 3
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,183)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,188)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,193)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,198)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########FECHAS ADICIONAL 4
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,203)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,208)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,213)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,218)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(45,223)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=18, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto lote
pdf.set_xy(63,41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=12, h=7, txt='LOTE', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')
######LOTE TETANO
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,48)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,53)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,58)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,63)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,68)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE HEPATITIS A
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,73)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,78)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,83)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE HEPATITIS B
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,88)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE INFLUENZA
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE AMARILLA
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE SARAMPION
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE ADICIONAL 1
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,133)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,138)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,143)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,148)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE ADICIONAL 2
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,153)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,158)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,163)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE ADICIONAL 3
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,183)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,188)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,193)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,198)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

######LOTE ADICIONAL 4
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,203)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,208)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,213)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,218)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(63,223)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=12, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto esquema
pdf.set_xy(75, 41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
cell_width = 24
pdf.multi_cell(w=cell_width, h=3.5, txt='ESQUEMA COMPLETO (marca X)', border=1, align='C', fill=1)
tfont(pdf, '')
#####ESQUEMA TETANOS
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,48)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
if data['esquema_tetano'] is True or data['esquema_tetano'] == 'True':
    pdf.cell(w=24, h=5, txt='x', border=1, ln=2, align='C', fill=1)  # Segunda casilla con 'x'
else:
    pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,53)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,58)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,63)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,68)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA HEPATITIS A
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,73)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,78)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,83)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA HEPATITIS B
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,88)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA INFLUENZA
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA AMARILLA
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA SARAMPION
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA ADICIONAL 1
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,133)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,138)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,143)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,148)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA ADICIONAL 2
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,153)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,158)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,163)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA ADICIONAL 3
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,183)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,188)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,193)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,198)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#####ESQUEMA ADICIONAL 4
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,203)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,208)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,213)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,218)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(75,223)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=24, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto nombres
pdf.set_xy(99, 41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 28
pdf.multi_cell(w=cell_width, h=3.5, txt='NOMBRES COMPLETOS DEL RESPONSABLE DE LA VACUNACIÓN', border=1, align='C', fill=1)
tfont(pdf, '')
########nombres tetanos
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,48)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt=data['responsable_tetano'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,53)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,58)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,63)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,68)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres HEPATITIS A
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,73)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,78)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,83)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres HEPATITIS B
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,88)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres INFLUENZA
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres AMARILLA
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres SARAMPION
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres ADICIONAL 1
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,133)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,138)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,143)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,148)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres ADICIONAL 2
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,153)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,158)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,163)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres ADICIONAL 3
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,183)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,188)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,193)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,198)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########nombres ADICIONAL 4
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,203)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,208)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,213)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,218)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(99,223)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto salud vacuna
pdf.set_xy(127, 41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4)
tfont(pdf, 'B')
cell_width = 28
pdf.multi_cell(w=cell_width, h=3.5, txt='ESTABLECIMIENTO DE SALUD DONDE SE COLOCÓ LA VACUNA', border=1, align='C', fill=1)
tfont(pdf, '')
########ESTABLECIMIENTO VACUNA TETANO
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,48)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt=data['establecimiento_tetano'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,53)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,58)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,63)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,68)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO VACUNA HEPATITIS A
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,73)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,78)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,83)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO VACUNA HEPATITIS B
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,88)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO INFLUENZA
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO AMARILLA
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO VACUNA SARAMPION
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO VACUNA ADICIONAL 1
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,133)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,138)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,143)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,148)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO VACUNA ADICIONAL 2
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,153)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,158)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,163)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO VACUNA ADICIONAL 3
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,183)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,188)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,193)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,198)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

########ESTABLECIMIENTO VACUNA ADICIONAL 4
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,203)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,208)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,213)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,218)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(127,223)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=28, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

# Casilla de texto verde
pdf.set_xy(155,41)
bcol_set(pdf, 'green')
tfont_size(pdf, 4.8)
tfont(pdf, 'B')
pdf.cell(w=45, h=7, txt='OBSERVACIONES', border=1, ln=2, align='C', fill=1)
tfont(pdf, '')

#######OBSERVACIONES TETANOS
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,48)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt=data['observaciones_tetano'], border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,53)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,58)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,63)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,68)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES HEPATITS A
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,73)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,78)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,83)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES HEPATITS B
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,88)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,93)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,98)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES INFLUENZA
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,103)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES AMARILLA
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,108)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES SARAMPION
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,113)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,118)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES ADICIONAL 1
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,128)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,133)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,138)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,143)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,148)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES ADICIONAL 2
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,153)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,158)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,163)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,168)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,173)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES ADICIONAL 3
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,178)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,183)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,188)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,193)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,198)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######OBSERVACIONES ADICIONAL 4
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,203)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,208)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,213)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,218)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')
# Casilla de texto en blanco a la derecha
pdf.set_xy(155,223)  # Establecer la posición X para la segunda casilla
pdf.set_fill_color(255, 255, 255)  # Establecer el color de fondo en blanco
pdf.cell(w=45, h=5, txt='', border=1, ln=2, align='C', fill=1)  # Segunda casilla de texto en blanco
tfont(pdf, '')

#######PARRAFOS BLANCOS
pdf.set_y(123)
bcol_set(pdf, 'white')
tfont_size(pdf,6)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 5, txt = 'INMUNIZACIONES DE ACUERDO AL TIPO DE EMPRESA Y RIESGO', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

pdf.set_y(228)
bcol_set(pdf, 'white')
tfont_size(pdf,4)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 6, txt = 'LA VACUNA CONTRA LA FIEBRE AMARILLA ES OBLIGATORIO PARA QUIEN VIVA O SE DESPLACE EN LA REGIÓN AMAZÓNICA, SU APLICACION ES HASTA LOS 59 AÑOS DE EDAD.', border = 1,
         align = 'L', fill = 1)
tfont(pdf,'')

pdf.set_xy(20,270)
bcol_set(pdf, 'white')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 6, txt = 'SNS-MSP-FORM. HCU. 083 / 2019', border = 0,
        fill = 1)
tfont(pdf,'')

pdf.set_xy(108,270)
bcol_set(pdf, 'white')
tfont_size(pdf,7)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 6, txt = 'REGISTRO DE INMUNIZACIONES PARA SALUD EN EL TRABAJO', border = 0,
        fill = 1)
tfont(pdf,'')

# Obtén la ruta del directorio "Documentos"
documentos_path = os.path.join(os.path.expanduser("~"), "Documentos")

# Crea la carpeta "FichasVacunas" dentro de "Documentos" si no existe
fichas_vacunas_path = os.path.join(documentos_path, "FichasVacunas")
os.makedirs(fichas_vacunas_path, exist_ok=True)

# Obtén el valor de 'historia_clinica' del archivo JSON
historia_clinica = data.get('historia_clinica', 'SinHistoriaClinica')

# Define la ruta completa donde deseas guardar el PDF con 'historia_clinica' en el nombre
pdf_filename = f'FormatoVacunas_{historia_clinica}.pdf'
pdf_path = os.path.join(fichas_vacunas_path, pdf_filename)

# Guarda el archivo PDF en la ruta especificada
pdf.output(pdf_path)

# Abre el archivo PDF con el visor de PDF predeterminado del sistema
try:
    subprocess.run(['xdg-open', pdf_path])  # Para sistemas basados en Linux con xdg-open
except OSError:  # Maneja excepciones si xdg-open no está disponible o si no es Linux
    try:
        subprocess.run(['open', pdf_path])  # Para sistemas basados en MacOS
    except OSError:  # Maneja excepciones si open no está disponible o si no es MacOS
        subprocess.run(['start', '', pdf_path], shell=True)  # Para sistemas basados en Windows
