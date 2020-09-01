##Imprime en consola Hello World.
Imprime en consola Hello World.

##Crea un directorio nuevo llamado new_dir.
mkdir new_dir

##Elimina ese directorio.
rm -r new_dir

##Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy.
cp lorem/sed.txt lorem-copy/sed.txt 

##Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante ;.
##Me dice con ; que tengo permiso denegado o algo así!
cp lorem/at.txt lorem/lorem.txt lorem-copy

##Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.

cat lorem/sed.txt

##Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
cat lorem/at.txt lorem/lorem.txt

##Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy

cat lorem-copy/sed.txt | head -n 3

##Visualiza las ultimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy

cat lorem-copy/sed.txt | tail -n 3

##Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.

echo Homo homini lupus>> lorem-copy/sed.txt

##Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..

cat lorem-copy/sed.txt | tail -n 3

##Sustituye todas las apariciones de et por ET del archivo at.txt dentro de la carpeta lorem-copy. Deberás usar sed.

sed -i 's/et/ET/' lorem-copy/at.txt

##Encuentra al usuario activo en el sistema.
cut -d: -f1 /etc/passwd

##Encuentra dónde estás en tu sistema de ficheros.
pwd 

##Lista los archivos que terminan por .txt en la carpeta lorem.
ls lorem/*.txt

##Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.

cat lorem/sed.txt | wc -l

##Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.

find .  -type f -name "lorem*" -ls | wc -l

##Encuentra todas las apariciones de et en at.txt dentro de la carpeta lorem.
cat lorem/at.txt | grep "et" 

##Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.

cat lorem/at.txt | grep "et" | wc -l

##Cuenta el número de apariciones del string et en todos los archivos del directorio lorem-copy.

cat * | grep "et" | wc -l

## BONUS
##Almacena en una variable name tu nombre.
read name

"""
Me he venido arriba y he hecho un .py con eso...antes de ver que era tan fácil!!

python3 exercices/bonus.py

"""

##Imprime esa variable.
echo $name


##Crea un directorio nuevo que se llame como el contenido de la variable name.
mkdir $name

##Elimina ese directorio.
rm -r $name

##Por cada archivo dentro de la carpeta lorem imprime el número de carácteres que tienen sus nombres. Intenta primero mostrar los archivos 
##mediante un bucle for

##a)Imprime los ficheros
##B)Imprime las longitudes de los nombres de los ficheros
##C)Imprime outputs con la siguiente estructura: lorem has 5 characters lenght
##No lo he conseguido!!

files=("lorem/lorem.txt" "lorem/at.txt" "lorem/sed.txt")
for file in $files
do 
name=basename $file
echo $name
n=  wc -c $name 
echo $n
echo "$name has $n characters length"
done


##Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
##a)Usando el comando top o htop
htop
##b)Usando el comando ps con argumentos
ps -ef

##Muestra información sobre tu procesador por pantalla
sudo dmidecode -s system-manufacturer processor-version

##Crea 3 alias y haz que estén disponibles cada vez que inicias sesión
alias imagenes=/home/silviaherf/pictures
alias home=/home
alias gch='git checkout'

##Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz

 tar -czvf lorem-compressed.tar.gz lorem lorem-copy 

##Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed
mkdir lorem-uncompressed
tar -xzvf lorem-compressed.tar.gz -C lorem-uncompressed