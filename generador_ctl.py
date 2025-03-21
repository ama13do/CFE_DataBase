# Script para generar un archivo .ctl para la tabla 'linea' con nombres de archivo alineados

def generar_ctl(nombre_archivo_ctl, nombre_tabla, columnas, infile, badfile, discardfile):
    """
    Genera un archivo de control para SQL*Loader.

    :param nombre_archivo_ctl: Nombre del archivo .ctl a generar
    :param nombre_tabla: Nombre de la tabla en la base de datos
    :param columnas: Lista de columnas en la tabla
    :param infile: Ruta al archivo de entrada (.csv)
    :param badfile: Ruta al archivo de errores
    :param discardfile: Ruta al archivo de descartes
    """
    with open(nombre_archivo_ctl, 'w', encoding='utf-8') as ctl:
        ctl.write("LOAD DATA\n")
        ctl.write(f"INFILE '{infile}'\n")
        ctl.write(f"BADFILE '{badfile}'\n")
        ctl.write(f"DISCARDFILE '{discardfile}'\n")
        ctl.write(f"INTO TABLE {nombre_tabla}\n")
        ctl.write("FIELDS TERMINATED BY ','\n")
        ctl.write("OPTIONALLY ENCLOSED BY '\"'\n")
        ctl.write("TRAILING NULLCOLS\n")
        ctl.write("(\n")
        for i, columna in enumerate(columnas):
            if i < len(columnas) - 1:
                ctl.write(f"    {columna},\n")
            else:
                ctl.write(f"    {columna}\n")
        ctl.write(")\n")

def main():
    # Nombre del archivo .ctl a generar
    nombre_archivo_ctl = 'linea.ctl'

    # Nombre de la tabla en la base de datos
    nombre_tabla = 'linea'

    # Lista de columnas de la tabla
    columnas = ['ID_LINEA', 'NUMERO_SECUNCIAL', 'LONGITUD', 'ID_RED']

    # Rutas a los archivos con nombres alineados a 'linea'
    infile = 'C:/Users/braul/Documents/CFE_DATOS_LOGS_BAD/Datos/linea.csv'
    badfile = 'C:/Users/braul/Documents/CFE_DATOS_LOGS_BAD/Bads/linea.bad'
    discardfile = 'C:/Users/braul/Documents/CFE_DATOS_LOGS_BAD/Discards/linea.dsc'

    # Generar el archivo .ctl
    generar_ctl(nombre_archivo_ctl, nombre_tabla, columnas, infile, badfile, discardfile)
    print(f"Archivo de control '{nombre_archivo_ctl}' generado exitosamente.")

if __name__ == "__main__":
    main()
