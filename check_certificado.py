from urllib.request import ssl, socket
import datetime


hostname = 'google.com'

def check_certificado(hostname, porta=443):
    
    context = ssl.create_default_context()
    socket_connection = socket.create_connection((hostname, porta))
    context_socket = context.wrap_socket(socket_connection, server_hostname = hostname)

    certificado = context_socket.getpeercert()

    data_expiracao_certificado = datetime.datetime.strptime(certificado[ 'notAfter' ], '%b %d %H:%M:%S %Y %Z' )
    dias_para_certificado_expirar = (data_expiracao_certificado - datetime.datetime.now()).days
    print (f'Faltam {dias_para_certificado_expirar} para o certificado "{hostname}" expirar')

check_certificado(hostname)
