echo Painel de consultas privado;
apt update;
apt upgrade -y;
apt install git -y;
apt install python3 -y;
termux-setup-storage;
pip3 install pyaes;
pip3 install keyboard;
cd storage/downloads;
git clone https://github.com/m7codee/painel_de_buscas;
cd painel_de_buscas;
python3 painel.py;
